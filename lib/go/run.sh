#!/bin/bash

year=$1
day=$2
part=$3
input_file=$4

curr_dir=$(pwd)

part2_arg=""
ln -sf $curr_dir/$year/day$day/part1.go $curr_dir/lib/go/part1.go
if [ -f "$curr_dir/$year/day$day/part2.go" ]; then
  ln -sf $curr_dir/$year/day$day/part2.go $curr_dir/lib/go/part2.go
  part2_arg="lib/go/part2.go"
fi

helpers_arg=""
if [ -f "$curr_dir/$year/day$day/helpers.go" ]; then
  ln -sf $curr_dir/$year/day$day/helpers.go $curr_dir/lib/go/helpers.go
  helpers_arg="lib/go/helpers.go"
fi

go run lib/go/part1.go $part2_arg $helpers_arg lib/go/main.go $year $day $part < "$input_file"
