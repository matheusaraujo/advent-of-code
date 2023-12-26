package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

type Puzzle struct {
	Title      string `json:"title"`
	Year       string `json:"year"`
	Day        string `json:"day"`
	Part1      struct {
		Solved     bool   `json:"solved"`
		OutputFile string `json:"outputFile"`
	} `json:"part1"`
	Part2      struct {
		Solved     bool   `json:"solved"`
		OutputFile string `json:"outputFile"`
	} `json:"part2"`
	InputFile  string `json:"inputFile"`
}

func main() {
	jsonData, err := ioutil.ReadFile("data/" + os.Args[1] + "-" + os.Args[2] + ".json")

	if err != nil {
		fmt.Println("Error reading JSON file:", err)
		return
	}

	var puzzle Puzzle

	err = json.Unmarshal(jsonData, &puzzle)
	if err != nil {
		fmt.Println("Error unmarshalling JSON:", err)
		return
	}

	fmt.Println("go: Running AoC", puzzle.Year, "Day", puzzle.Day, "-", puzzle.Title)

	input := readFile(puzzle.InputFile)

	expectedAnswerPart1 := readFile(puzzle.Part1.OutputFile)
	startTime1 := time.Now()
	answer1 := part1(input)
	endTime1 := time.Now()
	elapsedTime1 := endTime1.Sub(startTime1)
	assertEquals(answer1, expectedAnswerPart1)

	fmt.Printf("\033[35mPart 1: \033[32m%s \033[3;90m(executed in %s) \033[0m\n", fmt.Sprintf("%v", answer1), elapsedTime1.String())

	expectedAnswerPart2 := readFile(puzzle.Part2.OutputFile)
	startTime2 := time.Now()
	answer2 := part2(input)
	endTime2 := time.Now()
	elapsedTime2 := endTime2.Sub(startTime2)
	assertEquals(answer2, expectedAnswerPart2)

	fmt.Printf("\033[35mPart 2: \033[32m%s \033[3;90m(executed in %s) \033[0m\n", fmt.Sprintf("%v", answer2), elapsedTime2.String())
}

func assertEquals(object1 interface{}, object2 interface{}) {
	str1 := fmt.Sprintf("%v", object1)
	str2 := fmt.Sprintf("%v", object2)
	if str1 != str2 {
		panic(fmt.Sprintf("Assertion failed: %s != %s", str1, str2))
	}
}

func readFile(filePath string) (string) {
	fileContent, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(1)
	}

	contentString := string(fileContent)
	return contentString
}
