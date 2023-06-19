import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('D:/86152/Pictures/Saved Pictures/1628993676227.jpg')
print(img.shape)
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))  # 画布大小


axs[0].imshow(r, cmap='nipy_spectral')  # 调用属性进行设置hot映射
axs[0].set_title('Red channel')
axs[1].imshow(g, cmap='nipy_spectral')
axs[1].set_title('Green channel')
axs[2].imshow(b, cmap='nipy_spectral')
axs[2].set_title('Blue channel')


plt.show()
