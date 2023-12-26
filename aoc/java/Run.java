import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Run {
    public static void main(String[] args) {
        String filePath = "data/" + args[0] + "-" + args[1] + ".json";

        String fileContent = readFile(filePath);
        String[] extractedProperties = extractProperties(fileContent);

        String title = extractedProperties[0];
        String year = extractedProperties[1];
        String day = extractedProperties[2];
        String inputFile = extractedProperties[3];
        String input = readFile(inputFile);
        String part1OutputFile = extractedProperties[4];
        String expectedResultPart1 = readFile(part1OutputFile);
        String part2OutputFile = extractedProperties[5];
        String expectedResultPart2 = readFile(part2OutputFile);

        System.out.println("java: Running AoC " + year + " Day " + day + " - " + title);

        long startTime1 = System.nanoTime();
        Object answer1 = Part1.solve(input);
        long endTime1 = System.nanoTime();
        double executionTime1 = ((double)endTime1 - startTime1) / 1_000_000;
        assert answer1 == expectedResultPart1 : "Part 1 Failed";
        System.out.println("\033[35mPart 1: \033[32m" +
            answer1 +
            "\033[3;90m (executed in " + String.format("%.2f", executionTime1) + "ms) \033[0m"
        );

        long startTime2 = System.nanoTime();
        Object answer2 = Part2.solve(input);
        long endTime2 = System.nanoTime();
        double executionTime2 = ((double)endTime2 - startTime2) / 1_000_000;
        assert answer2 == expectedResultPart2 : "Part 2 Failed";
        System.out.println("\033[35mPart 2: \033[32m" +
            answer2 +
            "\033[3;90m (executed in " + String.format("%.2f", executionTime2) + "ms) \033[0m"
        );
    }

    public static String readFile(String filePath) {
        StringBuilder content = new StringBuilder();

        try {
            File file = new File(filePath);

            if (!file.exists()) {
                System.out.println("File not found.");
                return "";
            }

            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line;

            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }

            reader.close();
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file: " + e.getMessage());
        }

        return content.toString();
    }

    public static String[] extractProperties(String fileContent) {
        if (fileContent.isEmpty()) {
            System.out.println("File content is empty.");
            return new String[0];
        }

        String title = extractValue(fileContent, "\"title\": \"", "\"");
        String year = extractValue(fileContent, "\"year\": \"", "\"");
        String day = extractValue(fileContent, "\"day\": \"", "\"");
        String inputFile = extractValue(fileContent, "\"inputFile\": \"", "\"");
        String part1OutputFile = extractNestedValue(fileContent, "\"part1\":", "\"outputFile\": \"", "\"");
        String part2OutputFile = extractNestedValue(fileContent, "\"part2\":", "\"outputFile\": \"", "\"");

        return new String[]{title, year, day, inputFile, part1OutputFile, part2OutputFile};
    }

    public static String extractValue(String content, String startTag, String endTag) {
        int startIndex = content.indexOf(startTag);
        if (startIndex == -1) {
            return "";
        }

        int endIndex = content.indexOf(endTag, startIndex + startTag.length());
        if (endIndex == -1) {
            return "";
        }

        return content.substring(startIndex + startTag.length(), endIndex);
    }

    public static String extractNestedValue(String content, String parentTag, String startTag, String endTag) {
        int startIndex = content.indexOf(parentTag);
        if (startIndex == -1) {
            return "";
        }

        content = content.substring(startIndex);

        return extractValue(content, startTag, endTag);
    }
}
