#!/bin/bash

# TODO: @matheusaraujo - improve this, reading ignore patterns from .gitignore file

aoc_clean() {
  declare -a patterns=(
    "**/_readme*.html"
    "**/data/*"
    "helpers.sh"
    "lib/c/run"
    "*.plist"
    "lib/csharp/Part1.cs"
    "lib/csharp/Part2.cs"
    "lib/csharp/obj/"
    "lib/csharp/bin/"
    "**/bin/"
    "**/obj/"
    "**/check.csproj"
    "**/day**/Program.cs"
    "lib/go/part1.go"
    "lib/go/part2.go"
    "*.class"
    "node_modules/"
    "*.pl.bak"
    "*.pl.tdy"
    "*.pl.ERR"
    "__pycache__/"
  )
  
  for pattern in "${patterns[@]}"; do
    matches=$(find . -type f -name "${pattern}" -o -type d -name "${pattern}" 2>/dev/null)
    if [[ -n "$matches" ]]; then
      rm -rf $matches
    fi
  done

  echo "Cleaning completed."
}
