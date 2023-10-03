def traversing_minefield(minefield):
    """
    Approach Description: The number of rows and columns in the minefield are determined.
    In the minefield:
    Bombs are represented as : "1"
    Safe Spots are represented as: "0"
    We start off by creating two empty lists to store the paths for Totoshka and Ally.
    Then we will find the first index where Totoshka can start by looking for the first "0"
    in the first row. Since Ally is following Totoshka, we will initialize Ally's position
    to "None" to have it as a one step delay. The loop iterates through each row in the
    minefield as Totoshka moves downwards. We will use left_totoshka and right_totoshka to flag
    if it is possible to move left or right from the current position. So, we will first have
    to check if Totoshka is not already in the leftmost column. If it is greater than 0, it shows
    that it is potentially possible to move left, but we will also have to check if the cell
    to the left is a safe spot. If it is, we will set left_totoshka to "True". Similarly, we will
    perform the safe action for the "right". If neither of the flags for left or right are set to
    "True", Totoshka will remain in the same position, and move directly below.
    As for Ally, her step is updated witha one step delay. This will ensure that Ally is always
    right behind Totoshka, and occupying the same column as Totoshka previous position. Ally's
    position will be updated after Totoshka has moved.

    Parameters:
    minefield (list): A 2D list representing the minefield

    Returns:
    totoshka_path (list): A list containing the path for Totoshka
    ally_path (list): A list containing the path for Ally

    Time Complexity:
    O(N * M) where N is the number of rows and M is the number of columns in the minefield

    Aux Space Complexity:
    O(N * M) where the worst case, Totoshka may have to traverse through the entire minefield
    """
    row_nums = len(minefield)
    column_nums = len(minefield[0])

    totoshka_path = []
    ally_path = []
    column_totoshka = minefield[0].index(0) # Find the index of the first safe spot for Totoshka
    column_ally = None # Initialize Ally's position with a one-step delay

    for row in range(row_nums):
        left_totoshka = False
        right_totoshka = False

        # Check if there is a column to the left of the current element
        # and if the value of that element is less than the value of the current element.
        if column_totoshka > 0 and minefield[row][column_totoshka - 1] == 0:
            left_totoshka = True

        # Check if there is a column to the right of the current element
        if column_totoshka < column_nums - 1 and minefield[row][column_totoshka + 1] == 0:
            right_totoshka = True

        # Determine Totoshka's new position based on available safe spots
        if left_totoshka:
            column_totoshka -= 1
        elif right_totoshka:
            column_totoshka += 1

        # Update Ally's position with a one-step delay
        if row > 0:
            column_ally = totoshka_path[row - 1][1]

        totoshka_path.append((row, column_totoshka))
        ally_path.append((row, column_ally))

    return totoshka_path, ally_path

minefield = [
                        # (0, None) for Ally
    [1, 1, 1, 0, 1, 1], # (0, 3) # Totoshka starts here right away
    [1, 1, 0, 1, 1, 1], # (1, 2)
    [1, 0, 1, 1, 1, 1], # (2, 1)
    [1, 1, 0, 1, 1, 1], # (3, 2)
    [1, 1, 0, 1, 1, 1], # (4, 2)
    [1, 1, 1, 0, 1, 1], # (5, 3)
    [0, 0, 0, 0, 0, 0], # (6, 2)
    [0, 0, 0, 0, 0, 0]  # (7, 1)
]

path_totoshka, path_ally = traversing_minefield(minefield)
print("Totoshka's Path:", path_totoshka)
print("Ally's Path:", path_ally)
