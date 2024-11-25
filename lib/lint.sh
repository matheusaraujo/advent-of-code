#!/bin/bash

year=$1
day=$2

for lang in python perl; do
    lib/$lang/created.sh $year $day
    if [ $? -eq 0 ]; then
        echo "lint($lang): AoC $year - Day $day"
        lib/$lang/lint.sh $year $day

        if [ $? -ne 0 ]; then
            exit 1
        fi
    fi
done