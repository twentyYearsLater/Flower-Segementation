# # 图片二值化
# from PIL import Image
#
# img = Image.open('C:\\Users\\tzbz_\\Documents\\毕设\\花朵分割系统数据\\segmim\\segmim_00002.jpg')
#
# # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')
# #Img.save("test1.jpg")
#
# # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
# threshold = 200
#
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# # 图片二值化
# photo = Img.point(table, '1')
# #photo.save("test2.jpg")
# img.show()




#rgb图#
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def rgb2gray(rgb):
    return np.dot(rgb[..., : 3], [0.299, 0.587, 0.114])

img = np.array(Image.open('C:\\Users\\tzbz_\\Documents\\毕设\\花朵分割系统数据\\segmim\\segmim_00002.jpg'))#C:\\Users\\tzbz_\\Documents\\毕设\\花朵分割系统数据\\segmim\\segmim_00002.jpg#C:\\Users\\tzbz_\Documents\Pytorch\Data\\train\masks\\2.png
img = rgb2gray(img)
print(img.shape)
print(img.dtype)
print(img.size)
print(type(img))


rows,cols=img.shape
#for i in range(rows):
for i in range(rows):
    for j in range(cols):
        if (img[i,j] == 28.956):
            img[i,j]=0
        else:
            img[i,j]=1

plt.figure("love")
plt.imshow(img)
plt.axis('off')
plt.savefig('C:\\Users\\tzbz_\Documents\Pytorch\Data\\train\masks\\3.png')
plt.show()





#原图+mask进行分割#

#coding:utf-8
# import os
# import cv2
# import numpy as np
#
#
# def add_mask2image_binary(images_path, masks_path, masked_path):
#     # Add binary masks to images
#     for img_item in os.listdir(images_path):
#         print(img_item)
#         img_path = os.path.join(images_path, img_item)
#         img = cv2.imread(img_path)
#         mask_path = os.path.join(masks_path, img_item[:-4] + '.png')  # mask是.png格式的，image是.jpg格式的
#         mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)  # 将彩色mask以二值图像形式读取
#         masked = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)  # 将image的相素值和mask像素值相加得到结果
#         cv2.imwrite(os.path.join(masked_path, img_item), masked)
#
#
# images_path = 'C:/Users/tzbz_/Documents/image'
# masks_path = 'C:/Users/tzbz_/Documents/mask'
# masked_path = 'C:/Users/tzbz_/Documents/masked'
# add_mask2image_binary(images_path, masks_path, masked_path)