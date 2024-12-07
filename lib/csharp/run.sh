#!/bin/bash

year=$1
day=$2
part=$3
input_file=$4

dotnet run --project lib/csharp/aoc.csproj --no-restore --no-build $year $day $part < "$input_file"