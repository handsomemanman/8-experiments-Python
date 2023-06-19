# 编写函数，创建一个随机的 3 行 3 列的二位数组，输出每一行的最大值、每一列的最大值，以及整个数组的最大值。
import random as rd

rad = [[rd.randint(0, 1000) for i in range(3)] for j in range(3)]  # 列表推导式，随机二维列表
# 列
for c in range(3):
    print("第{}列最大值为：".format(c+1), end='')
    print(max([rad[i][c] for i in range(3)]))
# 行
for c in range(3):
    print("第{}行最大值为：".format(c + 1), end='')
    print(max([rad[c][i] for i in range(3)]))

print("矩阵中的最大值为：", max([rad[i][j] for i in range(3) for j in range(3)]))
