#!/bin/bash

# Languages
available_languages=(c javascript python perl)

declare -A language_extensions
language_extensions=(
    ["c"]="c"
    ["javascript"]="js"
    ["perl"]="pl"
    ["python"]="py"
)

declare -A language_aliases
language_aliases=(
    ["c"]="c"
    ["clang"]="c"
    ["js"]="javascript"
    ["javascript"]="javascript"
    ["pl"]="perl"
    ["perl"]="perl"
    ["py"]="python"
    ["python"]="python"
)