import time
import random

def generate_matrix(n):
    # Tạo ma trận vuông kích thước n x n
    return [[random.randint(1, n * 2) for _ in range(n)] for _ in range(n)]

def multiply_matrices(A, B):
    # Nhân 2 ma trận cùng kích thước
    n = len(A)
    
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def print_spiral(matrix):

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Đi từ trái sang phải
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Đi từ trên xuống dưới
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Đi từ phải sang trái
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1 

        if left <= right:
            # Đi từ dưới lên trên
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1 

    print(result)

def main():
    sizes = [10, 20, 30, 40, 50]
    for n in sizes:
        A = generate_matrix(n)
        B = generate_matrix(n)

        # Bắt đầu đo
        time_s = time.time()
        C = multiply_matrices(A, B)
        time_e = time.time()
        delta = (time_e - time_s) * 1000

        print("Ma trận C:")
        for row in C:
            print(row)
        print(f"Kích thước ma trận: {n}x{n}, Thời gian nhân ma trận: {delta:.5f} ms")

        print("Duyệt ma trận C theo hình xoắn ốc:")
        print_spiral(C)
        
        


if __name__ == "__main__":
    main()