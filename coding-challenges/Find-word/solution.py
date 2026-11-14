def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)
    
    # The four allowed directions: right, left, down, up
    directions = [
        (0, 1),   # left to right
        (0, -1),  # right to left
        (1, 0),   # top to bottom
        (-1, 0)   # bottom to top
    ]
    
    for r in range(rows):
        for c in range(cols):
            # Only check directions if the first letter matches
            if matrix[r][c] == word[0]:
                for dr, dc in directions:
                    # Calculate the potential end coordinates
                    end_r = r + dr * (word_len - 1)
                    end_c = c + dc * (word_len - 1)
                    
                    # Ensure the end coordinates stay inside the matrix bounds
                    if 0 <= end_r < rows and 0 <= end_c < cols:
                        # Check if all characters along this path match the word
                        if all(matrix[r + dr * i][c + dc * i] == word[i] for i in range(word_len)):
                            return [[r, c], [end_r, end_c]]
