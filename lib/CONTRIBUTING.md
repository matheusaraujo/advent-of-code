# contributing to advent-of-code lib

Supporting a new language:

1. Include the language in `lib/aoc/langs.sh`
    - `available_languages`
    - `language_extensions`
    - `language_aliases`
2. Create folder `lib/lang`
    - `check.sh` - script to run checks for the language
    - `format.sh` - script to format code in the language
    - `main.lang` - code to run the lang, should get input from stdin and print the result to stdout
    - `run.sh` - script to call `main.lang`
3. Update `Dockerfile` to install the dependencies
4. Update `devcontainer.json` to include extensions and related settings
5. Update the pipelines `.github/workflows` if necessary

