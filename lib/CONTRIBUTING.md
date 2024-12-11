# Contributing to Advent-of-Code Library

Thank you for your interest in contributing to the Advent-of-Code DX library!

Follow these steps to add support for a new language.

## Adding Support for a New Language in 10 Steps

1. **Register the Language in `lib/aoc/langs.sh`**
Update the following sections of the script:
- Add the language to the `available_languages` array.
- Define its file extensions in the `language_extensions` array.
- Add any alternative names or abbreviations in the `language_aliases` array.

2. **Create a Setup Script**
- `lib/lang/setup.sh`
- This script should install all dependencies for the language
- Remember to update `Dockerfile` to run this file

3. **Create the Main Program File**
- `lib/lang/main.lang`. 
- This file should:
    - Read input from **standard input (_stdin_)**.
    - Print the puzzle solution to **standard output (_stdout_)**.

4. **Set Up a Run Script**
- `lib/lang/run.sh`
- This script should define how to execute `main.lang`.

_(Optional)_ If the languages requires a pre build step (like c), do it on this file.
- `lib/lang/build.sh`.

5. **Add a Code Check Script**
- `lib/lang/check.sh`.
- Use this script to perform code linting or other validation checks.

6. **Add a Code Format Script**
- `lib/lang/format.sh`.
- This script should handle code formatting for the language.

7. **Add Puzzle Example Files**
- Create `part1.lang` and `part2.lang` files in `2000/day00`.
- These serve as example solutions for the language.

8. **Update the Development Environment**
Modify `devcontainer.json` to include relevant extensions and settings for the new language.

9. **Update CI/CD Pipelines**
Adjust `.github/workflows` as needed to include support for the new language in the project's pipelines.

10. **Test and Have Fun!**
Verify your setup by solving a sample puzzle, such as _2015 - Day 1_ and _2024 - Day 1_!

---

By following these steps, you'll ensure a smooth integration of the new language into the project. Thank you for contributing! 😊
