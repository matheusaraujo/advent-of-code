#/usr/bash

year=$1
day=$2
part=$3
input_file=$4

java -cp "$year/day$day:lib/java" main $year $day $part < "$input_file"