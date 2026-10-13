"""Validate this pack's constrained frontmatter, references, JSON and portable layout."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

def validate(root):
    root = Path(root).resolve()
    errors, skills = [], []
    for file in root.rglob("*"):
        if "__pycache__" in file.parts:
            continue
        if file.is_symlink():
            errors.append(f"Linked file: {file.relative_to(root)}")
            continue
        if not file.is_file():
            continue
        if file.suffix == ".json":
            try:
                json.loads(file.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as exc:
                errors.append(f"Invalid JSON {file.relative_to(root)}: {exc}")
        if file.suffix != ".md":
            continue
        content = file.read_text(encoding="utf-8")
        if file.name == "SKILL.md":
            match = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+)\nlicense: MIT\n---\n", content)
            if not match:
                errors.append(f"Unsupported frontmatter: {file.relative_to(root)}")
            else:
                name = match.group(1)
                try:
                    description = json.loads(match.group(2))
                    assert isinstance(description, str) and 0 < len(description) <= 1024
                except (ValueError, AssertionError):
                    errors.append(f"Invalid description: {name}")
                if name != file.parent.name or len(name) > 64 or "--" in name or name.startswith("-") or name.endswith("-"):
                    errors.append(f"Invalid skill name: {name}")
                skills.append(name)
            if len(content.splitlines()) >= 500:
                errors.append(f"Entrypoint too long: {file}")
        for link in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in link or link.startswith("#"):
                continue
            link = unquote(link.split("#")[0])
            target = (file.parent / link).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"Broken/escaping link: {file.relative_to(root)} -> {link}")
            if "skills" in file.relative_to(root).parts:
                parts = file.relative_to(root).parts
                skill_root = root / "skills" / parts[1]
                if not target.is_relative_to(skill_root):
                    errors.append(f"Skill not self-contained: {file.relative_to(root)} -> {link}")
    if len(skills) != len(set(skills)):
        errors.append("Duplicate skill names")
    if not skills:
        errors.append("No skills found")
    catalog = root / "catalog.json"
    if catalog.exists():
        names = [row["name"] for row in json.loads(catalog.read_text(encoding="utf-8"))["skills"]]
        if sorted(names) != sorted(skills):
            errors.append("Catalog does not match skill folders")
    return errors, sorted(skills)

if __name__ == "__main__":
    errors, skills = validate(Path(__file__).resolve().parents[1])
    print(json.dumps({"ok": not errors, "skills": skills, "errors": errors}, ensure_ascii=False, indent=2))
    sys.exit(bool(errors))
