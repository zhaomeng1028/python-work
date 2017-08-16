import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import time

wrong_pic = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\wrong_pic.txt"
imdir = r"C:\zhaomeng\img_val"
count = 1
for line in open(wrong_pic,'r'):
    line = line.strip()
    pic_dir = imdir + '\\' + line
    pic = mpimg.imread(pic_dir)
    plt.imshow(pic) # 显示图片
    plt.axis('off') # 不显示坐标轴
    plt.title(str(count))
    count += 1
    plt.pause(3)
    plt.close()