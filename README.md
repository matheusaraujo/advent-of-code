## Usage

```bash
# language is auto detected based on existence of part1 file on day folder
# multiple languages per day is supported

# run a specific day
$ make run year=${year} day={day}

# lint for a specific day
$ make lint year=${year} day={day}
$ make lint year=${year} day={day} fix=true

```

## Supported languages

### c

```c
// part1.c

int part1(const char* puzzle_input) {
    return 0;
}
```

### cpp

```cpp
// part1.cpp

#include <iostream>
#include <cstring>

using std::string;

int part1(const string& puzzle_input) {
    return 0;
}
```

### csharp

```csharp
// Part1.cs

namespace aoc;

public static class Part1
{
    public static object Solve(string puzzleInput)
    {
        return 0;
    }
}
```

### go

```go
// part1.go

package main

import (
	"strings"
)

func part1(puzzleInput string) interface{} {
	return 0
}

```

### java

```java
// Part1.java

public class Part1 {
    public static Object solve(String puzzleInput) {
        return 0;
    }
}

```

### js

```js
// part1.js

function part1(data) {
  return 0;
}

module.exports = part1;
```

### python

```python
# part1.py

def part1(puzzle_input):
    return 0
```
