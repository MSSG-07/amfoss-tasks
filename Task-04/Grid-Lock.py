def can_place_horizontally(grid, word, row, col):
    if col + len(word) > 10:
        return False
    for i in range(len(word)):
        if grid[row][col + i] not in ['-', word[i]]:
            return False
    return True

def place_horizontally(grid, word, row, col):
    for i in range(len(word)):
        grid[row][col + i] = word[i]

def remove_horizontally(grid, word, row, col):
    for i in range(len(word)):
        grid[row][col + i] = '-'

def can_place_vertically(grid, word, row, col):
    if row + len(word) > 10:
        return False
    for i in range(len(word)):
        if grid[row + i][col] not in ['-', word[i]]:
            return False
    return True

def place_vertically(grid, word, row, col):
    for i in range(len(word)):
        grid[row + i][col] = word[i]

def remove_vertically(grid, word, row, col):
    for i in range(len(word)):
        grid[row + i][col] = '-'

def solve_crossword(grid, words, index):
    if index == len(words):
        return True
    word = words[index]
    for row in range(10):
        for col in range(10):
            if can_place_horizontally(grid, word, row, col):
                place_horizontally(grid, word, row, col)
                if solve_crossword(grid, words, index + 1):
                    return True
                remove_horizontally(grid, word, row, col)
            if can_place_vertically(grid, word, row, col):
                place_vertically(grid, word, row, col)
                if solve_crossword(grid, words, index + 1):
                    return True
                remove_vertically(grid, word, row, col)
    return False

def crossword_puzzle(grid, words):
    words = words.split(';')
    grid = [list(row) for row in grid]
    solve_crossword(grid, words, 0)
    return [''.join(row) for row in grid]

grid = [input().strip() for _ in range(10)]
words = input().strip()
result = crossword_puzzle(grid, words)
for row in result:
    print(row)
