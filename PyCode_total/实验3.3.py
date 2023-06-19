import numpy as np

# 创建符合条件的随机矩阵
A = np.random.randint(0, 10, size=(5, 3))
B = np.random.randint(0, 6, size=(3, 2))

# 计算-利用numpy库中的dot函数运算
C = np.dot(A, B)

print("矩阵 A:\n", A)
print("矩阵 B:\n", B)
print("相乘之后矩阵 C:\n", C)