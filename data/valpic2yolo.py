import os
import shutil
import cv2
import numpy as np

# 这里的验证集合是经过放缩后的
rootdir = "/Volumes/未命名/widerface/WIDER_val/images"
labeltxt = "/Volumes/未命名/widerface/val/label.txt"

savedir = "/Volumes/未命名/widerface/faceval/val/images"
os.makedirs(savedir, exist_ok=True)
labeldir = "/Volumes/未命名/widerface/faceval/val/labels"
os.makedirs(labeldir, exist_ok=True)


def xywh2xxyy(box):
    x1 = box[0]
    y1 = box[1]
    x2 = box[0] + box[2]
    y2 = box[1] + box[3]
    return x1, x2, y1, y2

# xywh 都基于图像宽高归一化
def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


tag = False
headdic = {}
count = 0
with open(labeltxt, "r") as f:
    lines = f.readlines()
for line in lines:
    if "#" in line:
        picname = line.strip()[2:]
        picpath = os.path.join(rootdir, picname)
        if os.path.exists(picpath):
            count += 1
            dstpath = os.path.join(savedir, "{}.jpg".format(count))
            shutil.copy(picpath, dstpath)
            img = cv2.imread(picpath)
            height, width, _ = img.shape
            labeltxt = os.path.join(labeldir, "{}.txt".format(count))
            tag = True
        else:
            tag = False
            continue
    else:
        if tag:
            line = line.strip()
            box = np.array(line.split()[0:4], dtype=np.float32)  # (x1,y1,w,h)
            box = convert((width, height), xywh2xxyy(box))
            label = '0 {} {} {} {} -1 -1 -1 -1 -1 -1 -1 -1 -1 -1\n'.format(round(box[0], 4), round(box[1], 4),
                                                                         round(box[2], 4), round(box[3], 4))
            with open(labeltxt, "a") as f1:
                f1.write(label)

        else:
            continue








