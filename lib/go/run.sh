#!/bin/bash

year=$1
day=$2
part=$3
input_file=$4

curr_dir=$(pwd)

ln -sf $curr_dir/$year/day$day/part1.go $curr_dir/lib/go/part1.go
ln -sf $curr_dir/$year/day$day/part2.go $curr_dir/lib/go/part2.go

if [ -f "$curr_dir/$year/day$day/helpers.go" ]; then
  ln -sf $curr_dir/$year/day$day/helpers.go $curr_dir/lib/go/helpers.go
  helpers_arg="lib/go/helpers.go"
else
  helpers_arg=""
fi

go run lib/go/part1.go lib/go/part2.go $helpers_arg lib/go/main.go $year $day $part < "$input_file"
