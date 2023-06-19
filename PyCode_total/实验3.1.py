def Hanoi(a):
    if a == 1:
        return 1
    else:
        return Hanoi(a - 1) + 1 + Hanoi(a - 1)


print(Hanoi(3))
