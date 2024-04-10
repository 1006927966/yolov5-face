import os
import cv2
os.system("CUDA_VISIBLE_DEVICES='0' python3 train.py --data data/widerface.yaml --cfg models/yolov5s.yaml")

# img = cv2.imread("/code/wujilong/code/yolov5-face/data/widerface/facetrain/train/images/10000.jpg")
# txtpath = "/code/wujilong/code/yolov5-face/data/widerface/facetrain/train/labels/10000.txt"
# draws = "/code/wujilong/code/yolov5-face/data/widerface/c.jpg"
# h,w = img.shape[:2]
#
# with open(txtpath, "r") as f:
#     line = f.readline()
#
# corrds = [float(fac) for fac in line.split()]
#
# centerx = int(corrds[1]*w )
# centery = int(corrds[2]*h )
#
# gw = int(w*corrds[3])
# gh = int(h*corrds[4])


# x1 = int(centerx - gw/2)
# y1 = int(centery - gh/2)
#
# x2 = int(centerx + gw/2)
# y2 = int(centery + gh/2)
#
#
# img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
# cv2.imwrite(draws, img)




