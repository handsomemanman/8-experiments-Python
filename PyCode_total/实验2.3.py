# 编写程序，使用递归法求幂集。


def power_set(a):
    if a == 1:
        return [[1]]

    total = power_set(a - 1).copy()
    power_temp = total.copy()
    for i in range(len(power_temp)):
        power_temp[i].append(a)
    power_temp.append([a])
    return total + power_temp


print(power_set(4))
