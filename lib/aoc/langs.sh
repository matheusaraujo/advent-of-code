#!/bin/bash

# Languages
available_languages=(javascript python perl)

declare -A language_extensions
language_extensions=(
    ["javascript"]="js"
    ["perl"]="pl"
    ["python"]="py"
)

declare -A language_aliases
language_aliases=(
    ["js"]="javascript"
    ["javascript"]="javascript"
    ["pl"]="perl"
    ["perl"]="perl"
    ["py"]="python"
    ["python"]="python"
)