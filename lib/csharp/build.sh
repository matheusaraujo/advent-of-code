#!/bin/bash

year=$1
day=$2

additional_files="../../$year/day$day/part1.cs"
if [ -f "$year/day$day/part2.cs" ]; then
    additional_files="$additional_files;../../$year/day$day/part2.cs"
fi
if [ -f "$year/day$day/helpers.cs" ]; then
    additional_files="$additional_files;../../$year/day$day/helpers.cs"
fi

dotnet clean lib/csharp/aoc.csproj --verbosity=quiet > /dev/null 2>&1
if [ $? -ne 0 ]; then
    dotnet clean lib/csharp/aoc.csproj
    exit 1
fi

dotnet build lib/csharp/aoc.csproj /p:AdditionalFiles="\"$additional_files\"" --verbosity=quiet > /dev/null 2>&1
if [ $? -ne 0 ]; then
    dotnet build lib/csharp/aoc.csproj /p:AdditionalFiles="\"$additional_files\""
    exit 1
fi
