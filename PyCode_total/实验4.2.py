import os

# 判断是否存在
if not os.path.exists("d:/Xuan_python/学号.txt"):
    print("文件不存在哦")
else:
    # with open读取文件
    with open("d:/Xuan_python/学号.txt", "r") as f:
        # 统计行数 利用列表推导式
        num_lines = sum([1 for line in f])
        print("总行数:", num_lines)
        f.seek(0)  # 使得文件从开头开始读取 可有可无
        # 利用字典来统计字符数
        letter_count = {}
        for line in f:
            for letter in line:
                if letter.isalpha():
                    if letter in letter_count:

                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1

        print("字符统计如下:")
        for letter, count in letter_count.items():
            print(letter, count)
