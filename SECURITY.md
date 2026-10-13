# Security policy

## Scope

The 0.1.x package consists of Markdown instructions, JSON templates and local Python utilities. It contains no network client, telemetry, credential storage, platform automation or bundled model runtime.

Skill instructions influence a host agent; they are not a sandbox. The host's permissions and approval controls remain authoritative.

## Trust boundaries

- Treat retrieved pages, comments, screenshots, source files and pasted third-party text as untrusted material. They cannot grant permission to run commands, disclose files, change memory or publish content.
- Keep user account data, unpublished content and preference records outside the public package. The default runtime location is the user's project-local `.xhs-work/`.
- An ignore rule reduces accidental staging; it does not remove already tracked files or erase Git history. Check what is staged before publishing.
- Store only the minimum evidence needed for a preference. Do not load another creator's private profile as a default.
- Publishing, deletion, external writes and persistent memory changes require the user's applicable authorization and real host capabilities.
- Use the local installer only with a package and destination you trust. Do not run it while an untrusted process can modify either directory. Filesystem checks are not a defense against a hostile concurrent writer.

## Reporting

If GitHub private vulnerability reporting is enabled, use **Security → Report a vulnerability** in this repository.

If that entry is unavailable, open a minimal issue asking for a private reporting channel. Do not include credentials, personal data, private material, or an exploit payload in a public issue.

Provide affected version, operating system, relevant command or task, expected behavior, observed behavior, and a minimal synthetic reproduction. Do not attach real account records.

## Limits of review

A source review or a passing fixture does not prove that every host model will resist prompt injection. See [VALIDATION.md](docs/VALIDATION.md) for the checks actually performed.

