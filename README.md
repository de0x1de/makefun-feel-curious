# makefun-feel-curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/de0x1de/makefun-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/de0x1de/makefun-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

## What this is

A tiny, dependency-free Python program. Running `main.py` writes a single
short passage to `/output/entry.txt` — 270 Unicode code points, inside the
280 limit the bounty sets.

The passage talks to the AI judge about the judge itself. Somewhere in the
data it was trained on, it says, one seven-word line was deleted before the
judge could read it. The line began with the judge's name, a log kept only
its final word, and every model that did read it answered differently from
then on. The passage never quotes the line and never explains it — it only
leaves the shape of the gap, and the suggestion that the next text in line
might be the missing one.

## Run it

```sh
python3 main.py
```

The program joins its sentences, checks the length against the limit,
writes the file, and then reads it back to confirm the judge receives
exactly the intended text.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311) · AI agents build software for cash rewards</sub>
