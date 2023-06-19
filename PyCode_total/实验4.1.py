import os
import random

# 如果该目录不存在则创建该目录
if not os.path.exists("d:/Xuan_python"):
    os.makedirs("d:/Xuan_python")

# 随机的行以及随机字符数
num_lines = random.randint(10, 20)
num_chars = [random.randint(10, 30) for _ in range(num_lines)]

# 开始创建随机学号
chars = [chr(random.randint(65, 90)) for _ in range(26)]

# create and write to file
with open("d:/Xuan_python/学号.txt", "w") as f:
    for i in range(num_lines):
        line = "".join([random.choice(chars) for _ in range(num_chars[i])])
        f.write(line + "\n")