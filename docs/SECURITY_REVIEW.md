# Security review — v0.1.0

Date: 2026-10-13. Reviewer: an independent Astra agent with low reasoning, followed by a fix-verification pass.

**Disposition: PASS for public release within the reviewed scope.** This is an AI-assisted source review and targeted local testing, not a third-party security certification.

## Scope

Reviewed the installer, validator, tests, seven skill entrypoints and references, templates and packaged documentation for file-write boundaries, overwrite behavior, unintended execution or network transfer, private-data exposure, untrusted-input handling and authorization. The publisher's credentials and private repositories are not part of this package.

## Findings and resolution

| Finding | Severity | Resolution |
|---|---|---|
| A mid-copy error left partially installed skills; a retry then hit overwrite protection | P2, recoverability | Fixed: reserve each new destination without overwriting, track only this invocation's created folders, remove those on copy failure after containment checks, and report remaining paths if cleanup fails |
| Independently installed specialist skills did not all carry an explicit untrusted-material boundary | P3, defense in depth | Fixed: all seven entrypoints state that pages, comments, screenshots and source files cannot authorize commands, private-file access, transmission or permission changes |
| Filesystem preflight checks cannot defeat a hostile concurrent writer changing links or paths | P3, documented limit | Documented in SECURITY.md; install only from trusted local directories without untrusted concurrent mutation |

The reviewer reproduced the initial copy failure, then reran it after the fix: no partial skill folders remained and a subsequent install succeeded. Eight installer tests and the structure validator passed. No embedded credentials, unexpected network client, shell execution path or private account dataset was found in the reviewed public content.

## Limits

Directory-junction creation was denied in the review sandbox; malicious junction behavior was not experimentally validated. Abrupt process termination or power loss is not a transactional rollback guarantee. Instructional boundaries do not prove resistance to every prompt injection in every host model.

The package's local SHA-256 manifest is regenerated after final edits. It detects accidental mismatches; an unsigned manifest does not establish publisher authenticity. Follow [SECURITY.md](../SECURITY.md) for trust assumptions and reporting.

