package main

func part2(puzzleInput string) int {
	left, right := parseInput(puzzleInput)

	count := make(map[int]int)
	for _, x := range left {
		count[x]++
	}

	result := 0
	for _, item := range right {
		if countValue, exists := count[item]; exists {
			result += item * countValue
		}
	}
	return result
}
