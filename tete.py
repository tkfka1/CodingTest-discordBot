m,n = map(int, input().split())

dic = {}

def add_lists(list1, list2):
    # 결과 리스트의 길이는 두 리스트 중 더 긴 길이로 설정
    max_length = max(len(list1), len(list2))
    result = []

    for i in range(max_length):
        # 각 리스트의 현재 위치에 원소가 있는지 확인
        if i < len(list1):
            val1 = list1[i]
        else:
            val1 = 0

        if i < len(list2):
            val2 = list2[i]
        else:
            val2 = 0

        # 두 원소의 합을 결과 리스트에 추가
        result.append(val1 + val2)

    return result

for i in range(m):
    temp = list(map(int,input().split()))
    dic[i] = temp

for i in range(n):
    print()
    temp = list(map(int,input().split()))
    if dic.get(i):
       dic[i] = add_lists(temp,dic[i])
    else:
       dic[i] = temp
        
for i in dic:
   print(' '.join(dic[i]))



def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix

def add_matrices(matrix1, matrix2):
    max_rows = max(len(matrix1), len(matrix2))
    max_cols = max(max(len(row) for row in matrix1), max(len(row) for row in matrix2))

    result = [[0 for _ in range(max_cols)] for _ in range(max_rows)]

    for i in range(max_rows):
        for j in range(max_cols):
            val1 = matrix1[i][j] if i < len(matrix1) and j < len(matrix1[i]) else 0
            val2 = matrix2[i][j] if i < len(matrix2) and j < len(matrix2[i]) else 0
            result[i][j] = val1 + val2

    return result

m, n = map(int, input().split())
matrix1 = read_matrix(m)
matrix2 = read_matrix(n)

result = add_matrices(matrix1, matrix2)
for row in result:
    print(row)
