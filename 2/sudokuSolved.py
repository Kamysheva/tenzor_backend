def find_empty(board): # функция для поиска очередной пустой ячейки
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # проверяем, есть ли num в данной строке
    if num in board[pos[0]]:
        return False
    # проверяем, есть ли num в данном столбце
    if num in [board[i][pos[1]] for i in range(9)]:
        return False
    # Проверка квадратной области 3x3
    x, y = 3 * (pos[0] // 3), 3 * (pos[1] // 3) # ищем верхний левый угол квадрата
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty(board) # ищем очередную пустую ячейку
    if not empty:
        return True
    row, col = empty
    for i in range(1, 10): # пробуем подставлять числа в ячейку
        if is_valid(board, i, (row, col)): # если такого числа нет в row, col и квадратной области вокруг, то
            board[row][col] = i # присваеваем ячейке значение
            if solve_sudoku(board): # запускаем функцию рекурсивно, чтобы она решила судоку с данным числом
                return True
            board[row][col] = 0 # если функция не решила судоку, ячейка обнуляется
    return False


sudoku_input = open('input.txt', 'r')
sudoku = []

for line in sudoku_input:
    sudoku.append([int(num) for num in line.split()])

if solve_sudoku(sudoku):
    with open("output.txt", "w") as file:
        for line in sudoku:
            for num in line:
                file.write(str(num) + ' ')
            file.write('\n')
else:
    print('Impossible')

