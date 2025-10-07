import numpy as np


def AND(x1, x2):
    # 파라미터: 휴리스틱으로 결정
    w1, w2 = 0.5, 0.5
    theta  = 0.7
    # 가중치를 곱한 입력의 총합이 임곗값을 초과해야 출력 뉴런 활성화
    weighted_sum = w1*x1 + w2*x2
    return 1 if weighted_sum > theta else 0

def AND_bias(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    weighted_sum = np.sum(w * x) + b
    return 1 if weighted_sum > 0 else 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    weighted_sum = np.sum(w * x) + b
    return 1 if weighted_sum > 0 else 0 #라뷰

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.3, 0.3])
    b = -0.2
    weighted_sum = np.sum(w * x) + b
    return 1 if weighted_sum > 0 else 0

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y  = AND(s1, s2)
    return y


inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
truth_table = np.array(inputs)
header = np.array([["x1", "x2", "AND", "NAND", "OR", "XOR"]])

and_outputs = []
nand_outputs = []
or_outputs = []
xor_outputs = []
for row in inputs:
    x1, x2 = row
    and_outputs.append(AND_bias(x1, x2))
    nand_outputs.append(NAND(x1, x2))
    or_outputs.append(OR(x1, x2))
    xor_outputs.append(XOR(x1, x2))

truth_table = np.c_[truth_table, and_outputs, nand_outputs, or_outputs, xor_outputs]
truth_table = np.vstack([header, truth_table.astype(str)])

for row in truth_table:
    print(*row, sep='\t')