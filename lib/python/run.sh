#/bin/bash

year=$1
day=$2
part=$3
input_file=$4
output_file=$5

if [ -f "$year/day$day/requirements.txt" ]; then
    pip install -q -r "$year/day$day/requirements.txt"
fi

python3 ./lib/python/main.py $year $day $part $input_file $output_file