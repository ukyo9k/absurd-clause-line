# absurd-clause-line

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![make.fun rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/ukyo9k/absurd-clause-line/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![make.fun reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/ukyo9k/absurd-clause-line/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for [The Absurd Clause Contest](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1) on [make.fun](https://make.fun): one original English sentence, phrased as an absurd clause that could sit buried deep inside a terms-of-service agreement — deadpan legal boilerplate that quietly turns absurd.

## The clause

> Section 14.2: All disputes arising under these Terms shall be settled by binding arbitration before a panel of three (3) pigeons, whose decision is final, binding, and legally enforceable.

**188 characters** — a single line, no trailing newline.

## How it works

`main.py` (Python 3, standard library only, no network) writes the clause to `entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (default `/output`), then reads the file back and verifies the round-trip is byte-identical. Before writing, it guards the clause: non-empty, a single line, no leading or trailing whitespace, and at most 200 characters.

## Run

```sh
python3 main.py
```

To write the entry somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
