A=["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]

dot = "."
flag = 0
for i in range(9):
    row = []
    column = []
    box = []
    for j in range(9):
        value = A[i][j]
        if value != dot:
            if value in row:
                flag = flag + 1
                print('0')
            else:
                row.append(value)

        value = A[j][i]
        if value != dot:
            if value in column:
                flag = flag + 1
                print('0')
            else:
                column.append(value)

        value = A[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
        if value != dot:
            if value in box:
                flag = flag + 1
                print('0')
            else:
                box.append(value)

if flag == 0:                    
    print('1')
