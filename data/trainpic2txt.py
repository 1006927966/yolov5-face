import os
import shutil

# 这一部分只是让图像转化成txt 形式还需要增加一部转化成yolo形式的代码  trainpic2yolo.py

rootdir = "/Volumes/未命名/widerface/WIDER_train/images"
labeltxt = "/Volumes/未命名/widerface/train/label.txt"

savedir = "/Volumes/未命名/widerface/facetrain/train/images"
os.makedirs(savedir, exist_ok=True)
labeldir = "/Volumes/未命名/widerface/facetrain/train/labels"
os.makedirs(labeldir, exist_ok=True)

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
            labeltxt = os.path.join(labeldir, "{}.txt".format(count))
            tag = True
        else:
            tag = False
            continue
    else:
        if tag:
            line = line.strip().split()
            label = [float(fac) for fac in line ]
            newline = ""
            newline += "{}".format(label[0])  # x1
            newline += ",{}".format(label[1])  # y1
            newline += ",{}".format(label[0] + label[2])  # x2
            newline += ",{}".format(label[1] + label[3])  # y2

            # landmarks
            newline += ",{}".format(label[4])  # l0_x
            newline += ",{}".format(label[5])  # l0_y
            newline += ",{}".format(label[7])  # l1_x
            newline += ",{}".format(label[8])  # l1_y
            newline += ",{}".format(label[10])  # l2_x
            newline += ",{}".format(label[11])  # l2_y
            newline += ",{}".format(label[13])  # l3_x
            newline += ",{}".format(label[14])  # l3_y
            newline += ",{}".format(label[16])  # l4_x
            newline += ",{}".format(label[17])  # l4_y
            if label[4] < 0:  # 标注是否可见
                newline += ",{}".format(-1)
            else:
                newline += ",{}".format(1)
            newline += "\n"
            with open(labeltxt, "a") as f1:
                f1.write(newline)
        else:
            continue








