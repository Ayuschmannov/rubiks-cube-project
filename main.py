import cv2
import numpy as np
import glob

path = '<path of image folder>'
img_number = 1

for file in glob.glob(path):
    img = cv2.imread(file)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #defining coordinate lists
    cord = []
    sorted_cord = []
    final = []
    color = [] 
    color_distinct = []
    
    # right now, trying on perfect images, afterwards, will try to blur etc
    # def preprocess(img):
    #     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    #     img_canny = cv2.Canny(img_blur, 50, 50)
    #     kernel = np.ones((3, 3))
    #     img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    #     img_erode = cv2.erode(img_dilate, kernel, iterations=1)
    #     return img_erode

    # defining lower limits of colors
    lowred = np.array([0,190,20])
    lowyell = np.array([15,160,20])
    lowblu = np.array([100,100,20])
    lowpink = np.array([140,100,20])
    lowgreen = np.array([55,100,20])

    # defining higher limits of colors
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
    
    cntrall = cntrred + cntrblu + cntryell + cntrgreen + cntrpink  # collection of all contours 

    for contour in cntrall:
        M = cv2.moments(contour)
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cord.append([cx, cy])
#         print("printing coords: ", cord)

    sort_y = sorted(cord, key=lambda k: k[1])
    first_row = sort_y[0:3]
    second_row = sort_y[3:6]
    third_row = sort_y[6:9]

    for y1, y2, y3 in first_row, second_row, third_row:
        sort_x1 = sorted(first_row, key=lambda k: k[0])
        sort_x2 = sorted(second_row, key=lambda k: k[0])
        sort_x3 = sorted(third_row, key=lambda k: k[0])
    sorted_cord = sort_x1 + sort_x2 + sort_x3
#     print("sorted cord []= ", sorted_cord)

    for i in sorted_cord:
        sx = i[0]
        sy = i[1]
        color.append((img[sy, sx]).tolist())

    for x in color:
        if x not in color_distinct:
            color_distinct.append(x)

    for y in color:
        for z in color_distinct:
            if y == z:
                final.append(color_distinct.index(z) + 1)


    # print(final)  #printing the final numbered array

    output_path = '<path>'
    completeName = output_path + str(img_number) + '.txt'
    img_number += 1
    # cv2.imshow("color detection", img)
    f = open(completeName, "w+")
    for a in range(0,9):
        f.write("%d" % (final[a]))
        f.write("\t")
        if(a == 2 or a== 5 or a == 8):
            f.write("\n")
    f.close()


    # Wait Key
#     cv2.waitKey(0)
    # Destroy window
#     cv2.destroyAllWindows()
