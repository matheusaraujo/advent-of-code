#!/bin/bash

year=$1
day=$2

for lang in python perl; do
    lib/$lang/created.sh $year $day
    if [ $? -eq 0 ]; then
        echo "analysis($lang): AoC $year - Day $day"
        lib/$lang/analysis.sh $year $day
    fi
done