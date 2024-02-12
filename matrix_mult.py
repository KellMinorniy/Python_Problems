def matrix_multiply(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def input_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    n = int(input())
    A = input_matrix(n)
    B = input_matrix(n)
    result = matrix_multiply(A, B)
    for row in result:
        print(' '.join(str(x) for x in row))

if __name__ == "__main__":
    main()