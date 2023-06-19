import pandas as pd

df = pd.read_excel("d:/Xuan_python/score.xlsx")
# print(df)

# 计算每个人的平均成绩
df["平均成绩"] = ((df["笔试"] + df["平时"] + df["实验"]) / 3).__round__(2)

print(df)
# 每科的平均成绩
# df.loc["平均成绩"] = df.mean()
subjects_average = {"笔试": df["笔试"].mean(0).__round__(2),
                    "平时": df["平时"].mean(0).__round__(2),
                    "实验": df["实验"].mean(0).__round__(2),
                    "平均成绩": df["平均成绩"].mean(0).__round__(2)}
df = df.append(subjects_average, ignore_index=True)

df.to_excel("d:/Xuan_python/scoreResult.xlsx", index=False)
