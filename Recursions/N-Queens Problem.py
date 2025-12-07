"""
Docstring for Recursions.N-Queens Problem

Conditions: 

1) Every Row Should have 1 Queen
2) Every Column should have 1 Queen 
3) None of the Queens should attack each other 


Lower Diagonal -> row + col 
Upper Diagonal -> (n-1) + (col-row)


"""       
        


n = int(input("Enter the Number N :"))

board = [[0 for _ in range(n)] for _ in range(n)]
status = [[0 for _ in range(n)] for _ in range(n)]


def fill_diagonal(row, col, status, update):
    n = len(status)

    r, c = row, col
    while r >= 0 and c >= 0:
        status[r][c] += update
        r -= 1; c -= 1

    r, c = row, col
    while r < n and c >= 0:
        status[r][c] += update
        r += 1; c -= 1

    r, c = row, col
    while r >= 0 and c < n:
        status[r][c] += update
        r -= 1; c += 1

    r, c = row, col
    while r < n and c < n:
        status[r][c] += update
        r += 1; c += 1


def fill(row, col, status, update):
    for i in range(len(status)):
        status[row][i] += update

    for i in range(len(status)):
        status[i][col] += update

    fill_diagonal(row, col, status, update)


def recursion(board, col, status, ans):
    if col == len(board):
        ans.append([row[:] for row in board])
        return

    for row in range(len(board)):
        if status[row][col] == 0: 
            board[row][col] = 1
            fill(row, col, status, +1)
            recursion(board, col + 1, status, ans)
            fill(row, col, status, -1)
            board[row][col] = 0


ans = []
recursion(board, 0, status, ans)
print(ans)

