# contributing to advent-of-code lib

Supporting a new language:

1. Create folder `lib/lang`
- `analysis.sh` - script to run analysis for the language
- `lint.sh` - script to run lint for the language
- `main.lang` - code to run the lang, should get input from stdin and print the result to stdout
- `run.sh` - script to call `main.lang`

2. Update `Dockerfile` to install the dependencies
3. Update `devcontainer.json` to include extensions and related settings    
4. Include the language in `lib/aoc/consts.sh`
