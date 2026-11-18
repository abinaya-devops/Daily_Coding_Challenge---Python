
def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [
        (0, 1),   # Left to right
        (0, -1),  # Right to left
        (1, 0),   # Top to bottom
        (-1, 0)   # Bottom to top
    ]

    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] == word[0]:

                for row_dir, col_dir in directions:
                    end_row = row + (len(word) - 1) * row_dir
                    end_col = col + (len(word) - 1) * col_dir

                    if 0 <= end_row < rows and 0 <= end_col < cols:

                        found = True

                        for i in range(len(word)):
                            new_row = row + i * row_dir
                            new_col = col + i * col_dir

                            if matrix[new_row][new_col] != word[i]:
                                found = False
                                break

                        if found:
                            return [[row, col], [end_row, end_col]]
                          
