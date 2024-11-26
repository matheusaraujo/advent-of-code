#!/bin/bash

# Function to generate progress bar and percentage
generate_progress_bar() {
    local solved_days=$1
    local total_days=25
    local filled=$((solved_days))
    local empty=$((total_days - solved_days))
    local progress_bar=""

    # Create the filled part of the progress bar
    for ((i=0; i<filled; i++)); do
        progress_bar+="█"
    done

    # Create the empty part of the progress bar
    for ((i=0; i<empty; i++)); do
        progress_bar+="-"
    done

    # Calculate the percentage
    local percentage=$((solved_days * 100 / total_days))

    # Return the progress bar and percentage
    echo "$progress_bar $solved_days/25 ($percentage%)"
}

# Define an array of Christmas and coding-related emojis
emojis=("🎄" "🎅" "🎁" "❄️" "💻" "👨‍💻" "👩‍💻" "🧑‍💻" "🎉" "🧑‍🎄")

# Define the file path
README_FILE="README.md"

# Start the table with the updated header
new_content="<!-- progress-begin -->
| YEAR          | PROGRESS                      | COMPLETED (Out of 25) |
|---------------|-------------------------------|-----------------------|"

# Loop through years (2015 to 2024)
for year in {2015..2024}; do
    solved_days=0
    
    # Loop through days (01 to 25)
    for day in $(seq -f "%02g" 1 25); do
        # Check if the day folder and README.md exist
        if [ -d "$year/day$day" ] && [ -f "$year/day$day/README.md" ]; then
            solved_days=$((solved_days + 1))
        fi
    done

    # Pick a random emoji from the array
    emoji=${emojis[$RANDOM % ${#emojis[@]}]}

    # Generate the progress bar and completed count
    progress=$(generate_progress_bar $solved_days)
    
    # Add the row for this year with emoji in the YEAR column
    new_content+=$"\n| $emoji $year | $progress | $solved_days/25 ($((solved_days * 100 / 25))%) |"
done

# Finish the table
new_content+=$"\n<!-- progress-end -->"

# Use awk to safely replace content between the markers
awk '
  BEGIN {start=0; end=0}
  /<!-- progress-begin -->/ {start=1}
  /<!-- progress-end -->/ {end=1; print new_content; next}
  start==0 || end==0 {print $0}
' new_content="$new_content" "$README_FILE" > temp && mv temp "$README_FILE"

echo "Progress table updated in README.md"
