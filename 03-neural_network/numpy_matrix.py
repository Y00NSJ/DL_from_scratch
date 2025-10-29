import numpy as np


A = np.array([1, 2, 3, 4])
print(f"행렬 A: {A}")
print(f"행렬 A의 차원: {np.ndim(A)}")
print(f"행렬 A의 형상: {np.shape(A)}")
print("\t1차원 배열도 다차원 배열과 출력 형태를 통일시키기 위해 (1,) 과 같은 형태로 출력")

# 행렬곱
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f"A * B = f{np.dot(A, B)}")
