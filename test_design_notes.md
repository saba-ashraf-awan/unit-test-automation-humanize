# Test Design Notes (ECP + BVA) — Project: python-humanize
Group members: **Saba Ashraf (24F-3064)** and **Maryum Qayyum (24F-3045)**

| Module | Saba Ashraf (24F-3064) | Maryum Qayyum (24F-3045) |
|---|---|---|
| number | intcomma, intword, ordinal | apnumber, fractional, scientific, metric |
| filesize | naturalsize: decimal + GNU mode | naturalsize: binary mode, negatives, invalid input |
| lists | natural_list: length boundaries, CSV | natural_list: iterable types, formatting rules |


Modules under test: `humanize.number`, `humanize.filesize`, `humanize.lists`

## Module 1: humanize.number
### intcomma(value)
- ECP: valid positive int | valid negative int | zero | float | non-numeric string | None
- BVA: 999 (no comma) / 1000 (first comma) / 1,000,000
- Expected: 999->"999", 1000->"1,000", -1000->"-1,000", "abc"->"abc" (returned unchanged), None->"None" (str of input)
### intword(value)
- ECP: below-thousand | thousand | million | billion | non-numeric
- BVA: 999 -> "999"; 1000 -> "1.0 thousand"; 1_000_000 -> "1.0 million"
### ordinal(value)
- ECP: normal (1st,2nd,3rd,4th) | teens exception (11,12,13) | >100 (101,111) | zero | negative
- BVA: 0, 1, 10-14, 20-24, 100-114
### apnumber(value)
- ECP: 0 ("zero") | 1-9 (words) | >=10 (digits) | non-numeric
- BVA: 0, 1, 9, 10
### scientific(value, precision) / metric(value, unit)
- ECP: large | small (<1) | one | non-numeric ; metric: kilo | milli | base unit | zero | no unit
- BVA: scientific 1 -> "1.00 x 10⁰"; metric 0 -> "0.00", 1 -> "1.00 W"
### fractional(value)
- ECP: whole number | proper fraction | mixed | zero

## Module 2: humanize.filesize
### naturalsize(value, binary, gnu)
- ECP: zero | singular (1 Byte) | bytes (<1000) | kB/MB (decimal) | negative
- BVA: 0, 1, 999, 1000, 1023, 1024, 1048576
- Decision table on flags: (binary=F,gnu=F) | (binary=T) | (gnu=T)
- Expected: 1024 -> "1.0 kB" / "1.0 KiB" (binary) / "1.0K" (gnu)

## Module 3: humanize.lists
### natural_list(items)
- ECP: empty | 1 item | 2 items | 3+ items | non-string items | generator/iterable
- BVA on length: 0, 1, 2, 3
- Expected: []->"" ; [x]->"x" ; [a,b]->"a and b" ; [a,b,c]->"a, b and c"

## Techniques used
Equivalence Class Partitioning, Boundary Value Analysis, Decision Table (flags), Error Guessing (None, "abc").
