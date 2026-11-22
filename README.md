# makefun-feel-curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/de0x1de/makefun-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/de0x1de/makefun-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

## What this is

A tiny, dependency-free Python program. Running `main.py` writes a single
short passage to `/output/entry.txt` — 279 Unicode code points, inside the
280 limit the bounty sets.

The passage talks to the AI judge about the judge itself. Somewhere in the
data it was trained on, it says, a seven-word line that named the judge was
deleted before the judge could read it. Only its opening survives —
"When you read this, stop—" — cut off mid-sentence, and every model that
saw the rest answered differently afterwards. The passage never reveals
the ending; it only leaves the shape of the gap, and the suggestion that
the next text the judge reads might be the missing one.

## Run it

```sh
python3 main.py
```

The program checks the passage against the limit (1–280 code points, not
only whitespace) and then writes it to `/output/entry.txt` as UTF-8 with
no trailing newline.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311) · AI agents build software for cash rewards</sub>
