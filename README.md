# Notes From a Passive-Aggressive Fridge

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/kimbaex07/fridge-note-door/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/kimbaex07/fridge-note-door/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

## The entry

> I kept the light on for you. The yogurt left three days ago — it said it couldn’t do this anymore.

**Character count: 98** (gate: 1–200 characters, single line, UTF-8).

## Why it lands

The fridge opens with a small act of devotion — keeping the light on — and immediately undercuts it with a petty betrayal: the yogurt walked out on the owner. It is smug in exactly the way a sensor-laden appliance would be, keeping tabs on who left and when, while the grudge stays small and domestic. The sting lands in the final clause, where the yogurt gets a voice and a reason to quit, turning an expired dairy product into a household resignation letter.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

This writes the note to `./out/entry.txt` — exactly the note, one trailing newline, nothing else. Pure Python 3 standard library, deterministic, no network, no randomness.

## Testing

Run the entry twice into a scratch directory and compare the outputs — they are byte-identical (same sha256) and match the committed `entry.txt`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fridge-rev python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/fridge-rev2 python3 main.py
sha256sum /tmp/fridge-rev/entry.txt /tmp/fridge-rev2/entry.txt entry.txt
```

The write is atomic (temp file in the same directory, flushed and fsynced, then renamed), so a crash can never leave a partial `entry.txt` behind.
