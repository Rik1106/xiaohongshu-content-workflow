"""Project-scoped, offline installer. Python 3.10+. No overwrite or global writes."""
import argparse
import json
import shutil
from pathlib import Path

TARGETS = {"codex": ".agents/skills", "claude-code": ".claude/skills", "cursor": ".cursor/skills"}

def install(package, project, agent, selected=None, apply=False):
    package, project = Path(package).resolve(), Path(project).resolve()
    if not project.is_dir():
        raise ValueError("Project must be an existing directory")
    if agent not in TARGETS:
        raise ValueError("Unsupported agent")
    sources = {p.name: p for p in (package / "skills").iterdir() if (p / "SKILL.md").is_file()}
    names = sorted(set(selected or sources))
    if not names or any(n not in sources for n in names):
        raise ValueError("Unknown or empty skill selection")
    target = project / TARGETS[agent]
    if not target.resolve().is_relative_to(project):
        raise ValueError("Target escapes project through a link")
    plans = []
    for name in names:
        source, destination = sources[name], target / name
        if destination.exists() or destination.is_symlink():
            raise ValueError("Refusing to overwrite: " + str(destination))
        for p in [source, *source.rglob("*")]:
            if p.is_symlink() or not p.resolve().is_relative_to(package):
                raise ValueError("Linked or escaping source is not supported")
        plans.append((source, destination))
    if apply:
        target.mkdir(parents=True, exist_ok=True)
        created = []
        try:
            for source, destination in plans:
                # Reserve ownership without replacing a folder created after preflight.
                destination.mkdir(exist_ok=False)
                created.append(destination)
                shutil.copytree(source, destination, dirs_exist_ok=True)
        except Exception as exc:
            remaining = []
            for destination in reversed(created):
                try:
                    # Only remove directories created by this invocation, inside this project.
                    if destination.is_symlink() or not destination.resolve().is_relative_to(project):
                        raise OSError("Cleanup target changed or escaped project")
                    shutil.rmtree(destination)
                except OSError:
                    remaining.append(str(destination))
            if remaining:
                raise OSError("Install failed; cleanup incomplete. Inspect these newly created folders before retrying: " + "; ".join(remaining)) from exc
            raise OSError("Install failed; newly created skill folders were removed. " + str(exc)) from exc
    return {"applied": apply, "agent": agent, "destinations": [str(d) for _, d in plans]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=TARGETS, required=True)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--skill", action="append", dest="selected")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parents[1], args.project, args.agent, args.selected, args.apply)
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
