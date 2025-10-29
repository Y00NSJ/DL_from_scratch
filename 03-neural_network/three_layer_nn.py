import numpy as np
from activate_functions import sigmoid


## 3층 신경망 구현(임의 값)
# 1층: 입력층 뉴런 2개, 편향 1개 => 1번 은닉층 뉴런 3개
X = np.array([1.0, 0.5])
W1 = np.array([0.1, 0.3, 0.5], [0.2, 0.4, 0.6])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(f"1층 뉴런의 출력 신호: {A1}")
print(f"1층 뉴런 출력 신호의 활성함수 적용 결과: {Z1}")

# 2층: 1번 은닉층 뉴런 3개, 편향 1개 => 2번 은닉층 뉴런 2개
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

# 출력층: 2번 은닉층 뉴런 2개, 편향 1개 => 출력층 뉴런 2개
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
# 활성 함수로 항등 함수 사용; 보통 회귀 문제에서 사용
def identity_function(x):
    return x

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)