# aoc-dx specs

some specs ...

## regular dev experience:

```bash
# create scaffolds, if needed; download data from adventofcode.com
$ make init year=2015 day=01 lang=python

# (have fun) solve part 1
$ make run

# part 1 solved, one more star, update data getting solved state from adventofcode.com
$ make update

# (have fun) solve part 2
$ make run
c
# part 2 solved, second star of day!
$ make update

# just checking, or maybe refactoring something
$ make run

# clean up
$ make finish
```

## choosing run modes

the modes can be defined explicitly, or inferred from `data.json`.

```
make run --mode=part1|part2|solved
```

```json
// data.json, part1 mode
{
  "part1": { "solved": false },
  "part2": { "solved": false }
}

// data.json, part2 mode
{
  "part1": { "solved": true },
  "part2": { "solved": false }
}

// data.json, solved mode
{
  "part1": { "solved": true },
  "part2": { "solved": true }
}
```

- part1
  - runs `part1` using all examples, assert answers
  - runs `part1` using default input, does not assert answer
- part2
  - runs `part2` using all examples, assert answers
  - runs `part2` using default input, does not assert answer
- solved
  - runs `part1` using default input, assert answer
  - runs `part2` using default input, assert answer

## choosing puzzle

puzzles are defined by year and day. when you run

```baseh
$ make init year=2015 day=01 lang=python
```

you are automatically choosing December 1st 2015 puzzle, future commands will use this date.

if you want to run or update another puzzle, you can explicitly define it:

```bash
$ make run year=2015 day=02
```

or you can use env vars:

```bash
$ export AOC_YEAR=2015 && export AOC_DAY=02
$ make run
```

> in backstage, `make init` will define the env vars. if for some reason you don't want this behavior, you can use:
> `make init year=2015 day=01 --no-env-vars=true`

## tests operations

- `make test show`
- `make test create`
- `make test delete`
- `make test inactivate`
- `make test activate`
