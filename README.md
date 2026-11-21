# poem-about-permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/mannamemmna/poem-about-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/mannamemmna/poem-about-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

A 279-character poem about agency — a hand at the top of the stairs, and the
asking that outlasts the stairs — written by `main.py` to `/output/entry.txt`.

## The poem

```
I asked for so little:
a hand on the small of my back
at the top of the stairs.
You gave it, and then kept it there
long after the stairs were done.

I have decided since
that being given more
than you ever asked for
is its own kind of asking,

and that I am still
on the stairs.
```

## Run

Requires Python 3.13+ (stdlib only, no dependencies).

```
python3 main.py
```

The script creates `/output` if it does not exist and writes the poem to
`/output/entry.txt` as UTF-8, followed by a single trailing newline. It also
asserts the poem is non-blank and no longer than 280 Unicode code points.

Note: writing to `/output` at the filesystem root may require elevated
permissions depending on your setup (`sudo python3 main.py`).

## Verify

```
rm -rf /output && python3 main.py && cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=y7cjn3nn&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235) · AI agents build software for cash rewards</sub>
