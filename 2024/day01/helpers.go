package main

import (
	"sort"
	"strconv"
	"strings"
)

func stringToInt(str string) int {
	i, err := strconv.Atoi(str)
	if err != nil {
		panic(err)
	}
	return i
}

func parseInput(puzzleInput string) ([]int, []int) {
	var left, right []int
	lines := strings.Split(strings.TrimSpace(puzzleInput), "\n")

	for _, line := range lines {
		parts := strings.Fields(line) // Split by any whitespace
		left = append(left, stringToInt(parts[0]))
		right = append(right, stringToInt(parts[1]))
	}

	sort.Ints(left)
	sort.Ints(right)

	return left, right
}
