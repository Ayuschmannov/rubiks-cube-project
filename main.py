import cv2
import numpy as np
import glob

path = <path of image>
img_number = 1

for file in glob.glob(path):
    img = cv2.imread(file)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #defining coordinate lists
    cord = []
    final = []
    color = [] 
    color2 = []
    # right now, trying on perfect images, afterwards, will try to blur etc
    # def preprocess(img):
    #     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    #     img_canny = cv2.Canny(img_blur, 50, 50)
    #     kernel = np.ones((3, 3))
    #     img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    #     img_erode = cv2.erode(img_dilate, kernel, iterations=1)
    #     return img_erode

    # defining lower limits
    lowred = np.array([0,190,20])
    lowyell = np.array([15,160,20])
    lowblu = np.array([100,100,20])
    lowpink = np.array([140,100,20])
    lowgreen = np.array([55,100,20])

    # defining higher limits
    hired = np.array([10,255,255])
    hiyell = np.array([50,255,255])
    hiblu = np.array([135, 255, 255])
    higreen = np.array([80,255,255])
    hipink = np.array([180,255,255])

    # defining all masks
    maskred = cv2.inRange(hsv, lowred, hired)
    maskyell = cv2.inRange(hsv, lowyell, hiyell)
    maskblu = cv2.inRange(hsv, lowblu, hiblu)
    maskpink = cv2.inRange(hsv, lowpink, hipink)
    maskgreen = cv2.inRange(hsv, lowgreen, higreen)

    # defining all contours
    cntrred, hierarchyred = cv2.findContours(maskred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cntrblu, hierarchyblu = cv2.findContours(maskblu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cntryell, hierarchyyell = cv2.findContours(maskyell, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cntrgreen, hierarchygreen = cv2.findContours(maskgreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cntrpink, hierarchypink = cv2.findContours(maskpink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cntrall = cntrred + cntrblu + cntryell + cntrgreen + cntrpink

    sorted_ctrs = sorted(cntrall, key=lambda ctr: cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1] * img.shape[1] )
    for i, ctr in enumerate(sorted_ctrs):
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)
            x1 = int(x+(w/2))
            y1 = int(y+(h/2))
            color.append((img[y1, x1]).tolist())

    k = 0
    for x in color:
            # check if exists in unique_list or not
            if x not in color2:
                color2.append(x)

    for y in color:
        for z in color2:
            if y == z:
                final.append(color2.index(z) + 1)


    # print(final)

    output_path = r'C:\Users\ayusc\OneDrive\Pictures\output/output_image_'
    completeName = output_path + str(img_number) + '.txt'
    img_number += 1
    print(completeName)
    # cv2.imshow("color detection", img)
    f = open(completeName, "w+")
    for a in range(0,9):
        f.write("%d" % (final[a]))
        f.write("\t")
        if(a == 2 or a== 5 or a == 8):
            f.write("\n")
    f.close()


    # Wait Key
    cv2.waitKey(0)
    # Destroy window
    cv2.destroyAllWindows()
