from PIL import Image
import matplotlib.image as mpimg

# 读取图片
img = Image.open("D:/86152/Pictures/Saved Pictures/lazy_jay.jpeg")

# 直接翻转成灰度图片
gray_img = img.convert("L")

gray_img.show()

# # 保存图片的操作
# mpimg.imsave("D:/86152/Pictures/Saved Pictures/lazy_jay_gray.png", gray_img, cmap='gray')
