import os
import cv2
picdir = "/Volumes/未命名/widerface/facetrain/train/images"
labeldir = "/Volumes/未命名/widerface/facetrain/train/mlabels"
savedir = "/Volumes/未命名/widerface/facetrain/train/labels"
os.makedirs(savedir, exist_ok=True)

picnames = os.listdir(picdir)

for picname in picnames:
    tag = False
    if "jpg" not in picname:
        continue
    picpath = os.path.join(picdir, picname)
    img = cv2.imread(picpath)
    height,width = img.shape[:2]
    labelname = picname.replace("jpg", "txt")
    labelpath = os.path.join(labeldir, labelname)
    savelabel = os.path.join(savedir, labelname)
    with open(labelpath, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            label = [float(fac) for fac in line.split(",")]
            if label[-1] <0:
                continue
            tag = True
            newline = "0"
            label[0] = max(0, label[0])
            label[1] = max(0, label[1])
            label[2] = min(width - 1, label[2])
            label[3] = min(height - 1, label[3])
            newline+=" {}".format(((label[0] + label[2])/2) / width)  # cx
            newline +=" {}".format( ((label[1] + label[3])/2) / height)  # cy
            newline +=" {}".format( (label[2]-label[0]) / width)  # w
            newline +=" {}".format( (label[3]-label[1]) / height)  # h

            # landmarks
            newline +=" {}".format( label[4] / width)  # l0_x
            newline +=" {}".format( label[5] / height)  # l0_y
            newline +=" {}".format( label[6] / width)  # l1_x
            newline +=" {}".format( label[7] / height)  # l1_y
            newline +=" {}".format( label[8] / width)  # l2_x
            newline +=" {}".format( label[9] / height)  # l2_y
            newline += " {}".format(label[10] / width)  # l3_x
            newline +=" {}".format( label[11] / height)  # l3_y
            newline +=" {}".format( label[12] / width)  # l4_x
            newline +=" {}".format( label[13] / height)  # l4_y
            newline += "\n"
            with open(savelabel, "a") as f2:
                f2.write(newline)
        if not tag:
            print(picpath)
            os.remove(picpath)


