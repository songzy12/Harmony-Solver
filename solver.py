from constant import sep1, sep2, sep3


def encode(grid):
    """list to str
    """
    row = len(grid)
    col = len(grid[0])

    res = ""
    for i in range(row):
        for j in range(col):
            item = grid[i][j]
            res += sep1.join(item)
            if j != col - 1:
                res += sep2
        if i != row - 1:
            res += sep3
    return res


def decode(grid):
    """str to list
    """
    res = []
    rows = grid.split(sep3)
    for row in rows:
        res_row = []
        cols = row.split(sep2)
        for col in cols:
            res_col = col.split(sep1)
            res_row.append(res_col)
        res.append(res_row)
    return res


def read(input_file):
    res = ""
    with open(input_file) as f:
        for line in f.readlines():
            if not line.strip():
                continue
            res += line.strip()
    return res


def check(grid):
    """str to False/True
    """
    grid = decode(grid)
    for i, row in enumerate(grid):
        for col in row:
            x, y = col
            if x != str(i) or y != '0':
                return False
    return True


def swap(grid, i0, j0, i1, j1):
    """list to str
    """
    if i0 == i1 and j1 == j0:
        return ""

    grid = decode(grid)
    x0, y0 = grid[i0][j0]
    x1, y1 = grid[i1][j1]

    if y0 == '0' or y1 == '0':
        return ""

    grid[i0][j0] = x1, str(int(y1)-1)
    grid[i1][j1] = x0, str(int(y0)-1)
    return encode(grid)


def pprint(grid):
    for row in grid.split(sep3):
        print(row)
    print()

# def bfs(grid):
#     """str
#     """
#     q = [[[grid], grid]]
#     visited = set(grid)
#     while q:
#         prev, cur = q.pop(0)
#         pprint(cur)
#         cur = decode(cur)
#         for i0 in range(len(cur)):
#             for j0 in range(len(cur[0])):
#                 for i1 in range(len(cur)):
#                     next_ = swap(encode(cur), i0, j0, i1, j0)
#                     if not next_:
#                         continue
#                     if next_ in visited:
#                         continue
#                     if check(next_):
#                         return prev
#                     q.append([prev + [encode(next_)], next_])
#                     visited.add(next_)

#                 for j1 in range(len(cur[0])):
#                     next_ = swap(encode(cur), i0, j0, i0, j1)
#                     if not next_:
#                         continue
#                     if next_ in visited:
#                         continue
#                     if check(next_):
#                         return prev
#                     q.append([prev + [encode(next_)], next_])
#                     visited.add(next_)


visited = set()


def dfs(grid):
    if check(grid):
        return True
    cur = decode(grid)
    for i0 in range(len(cur)):
        for j0 in range(len(cur[0])):
            for i1 in range(len(cur)):
                next_ = swap(encode(cur), i0, j0, i1, j0)
                if not next_:
                    continue
                if next_ in visited:
                    continue
                visited.add(next_)
                if dfs(next_):
                    pprint(next_)
                    return True

            for j1 in range(len(cur[0])):
                next_ = swap(encode(cur), i0, j0, i0, j1)
                if not next_:
                    continue
                if next_ in visited:
                    continue
                visited.add(next_)
                if dfs(next_):
                    pprint(next_)
                    return True
    return False


def solve(input_file):
    grid = read(input_file)
    visited.add(grid)
    dfs(grid)


if __name__ == "__main__":
    input_file = "input/grid_.txt"
    solve(input_file)
