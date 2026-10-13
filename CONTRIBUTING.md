# Contributing

Start with one concrete failure: share a public-safe input, the observed output, the intended behavior, scope, and a counterexample when useful. Use synthetic material when the real input includes private messages, account data or someone else's unpublished work.

Keep a one-off correction in its case. Put a stable, scoped procedure in the relevant reference. Change `SKILL.md` when discovery or execution guidance actually needs to change. Avoid global word bans, one mandatory voice, or fixed posting quotas.

Run:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

For behavioral changes, rerun the affected evaluation in a fresh context using only that task's inputs. Record the host, available model/version information, input, actual output, and any manual edits. Keep the rubric away from the executing agent until the run is complete. Report failures and untested environments; a model's self-assessment is not an outcome measurement.

Do not commit secrets, personal preference stores, original private conversations or unlicensed media. Report security concerns using [SECURITY.md](SECURITY.md).

中文：欢迎提交具体失败案例与有适用范围的改进。请脱敏，保留实际输入输出，不把个人文风或一次纠正升级成所有人的强制规则。

