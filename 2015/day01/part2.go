package main

func part2(puzzleInput string) int {
	floor := 0
	for i, c := range puzzleInput {
		if c == '(' {
			floor++
		}
		if c == ')' {
			floor--
		}

		if floor == -1 {
			return i + 1
		}
	}
	return 0
}
