import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.util import random_noise

img = mpimg.imread("D:/86152/Pictures/jay.png")

# 加入随机高斯噪声
noisy_img = random_noise(img, mode="gaussian")

plt.imshow(noisy_img)
plt.show()

# 保存文件
mpimg.imsave("D:/86152/Pictures/noisy_jay.png", noisy_img)
