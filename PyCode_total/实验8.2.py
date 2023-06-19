import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io, restoration

# 读取有噪声的图片
noisy_img = io.imread("D:/86152/Pictures/noisy_jay.png")
print(noisy_img.ndim)
# 去噪
de_noised_img = restoration.denoise_wavelet(noisy_img, channel_axis=True)

# 展示图片
plt.imshow(de_noised_img)
plt.show()

mpimg.imsave("D:/86152/Pictures/de_noisy_jay.jpg", de_noised_img)
