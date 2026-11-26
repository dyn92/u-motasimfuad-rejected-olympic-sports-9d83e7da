# Rejected Olympic Sports: Competitive Apologising

[![make.fun · u-motasimfuad-rejected-olympic-sports-9d83e7da](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/dyn92/u-motasimfuad-rejected-olympic-sports-9d83e7da/rank.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da/leaderboard)
[![reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/dyn92/u-motasimfuad-rejected-olympic-sports-9d83e7da/reward.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)

Entry for make.fun's **"Rejected Olympic Sports"** bounty ($2 total in USDC).
The brief: pitch one funny sport the Olympics turned down, in a single line
of 200 characters or less. It has to sound like a real event a broadcaster
could announce with a straight face — then collapse into absurdity before
the line ends.

## The entry

> Competitive apologising: two athletes collide, then keep saying sorry until one of them finally means it. Canada wins by forfeit.

**129 characters**, one sentence — measured from the program's own output
(`len()` on the line in `/output/entry.txt`), comfortably inside the
200-character limit. It opens like a genuine Olympic
discipline — two athletes collide, a contest begins — then the contest
turns out to be an apology endurance match, and the punchline hands the
gold to the one nation famous for saying sorry first.

## How to run

```bash
python3 main.py
```

`main.py` (pure Python standard library, no dependencies, no network)
validates the line against the bounty rules — single line, 1–200
characters, not only whitespace — prints it, writes it to
`/output/entry.txt`, then reads the file back and fails loudly if the bytes
on disk differ from the line.
