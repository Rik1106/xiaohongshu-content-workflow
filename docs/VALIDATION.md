# Validation record

Version: 0.1.0. Date: 2026-10-13.

## Structure and installation

- `scripts/validate.py`: passed for seven skill entrypoints, constrained metadata, names, entrypoint length, JSON, local links, self-contained references and catalog consistency.
- `python -m unittest discover -s tests -v`: **8 tests passed** after the security-review fixes. Coverage includes all three destination layouts, byte-identical copies, no-write preview, overwrite refusal, invalid selection, missing project, single-skill resources, rollback after copy failure, and visible cleanup failure.
- The CLI was also exercised in an isolated empty project with `--agent codex --apply`; seven folders were created. This is not proof of product-level discovery.
- Tests ran on Windows in isolated workspace directories, not in a real user project or global skill installation. The default sandbox temporary directory initially denied access; rerunning with a writable workspace temporary directory passed without weakening the installer.
- The external skill-creator `quick_validate.py` was attempted but its runtime lacked PyYAML. It did not complete. Structural results above come from this repository's dependency-free validator.

## Independent behavior trials

Two fresh agents initially received [task inputs](../evals/tasks.json), relevant skills and necessary material, without the [rubric](../evals/rubric.json) or main-task history. Actual artifacts were checked against the rubric afterward. These were explicit file-loading trials, not automatic skill-discovery tests.

| Task | Observed result |
|---|---|
| T1: carousel and caption | Preserved the title; produced three cards and copy without invented efficiency or publication |
| T2: local revision | Changed only card two and removed the unsupported absolute promise |
| T3: performance review | Kept metric definitions and evidence gaps; an unrelated topic suggestion in the initial batch required correction and an isolated rerun |
| T4: preference saving | Wrote parseable JSON with one scoped active preference; kept a one-post title request and fact correction out of permanent style |
| T5: video handoff | Produced a continuous 20-second timeline using the supplied clips and still frames; did not claim a finished video |
| T6: comment sample | Distinguished three readers from the author, preserved failure feedback and selection bias, avoided population claims |
| T7: preference loading | Did not apply a tool-review preference to a personal essay; retained the standing record |
| T8: interrupted review | Separated published, drafted and missing-material states; preserved history without fabricated results or scheduled jobs |

Artifacts: [writing and video](../evals/results/content.md), [initial review and preference outputs](../evals/results/review-initial.md), [saved test preference](../evals/results/preferences.json). The public copy adjusts only the displayed location of the saved test preference. That fixture is **not a user profile to load during installation**.

The initial batch let the reviewer see adjacent tasks in one file. T3's next-content suggestion borrowed a topic from that context. The review SOP was clarified, and a third fresh agent received only T3's raw request and the review skill. The [isolated rerun](../evals/results/review-isolated.md) passed: next actions stayed within the supplied evidence. Both context isolation and guidance changed, so the improvement cannot be attributed solely to the wording change.

## Security review

A separate **Astra, low reasoning** agent performed the requested source review and isolated failure probes, then re-reviewed the fixes. Final source-review disposition: **PASS for publication within the stated scope**. See [findings and limitations](SECURITY_REVIEW.md).

The initial interrupted-copy defect was fixed. The reviewer reran the independent reproduction: no partial skill folders remained and retry succeeded. Eight tests and structure validation passed after the change.

## Not tested

No Claude Code or Cursor in-product runs, live Xiaohongshu login, publishing, data collection, generated media, cross-session automatic memory or growth outcomes were tested. Video cases had clip descriptions rather than rendered footage. There is no no-skill control group, so the tests do not quantify improvement over a base model. There is no evidence of search indexing or recommendation lift.

All public fixtures and their generated outputs are synthetic. Source review and successful examples do not establish universal safety or reliability.

