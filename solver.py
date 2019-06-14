
FULL_SET = set(range(1, 10))

def solve(sudoku, i, j):
    posible_set = FULL_SET
    s_i = int(i/3)
    s_j = int(j/3)
    # print('sub table', s_i, s_j)
    sub = sudoku.sub_table(s_i, s_j)
    curr_set = set(filter(lambda v: v is not None, _normalize(sub)))
    # print('current', curr_set)
    posible_set = FULL_SET - curr_set
    # print('posible:', posible_set)
    if len(posible_set) == 1:
        return posible_set
    # print(sudoku.row(i))
    # print(sudoku.column(j))
    not_posible_set = set()
    for p in posible_set:
        if not posible(sudoku, p, i, j):
            not_posible_set.add(p)
    posible_set = posible_set - not_posible_set
    return posible_set

        
def posible(sudoku, val, i, j):
    s_row = sudoku.row(i)
    s_column = sudoku.column(j)
    
    if (val in s_row) or (val in s_column):
        return False
    return True

def _normalize(table):
    result = []
    for r in table:
        for v in r:
            result.append(v)
    return result
    
    