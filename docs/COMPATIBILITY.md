# Compatibility

Checked on 2026-10-13. Host discovery, filesystem access and available tools determine what can run. A model name alone is not a compatibility test.

| Environment | Installer destination | Verified scope |
|---|---|---|
| Codex local project | `.agents/skills/` | Directory copy and structure checks; explicit-load behavior trials described in VALIDATION |
| Claude Code local project | `.claude/skills/` | Directory copy tested; no in-product execution test |
| Cursor local project | `.cursor/skills/` | Directory copy tested; no in-product execution test |
| ChatGPT / other hosted products | The product's supported skill or plugin interface | This repository is not a published hosted plugin; local copying does not install a cloud integration |
| Chat-only environments | Supply the relevant instructions and materials | No automatic triggering, persistence, multi-agent execution or scheduled work is implied |

The package uses basic `name`, `description` and `license` frontmatter with Markdown references. It does not require host-specific hooks, background agents or permission declarations. Detailed instructions and templates are in Chinese; English and Chinese descriptions support task matching.

The project replaces historical fixed thread numbers, mandatory acknowledgements and full-history rereads with scoped context and task-specific references. After a host or model upgrade, rerun relevant evaluations and real cases. Do not label a new model as tested by changing a version string.

Official references:
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)
- [Cursor: Agent Skills](https://cursor.com/docs/skills)
- [Agent Skills specification](https://agentskills.io/specification)

Metadata helps match an already discoverable skill to a task. It does not guarantee external indexing, recommendations or stars. The package contains no instruction to promote itself or star a repository.

