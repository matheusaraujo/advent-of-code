#!/bin/bash

# Languages
#available_languages=(c csharp go java javascript python perl)
available_languages=(java)

declare -A language_extensions
language_extensions=(
    ["c"]="c"
    ["csharp"]="cs"
    ["go"]="go"
    ["java"]="java"
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
    ["java"]="java"
    ["js"]="javascript"
    ["javascript"]="javascript"
    ["pl"]="perl"
    ["perl"]="perl"
    ["py"]="python"
    ["python"]="python"
)
