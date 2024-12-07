package main

import (
	"strings"
)

func part1(puzzleInput string) interface{} {
	openParentheses := strings.Count(puzzleInput, "(")
	closeParentheses := strings.Count(puzzleInput, ")")

	return openParentheses - closeParentheses
}
