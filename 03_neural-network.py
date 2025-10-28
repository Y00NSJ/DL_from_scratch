## 계단 함수 구현
def step_function(x):
    return 1 if x > 0 else 0
# numpy 배열에 대응하도록 수정
def step_function_numpy(x):
    y = x > 0               # 입력 numpy 배열의 각 원소에 대해 Bool 값 대응
    return y.astype(int)    # Bool -> Int로 변환된 numpy 배열로 변환
# 도식화
import numpy as np
import matplotlib.pylab as plt


def step_function_plt(x):
    return np.array(x > 0, dtype=int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function_plt(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()