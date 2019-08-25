import sys

import cv2
import numpy as np


IMAGE_WHITELIST = [
    'ras',
    'sr',
    'tiff',
    'webp',
    'pgm',
    'jp2',
    'pbm',
    'dib',
    'bmp',
    'ppm',
    'png',
    'jpe',
    'jpeg',
    'jpg',
    'tif']

VIDEO_WHITELIST = ['mp4', 'avi', 'mkv', 'swf', 'webm', 'mjpeg']


def gaussianblur__transform(im, blur_w, blur_h, blur_r):
    blur_w = 1 + 2 * blur_w
    blur_h = 1 + 2 * blur_h

    return cv2.GaussianBlur(im, (blur_w, blur_h), blur_r)


def thresholding__transform(
        im, thresholdMode, threshold, maxvalue, combinedWithOTSU):
    imgray = im.copy()
    if im.ndim > 2:
        imgray = cv2.cvtColor(imgray, cv2.COLOR_BGR2GRAY)

    thresholdMode = getattr(cv2, thresholdMode)
    if combinedWithOTSU:
        thresholdMode |= cv2.THRESH_OTSU

    ret, imbin = cv2.threshold(imgray, threshold, maxvalue, thresholdMode)
    return imbin


def mser__transform(im, minArea, maxArea, max_variation, min_diversity,
                    max_evolution, area_threshold, min_margin, blur_size, source):
    copiedim = im.copy()
    img2     = im.copy()

    imsize = im.shape[0] * im.shape[1]

    blur_size = 1 + 2 * blur_size

    minArea = (float(minArea) / 100.0) * float(imsize)
    maxArea = (float(maxArea) / 100.0) * float(imsize)

    mser = cv2.MSER_create(_delta=1,
                           _min_area=int(minArea),
                           _max_area=int(maxArea),
                           _max_variation=max_variation,
                           _min_diversity=min_diversity,
                           _max_evolution=max_evolution,
                           _area_threshold=area_threshold,
                           _min_margin=0.003,
                           _edge_blur_size=blur_size
                           )

    regions = None
    bboxes = None

    try:
        (_, bboxes) = mser.detectRegions(copiedim)
    except:
        regions = mser.detectRegions(copiedim, None)
        regions = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

    if copiedim.ndim == 2:
        copiedim = cv2.cvtColor(copiedim, cv2.COLOR_GRAY2BGR)
        img2     = copiedim.copy()

    boxX = 0
    if bboxes is not None:
        for bb in bboxes:
            x, y, w, h = bb
            print "Imagem Num.: ", boxX
            cv2.rectangle(copiedim, (x, y), (x + w, y + h), (0, 255, 0), 2)
            prop = float(h/w) #isso se nao soubesse que eh 2, porque eh apenas um teste
            print "altura/base: ",  prop
            print("W: ",w,"H: ",h)
            area = source[y:y+h,x:x+w]
            target_area = copiedim[y:y+h,x:x+w]

            MINI = np.array([0,0,0],np.uint8)
            MAXI = np.array([0,0,0],np.uint8)
            dst = cv2.inRange(target_area,MINI,MAXI)
            if not prop == 0:
                nonZero = cv2.countNonZero(dst)/prop
                print "black prop: ", nonZero
            else:
                print "black prop: 0"
            if nonZero > 100 and nonZero < 290 and prop == 2.0:
                namef = str(boxX) + ".jpg"
                cv2.imwrite(namef,area) 
                boxX = boxX + 1
            print "------------------------------"

    if regions is not None:
        cv2.polylines(copiedim, regions, 1, (0, 255, 0))

    return copiedim


def apply_transformations(output):
    src    = output.copy()
    output = gaussianblur__transform(output, blur_w=1, blur_h=2, blur_r=1)
    output = thresholding__transform(
        output,
        thresholdMode='THRESH_BINARY',
        threshold=195,
        maxvalue=255,
        combinedWithOTSU=False)
    output = mser__transform(
        output,
        minArea=0.07,
        maxArea=0.108,
        max_variation=0.02,
        min_diversity=0.0,
        max_evolution=132,
        area_threshold=1.1,
        min_margin=0.001,
        blur_size=0,
        source = src)
    return output


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Ingresa una imagen!")
        sys.exit(1)

    in_im = sys.argv[1]

    if len(sys.argv) == 3:
        out_im_path = sys.argv[2]
    else:
        im_name, im_filetype = in_im.rsplit(".", 1)
        out_im_path = im_name + "-out." + im_filetype
    print "Imagen guardada en: "+out_im_path
    if im_filetype in IMAGE_WHITELIST:
        im = cv2.imread(in_im)
        out_im = apply_transformations(im)
        cv2.imwrite(out_im_path, out_im)

    elif im_filetype in VIDEO_WHITELIST:
        cap = cv2.VideoCapture(in_im)
        if not cap.isOpened():
            print("cannot open video")
            sys.exit(1)

        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int((1.0 / float(fps)) * 1000)

        while (cap.isOpened()):
            ret, im = cap.read()
            if not ret:
                break

            out_im = apply_transformations(im)
            cv2.imshow("Output - Press 'q' to exit", out_im)
            k = cv2.waitKey(delay)
            if k & 0xFFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    sys.exit(0)