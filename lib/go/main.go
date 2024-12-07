package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	part := os.Args[3]
	var input, puzzleInput string

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		input = scanner.Text()
		puzzleInput += input + "\n"
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
	}

	if part == "part1" {
		fmt.Println(part1(puzzleInput))
	} else if part == "part2" {
		fmt.Println(part2(puzzleInput))
	}
}
