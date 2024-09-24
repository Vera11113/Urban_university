def get_matrix(n, m, value):

    mat = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(value)

        mat.append(temp)
    return mat

res1 = get_matrix(2, 2, 10)
print(res1)
res2 = get_matrix(3, 5, 42)
print(res2)
res3 = get_matrix(4, 2, 13)
print(res3)