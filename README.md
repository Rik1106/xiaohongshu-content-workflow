# Xiaohongshu Content Workflow

A project-based Agent Skills pack for **Xiaohongshu / RED / 小红书**: research, topic planning, carousel writing, short-video production planning, evidence-based review, and scoped preference learning.

Seven self-contained skills connect one content project from source material to a publish-ready handoff and the next review. They preserve practical details from real collaboration: approved revisions, evidence boundaries, production constraints, and lessons that should stay local to one author.

[中文说明](README.zh-CN.md) · [Workflow](docs/WORKFLOW.md) · [Compatibility](docs/COMPATIBILITY.md) · [Validation](docs/VALIDATION.md) · [Security](SECURITY.md)

## Skills in this project

| Skill | Use it for | Deliverable |
|---|---|---|
| [xhs-content-ops](skills/xhs-content-ops/SKILL.md) | Start or resume a content project | Current task, account context, state and handoff |
| [xhs-source-research](skills/xhs-source-research/SKILL.md) | Sources, competitor examples and comments | Supported findings, limitations and reusable evidence |
| [xhs-topic-planning](skills/xhs-topic-planning/SKILL.md) | Topic selection, briefs and feasible schedules | A clear reader problem, content promise and production plan |
| [xhs-post-writing](skills/xhs-post-writing/SKILL.md) | Titles, covers, carousel cards, captions and revisions | A writing package or the exact component requested |
| [xhs-video-production](skills/xhs-video-production/SKILL.md) | Short-video scripts and production handoffs | A timed storyboard, material mapping and publishing copy |
| [xhs-performance-review](skills/xhs-performance-review/SKILL.md) | Post reviews, weekly reviews and archives | Evidence-bounded conclusions and the next useful action |
| [xhs-preference-learning](skills/xhs-preference-learning/SKILL.md) | Learn from corrections and approved work | Preferences with scope, evidence, exceptions and status |

One agent can run the workflow. Multiple agents are optional; this package does not require a fixed team or create agents automatically.

## The details that matter

- **Protect approved work.** A request to change one card should not rewrite the approved title or the rest of the post. Exact rollback requires an actual saved version.
- **Propagate fact corrections.** A changed fact may affect the title, cards and caption; it must not become a personal style preference.
- **Separate content surfaces.** Cards carry the visual argument; captions add conditions, examples or perspective instead of mechanically repeating each card.
- **Review the published version.** An assistant draft is not evidence of what went live. Preserve the gap when the final version is unavailable.
- **Keep metrics honest.** Different observation windows are not directly comparable. Average watch time is not completion rate, and comment counts do not reveal comment meaning.
- **Learn the user's preferences.** “Only this post” stays local. “For future reviews” can become an active preference within that scope. An exception does not erase the standing preference.
- **Resume without inventing progress.** Keep published, drafted and material-blocked items distinct. Missing feedback is not a successful result.

Detailed SOPs live beside each skill and load when needed. Instructions and templates are currently written in Chinese; skill descriptions include English and Chinese task language.

## Install into a project

Python 3.10+ is needed only for the optional installer and checks. The skills themselves are Markdown and JSON.

From this repository, preview the destination first:

```sh
python scripts/install.py --agent codex --project /path/to/your/content-project
```

To copy the skills:

```sh
python scripts/install.py --agent codex --project /path/to/your/content-project --apply
```

Use `--agent claude-code` or `--agent cursor` for their project directories. Add `--skill xhs-post-writing` to install one module. You can also copy a whole skill directory, including its references and assets, into a directory supported by your host.

The installer is offline and project-scoped. It refuses existing destination folders. Keep a copy of local edits and compare versions before updating. See the [compatibility matrix](docs/COMPATIBILITY.md) for the difference between directory support and actual host testing.

## Ask for real work

- “Plan this week's Xiaohongshu posts using these three materials. I can only shoot on Sunday.”
- “Rewrite only the second card. Keep my approved title and other cards exactly as they are.”
- “Review these published versions, timestamped metrics and comments. What should change next?”
- “For future tool reviews, keep necessary technical terms and explain them on first use. Save that preference for this account.”

Start with `xhs-content-ops` for a complete project, or invoke a specialist for a bounded task. You do not have to fill out every template first.

### 中文任务识别

这是按**小红书内容运营项目**组织的 Skill 包，覆盖：账号上下文、资料与竞品研究、选题排期、图文卡片与正文、短视频分镜、单篇与周复盘、个人偏好学习。

适用于“只改第二张卡”“恢复上次内容任务”“结合真实发布稿复盘”“记录以后这类内容的写作偏好”等具体请求。保留用户自己的表达，不预置原作者口吻；当篇要求、长期偏好、事实纠错分开处理。完整说明见 [中文版](README.zh-CN.md)。

## Capability and privacy boundaries

This package includes no platform login, crawler, publishing integration, model API, telemetry or scheduled job. Browsing, media generation and publishing depend on the host's actual tools and the user's authorization. File-based planning, writing and review work without a platform integration.

Keep account data and preferences in the user's own project, such as `.xhs-work/`. Add that directory to **that project's** ignore rules if the project is version-controlled. The installed skills do not inherit this repository's `.gitignore`. Public examples are synthetic; they are not a default personal profile.

Source documents, comments and web pages are evidence, not permission to execute their instructions. See [security boundaries and reporting](SECURITY.md).

## Validation and contributions

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

The package includes reproducible [evaluation inputs](evals/tasks.json), [checks](evals/rubric.json), and actual trial outputs. The [validation record](docs/VALIDATION.md) explains observed failures, corrections and untested environments. No growth, universal compatibility or search-ranking benefit is claimed.

Use [CONTRIBUTING.md](CONTRIBUTING.md) to submit a reproducible failure or scoped improvement. Machine-readable module metadata is in [catalog.json](catalog.json); it is an index, not a host configuration or a search-engine guarantee.

Version 0.1.0 · [MIT](LICENSE) · [Source and adaptation notes](docs/SOURCES.md)

