import kotlinx.serialization.*
import kotlinx.serialization.json.*

// @Serializable
// data class Example(
//     val example: String,
//     val inputFile: String,
//     val outputFile: String
// )

// @Serializable
// data class Part(
//     val part: String,
//     val solved: Boolean,
//     val outputFile: String,
//     val examples: List<Example>
// )

// @Serializable
// data class Puzzle(
//     val title: String,
//     val fullTitle: String,
//     val year: String,
//     val day: String,
//     val part1: Part,
//     val part2: Part,
//     val inputFile: String
// )

fun main(args: Array<String>) {
    println(args[0])
    println(System.getProperty("java.class.path"))
    // val filePath = args[0]
    // val jsonText = File(filePath).readText()

    // val puzzle = Json.decodeFromString<Puzzle>(jsonText)

    // println(puzzle.title)
    // println(puzzle.part1.part)
    // println(puzzle.part1.examples.first().inputFile)
}