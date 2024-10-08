'''
2차원 행렬을 90도(시계방향)으로 회전하는 함수
input: original matrix a
output: new matrix new_a
'''
def rotate_a_matrix_by_90degree(a):
    row_len = len(a)
    col_len = len(a[0])

    new_a = [[0]*row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            new_a[c][row_len - r - 1] = a[r][c]

    return new_a
            
