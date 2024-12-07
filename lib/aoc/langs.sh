#!/bin/bash

# Languages
available_languages=(c csharp go javascript python perl)

declare -A language_extensions
language_extensions=(
    ["c"]="c"
    ["csharp"]="cs"
    ["go"]="go"
    ["javascript"]="js"
    ["perl"]="pl"
    ["python"]="py"
)

declare -A language_aliases
language_aliases=(
    ["c"]="c"
    ["clang"]="c"
    ["csharp"]="csharp"
    ["c#"]="csharp"
    ["go"]="go"
    ["golang"]="go"
    ["js"]="javascript"
    ["javascript"]="javascript"
    ["pl"]="perl"
    ["perl"]="perl"
    ["py"]="python"
    ["python"]="python"
)