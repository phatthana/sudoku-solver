from model import Sudoku
from solver import solve
from time import sleep

sudoku = Sudoku()
print(sudoku)

# solve(sudoku, 0, 0 )
# sudoku.sub_table(1, 0)

def loop():
    for i, r in enumerate(sudoku.table):
        for j, val in enumerate(r):
            if val is None:
                posible_set = solve(sudoku, i, j)
                # print('solving in {}, {} | {}'.format(i, j, posible_set))
                if len(posible_set) == 1:
                    sudoku.fill(list(posible_set)[0], i, j)
                    

while not sudoku.completed():
    loop()
    # sleep(1)
    print(sudoku)
print('complete!!')
print(sudoku)
