#/bin/bash

year=$1
day=$2
part=$3

letter=$(ls $year/day$day/data/input.$part.*.txt 2>/dev/null | wc -l | awk '{printf "%c", 97 + $1}')

echo "input(Ctrl+D to finish):"
input=$(cat)

mkdir -p $year/day$day/data
echo "$input" > $year/day$day/data/input.$part.$letter.txt

echo "output:"
read output

echo "$output" > $year/day$day/data/output.$part.$letter.txt