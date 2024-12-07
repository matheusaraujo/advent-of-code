#!/bin/bash

year=$1
day=$2
part=$3
input_file=$4

curr_dir=$(pwd)
ln -sf $curr_dir/$year/day$day/part1.go $curr_dir/lib/go/part1.go
ln -sf $curr_dir/$year/day$day/part2.go $curr_dir/lib/go/part2.go

go run lib/go/part1.go lib/go/part2.go lib/go/main.go $year $day $part < "$input_file"