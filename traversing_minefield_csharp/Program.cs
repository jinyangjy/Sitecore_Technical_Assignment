using System;
using System.Collections.Generic;

class Program
{
    /*
    Approach Description: The number of rows and columns in the minefield are determined.
    In the minefield:
    Bombs are represented as : "1"
    Safe Spots are represented as: "0"
    We start off by creating two empty lists to store the paths for Totoshka and Ally.
    Then we will find the first index where Totoshka can start by looking for the first "0"
    in the first row. Since Ally is following Totoshka, we will initialize Ally's position
    to "None" to have it as a one step delay. The loop iterates through each row in the minefield
    as Totoshka moves downwards. We will use left_totoshka and right_totoshka to flag if it is
    possible to move left or right from the current position. So, we will first have to check if
    Totoshka is not already in the leftmost column. If it is greater than 0, it shows that it is
    potentially possible to move left, but we will also have to check if the cell to the left is a
    safe spot. If it is, we will set left_totoshka to "True". Similarly, we will perform the safe
    action for the "right". If neither of the flags for left or right are set to "True", Totoshka
    will remain in the same position, and move directly below.
    As for Ally, her step is updated witha one step delay. This will ensure that Ally is always
    right behind Totoshka, and occupying the same column as Totoshka previous position. Ally's
    position will be updated after Totoshka has moved.

    Parameters: minefield, a 2D array of integers representing the minefield

    Return: A tuple of two lists, where the first list is Totoshka's path, and the second list is Ally's path

    Time Complexity:
    O(N * M) where N is the number of rows, and M is the number of columns in the minefield.

    Aux Space Complexity:
    O(N * M) where the worst case, Totoshka may have to traverse through the entire minefield
    */

    // containing two lists of tuples, where the first list is Totoshka's path, and the second list is Ally's path
    // accepting an array of arrays of integers representing the minefield
    static Tuple<List<Tuple<int, int>>, List<Tuple<int, int>>> traversing_minefield(int[][] minefield)
    {
        int row_nums = minefield.Length;
        int columns_num = minefield[0].Length;

        List<Tuple<int, int>> totoshka_path = new List<Tuple<int, int>>();  //creating a list tuples for Totoshka's path(row index, column index)
        List<Tuple<int, int>> ally_path = new List<Tuple<int, int>>();  // creating a list tuples for Ally's path(row index, column index)
        int column_totoshka = Array.FindIndex(minefield[0], item => item == 0);
        int? column_ally = null;    // Ally's initial position is initialized to null to have a one step delay

        for (int row = 0; row < row_nums; row++)
        {
            bool left_totoshka = false;
            bool right_totoshka = false;

            // Check if Totoshka is not in the leftmost column and the element to the left is a safe spot.
            if (column_totoshka > 0 && minefield[row][column_totoshka - 1] == 0)
            {
                left_totoshka = true;
            }

            // Check if Totoshka is not in the rightmost column and the element to the left is a safe spot.
            if (column_totoshka < columns_num - 1 && minefield[row][column_totoshka + 1] == 0)
            {
                right_totoshka = true;
            }

            if (left_totoshka)
            {
                column_totoshka--;
            }
            else if (right_totoshka)
            {
                column_totoshka++;
            }

            if (row > 0)
            {
                column_ally = totoshka_path[row - 1].Item2; // access the column position of Totoshka in the previous row
            }

            ally_path.Add(new Tuple<int, int>(row, column_ally ?? 0)); // Use ?? to handle null cases( ally's initial position)
            totoshka_path.Add(new Tuple<int, int>(row, column_totoshka));
        }

        return new Tuple<List<Tuple<int, int>>, List<Tuple<int, int>>>(totoshka_path, ally_path);
    }

    static void Main(string[] args)
    {
        int[][] minefield = new int[][]
        {
                                           // (0,0) <- Ally's path starts here
            new int[] {1, 1, 1, 0, 1, 1},  // (0,3) <- Totoshka's path starts here
            new int[] {1, 1, 0, 1, 1, 1},  // (1,2)
            new int[] {1, 0, 1, 1, 1, 1},  // (2,1)
            new int[] {1, 1, 0, 1, 1, 1},  // (3,2)
            new int[] {1, 1, 0, 1, 1, 1},  // (4,2)
            new int[] {1, 1, 1, 0, 1, 1},  // (5,3)
            new int[] {0, 0, 0, 0, 0, 0},  // (6,2)
            new int[] {0, 0, 0, 0, 0, 0}   // (7,1)
        };

        Tuple<List<Tuple<int, int>>, List<Tuple<int, int>>> paths = traversing_minefield(minefield);
        List<Tuple<int, int>> totoshka_path = paths.Item1;
        List<Tuple<int, int>> ally_path = paths.Item2;

        Console.WriteLine("Totoshka's Path:");
        foreach (var tuple in totoshka_path)
        {
            Console.WriteLine($"({tuple.Item1}, {tuple.Item2})");
        }

        Console.WriteLine("\nAlly's Path:");
        foreach (var tuple in ally_path)
        {
            Console.WriteLine($"({tuple.Item1}, {tuple.Item2})");
        }
    }
}
