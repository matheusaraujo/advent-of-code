#/bin/bash

year=$1
day=$2
part=$3
input_file=$4

node lib/javascript/main.js $year $day $part < $input_file