#!/bin/bash

# year=$1
# day=$2

# files="lib/java/main.java $year/day$day/part1.java"

# helpers_file="$year/day$day/helpers.java"
# if [[ -f "$helpers_file" ]]; then
#     files="$files $helpers_file"
# fi

# part2_file="$year/day$day/part2.java"
# if [[ -f "$part2_file" ]]; then
#     files="$files $part2_file"
# fi

# javac $files

#pmd check -d $year/day$day -R rulesets/java/quickstart.xml
#pmd check -d $year/day$day -R lib/java/ruleset.xml

#!/bin/bash

year=$1
day=$2


files=("part1.java" "part2.java" "helpers.java")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        pmd check -d $year/day$day/$file -R lib/java/ruleset.xml 
    fi
done
