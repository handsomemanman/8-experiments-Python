Dec_int = int(input("输入一个十进制数："))
B4 = Dec_int
O4 = Dec_int
H4 = Dec_int
Hlist = ['A', 'B', 'C', 'D', 'E', 'F']
Hstr = ""
Bstr = ""
Ostr = ""
while B4 > 0:
    Bt = B4 % 2
    Bstr = str(Bt) + Bstr
    B4 //= 2
while O4 > 0:
    Ot = O4 % 8
    Ostr = str(Ot) + Ostr
    O4 //= 8
while H4 > 0:
    Ht = H4 % 16
    print(Ht / 10)
    if Ht > 9:
        Hstr = Hlist[int(Ht % 10)] + Hstr
    else:
        Hstr += str(Ht)
    H4 //= 16
print("二进制：  ", Bstr, end=" ")
print("二进制：  ", bin(Dec_int))
print("八进制：  ", Ostr, end=" ")
print("八进制：  ", oct(Dec_int))
print("十六进制：", Hstr, end=" ")
print("十六进制：", hex(Dec_int))
