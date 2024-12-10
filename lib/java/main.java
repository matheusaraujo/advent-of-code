import java.util.Scanner;

public class main {
    public static void main(String[] args) {
            
        String part = args[2];
        StringBuilder puzzleInput = new StringBuilder();

        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            puzzleInput.append(scanner.nextLine()).append("\n");
        }
        scanner.close();

        if (part.equals("part1")) {
            System.out.println(part1.solve(puzzleInput.toString()));
        } else if (part.equals("part2")) {
            System.out.println(part2.solve(puzzleInput.toString()));
        }
    }
}