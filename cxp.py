import cv2

img = cv2.imread("/code/wujilong/code/yolov5-face/data/widerface/facetrain/train/images/793.jpg")
h, w = img.shape[:2]
print(h,w)