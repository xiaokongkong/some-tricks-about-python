def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while start * 2 < row and start * 2 < col:
        print_circle(matrix, start, rows, cols, ret)
        start += 1
    return ret


def print_circle(matrix, start, rows, cols, ret):
    row = rows - start - 1  # 最后一行
    col = cols - start - 1  # 最后一列
    # left -> right
    for c in range(start, col + 1):
        ret.append(matrix[start][c])
    # top -> bottom
    # 终止行号大于起始行号
    if start < row:
        for r in range(start + 1, row + 1):
            ret.append(matrix[r][col])
    # right -> left
    # 至少有两行两列
    # 终止行号大于起始行号，并且终止列号大于起始列号
    if start < row and start < col:
        for c in range(start, col)[::-1]:
            ret.append(matrix[row][c])
    # bottom -> top
    # 至少有三行两列
    # 终止行号至少比起始行号大2，并且终止列号大于起始列号
    if start < row - 1 and start < col:
        for r in range(start + 1, row)[::-1]:  #
            ret.append(matrix[r][start])


print(list(range(0,3)[::-1]))
print(list(range(1,1)[::-1]))
print(list(range(3,0,-1)))