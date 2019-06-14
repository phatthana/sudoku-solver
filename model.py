
class Sudoku():

    def __init__(self):
        self.table = self._init_table()

    def _init_table(self):
        # Test
        return [
            [None, 5, 3, None, 7, None, 4, None, 1],
            [None, 6, None, None, None, 5, 7, 8, 3],
            [None, 7, None, 4, None, 6, 2, None, 5],
            [None, None, None, 1, None, 4, 8, None, 9],
            [6, 2, None, None, None, 8, None, None, None],
            [None, None, 1, None, None, None, 6, None, None],
            [7, 1, None, None, None, 9, 5, None, None],
            [3, None, 5, None, 4, 7, None, 1, 2],
            [4, 9, None, None, None, None, 3, None, 8],
            
        ]
        _rows = []
        for i in range(9):
            _col = [None for j in range(9)]
            _rows.append(_col)
        return _rows

    def completed(self):
        for r in self.table:
            for val in r:
                if val is None:
                    return False
        return True

    def fill(self, val, i, j):
        print('fill {} in {}, {}'.format(val, i, j))
        self.table[i][j] = val

    def row(self, i):
        return self.table[i]

    def column(self, i):
        return [self.table[x][i] for x in range(9)]

    def sub_table(self, i, j):
        s_table = []
        s_i = 3 * i
        max_s_i = s_i+3
        for s_i in range(s_i, max_s_i):
            s_j = 3 * j
            max_s_j = s_j + 3
            s_table.append([self.table[s_i][s_j] for s_j in range(s_j, max_s_j)])
        # print(self._build_str_table(s_table))
        return s_table
    
    def __repr__(self):
        return self._build_str_table(self.table)

    def _build_str_table(self, table):
        l = len(table)
        result = ''
        for i in range(len(table)):
            r = table[i]
            row_str = ''
            for j in range(len(r)):
                c = r[j]
                if j == 0:
                    row_str += '| '
                row_str += self._val(c) + ' '
                if j%3 == 2:
                    row_str += '| '
            result += row_str
            result += '\n'
            if i%3 == 2:
                result += '-'* (l*2 + (int(l/3)+1)*2 - 1)
                result += '\n'
        return result

    def _val(self, val):
        if val == None:
            return '.'
        return str(val)