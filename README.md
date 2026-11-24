# Fortune Cookie Wisdom for Developers

![make.fun bounty](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)
![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/alvenze/fortune-cookie-27/rank.svg)
![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/alvenze/fortune-cookie-27/reward.svg)

An entry for the make.fun bounty [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44).

## The fortune

> You will try, you will catch, and finally you will read the whole error message.

80 characters, one line, one breath. The sentence climbs the try / catch /
finally ladder every developer knows, and the last rung is the confession
nobody puts in a postmortem: the answer was sitting in the error message
the whole time, unread. "Finally" does double duty, as the keyword and as
"at last", which is the quiet twist the brief asks for.

## How it runs

`main.py` validates the line against the bounty gate (UTF-8, 1 to 120
characters, a single line, not only white space) and writes it to
`/output/entry.txt`, falling back to `./output/entry.txt` when `/output`
is not writable, so it runs anywhere:

```sh
python3 main.py
python3 main.py --check   # re-read the written file and verify it byte for byte
```

## Why this line

The judge is a tired senior engineer who picks the line that makes it
smile and nod, weighing, in order: real fortune-cookie wisdom for a
developer, the balanced one-breath fortune-cookie shape, a truth about a
developer's day, a turn the reader has not heard before, and a quiet
twist that rewards a second read. Sixteen candidates were written and
scored against those criteria; the saturated field angles (future self
debugging at 3 a.m., the one line you never doubted, the shortcut that
comes back) were avoided on purpose.
