import glob
import os
import sys
from PIL import Image

def ImgSplit(im, row, column):
    width = im.size[0]/column
    height = im.size[1]/row

    buff = []
    for h1 in range(row):
        for w1 in range(column):
            w2 = w1 * width
            h2 = h1 * height
            print(w2, h2, width + w2, height + h2)
            c = im.crop((w2, h2, width + w2, height + h2))
            buff.append(c)
    return buff

### 設定
img_dir = sys.argv[1]  # 入力
row, column = int(sys.argv[2]), int(sys.argv[3])
types = ['*.png', '*.jpg', '*.jpeg', '*.bmp']
paths = []

if os.path.isdir(img_dir):
    for t in types:
        paths.extend(glob.glob(os.path.join(img_dir, t)))
else:
    paths.append(img_dir)

for p in paths:
    im = Image.open(p)  # 読み込む。
    for id, ig in enumerate(ImgSplit(im, row, column)):
        if os.path.isdir(img_dir):
            ig.save(os.path.join(img_dir, os.path.splitext(os.path.basename(p))[0]) + "_" + str(id+1) + ".png", "PNG")
        else:
            ig.save(os.path.splitext(os.path.basename(img_dir))[0] + "_" + str(id+1) + ".png", "PNG")