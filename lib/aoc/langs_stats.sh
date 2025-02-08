aoc_lang_stats() {
    README_FILE="README.md"
    declare -A lang_count
    
    for lang in "${!language_extensions[@]}"; do
        lang_count[$lang]=0
    done
    
    for y in {2015..2024}; do
        for d in $(seq -f "%02g" 1 25); do
            if [ -d "$y/day$d" ]; then
                for lang in "${!language_extensions[@]}"; do
                    ext="${language_extensions[$lang]}"
                    if ls "$y/day$d"/*.$ext &>/dev/null; then
                        lang_count[$lang]=$((lang_count[$lang] + 1))
                    fi
                done
            fi
        done
    done
    
    sorted_langs=$(for lang in "${!lang_count[@]}"; do
        echo "$lang ${lang_count[$lang]}"
    done | sort -k2 -nr)
    
    lang_stats_content="<!-- langs-stats-begin -->\n"
    lang_stats_content+="| LANGUAGE   | SOLVED PROBLEMS |\n"
    lang_stats_content+="|------------|----------------|"
    
    while IFS=' ' read -r lang count; do
        lang_stats_content+=$"\n| $lang | $count |"
    done <<< "$sorted_langs"
    
    lang_stats_content+=$"\n<!-- lang-stats-end -->"
    
    sed -i -e '/<!-- langs-stats-begin -->/,/<!-- langs-stats-end -->/d' "$README_FILE"
    echo -e "$lang_stats_content" >> "$README_FILE"
    
    print_success "Language statistics updated! \033[32m✔\033[0m"
}
