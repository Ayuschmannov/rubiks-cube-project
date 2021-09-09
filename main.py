import cv2
import numpy as np

#defining coordinate lists
cord = []
final = []

#rgb values of colors
#red--    255,22,22
#yellow-- 255,222,89
#green-- 0,128,55
#blue--  0,74,173

# the code is incomplete as of now.
# i am able to arrange the contours in desired order
# but work is in progress regarding proper numbering of contours

def threelargest(list):
# i am working on this function and this is incomplete as of now
    y_sorted = sorted(list, key=lambda l: l[1], reverse=False)
    a = y_sorted[0]
    b = y_sorted[1]
    c = y_sorted[2]
    y1 = [a,b,c]
    x1 = sorted(y1, key=lambda x: (x[0], x[1]))

    a1 = x1[0]
    c1 = img[a1[1],a1[0]]
    a2 = x1[1]
    c2 = img[a2[1], a2[0]]
    a3 = x1[2]
    c3 = img[a3[1], a3[0]]
    c4 = img[804, 724]
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    if(c2.all() == c4.all()):
        print("same")
    else:
        print("different")

    # for x in x1new:
    #     a[i] = x1new[0]
    # print(c1)
    # print(c2)
    # print(x1new[0])
    # print(x1new)
    d = y_sorted[3]
    e = y_sorted[4]
    f = y_sorted[5]
    y2 = [d,e,f]
    x2 = sorted(y2, key=lambda x: (x[0], x[1]))
    x2new = [i[::-1] for i in x1[::1]]


    # print(x2)

    # print(y2)
    g = y_sorted[6]
    h = y_sorted[7]
    i = y_sorted[8]
    y3 = [g,h,i]
    x3 = sorted(y3, key=lambda x: (x[0], x[1]))
    x3new = [i[::-1] for i in x1[::1]]

# reading image
img = cv2.imread(<path of image>)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

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
lowwhite = np.array([0,0,100])
lowpink = np.array([140,100,20])
lowgreen = np.array([55,100,20])

# defining higher limits
hired = np.array([10,255,255])
hiyell = np.array([50,255,255])
hiblu = np.array([135, 255, 255])
hiwhite = np.array([0,0,255])
higreen = np.array([80,255,255])
hipink = np.array([180,255,255])

# defining all masks
maskred = cv2.inRange(hsv, lowred, hired)
maskyell = cv2.inRange(hsv, lowyell, hiyell)
maskblu = cv2.inRange(hsv, lowblu, hiblu)
maskwhite = cv2.inRange(hsv, lowwhite, hiwhite)
maskpink = cv2.inRange(hsv, lowpink, hipink)
maskgreen = cv2.inRange(hsv, lowgreen, higreen)

# defining all contours
cntrred, hierarchyred = cv2.findContours(maskred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cntrblu, hierarchyblu = cv2.findContours(maskblu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cntryell, hierarchyyell = cv2.findContours(maskyell, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cntrwhite, hierarchywhite = cv2.findContours(maskwhite, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cntrgreen, hierarchygreen = cv2.findContours(maskgreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cntrpink, hierarchypink = cv2.findContours(maskpink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# getting red contours
i = 0
if len(cntrred) != 0:
    for contour in cntrred:
        #print(cv2.contourArea(contour))
        if cv2.contourArea(contour) > 1000:
            cv2.drawContours(img, cntrred, i, (0, 255, 0), 3)
            M = cv2.moments(contour)
            rX = int(M["m10"] / M["m00"])
            rY = int(M["m01"] / M["m00"])
            cord.append([rX, rY])
            # ycord.append(rY)
            print("Red: ")
            print(rX, rY)
        i = i + 1
        # x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
        #print("i= ")
        #print(i)

# getting blue contours
j = 0
if len(cntrblu) != 0:
    for contour in cntrblu:
        if cv2.contourArea(contour) > 1000:
            # x, y, w, h = cv2.boundingRect(contour)
            #print(cv2.contourArea(contour))
            # cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
            cv2.drawContours(img, cntrblu, j, (255, 255, 0), 3)
            M = cv2.moments(contour)
            bX = int(M["m10"] / M["m00"])
            bY = int(M["m01"] / M["m00"])
            cord.append([bX, bY])
            # ycord.append(bY)
            print("Blue: ")
            print(bX, bY)
        j = j + 1
        # print("j = ")
        # print(j)

# getting yellow contours
k = 0
if len(cntryell) != 0:
    for contour in cntryell:
#         print(cv2.contourArea(contour))
        if cv2.contourArea(contour) > 1000:
            cv2.drawContours(img, cntryell, k, (0, 0, 255), 3)
        #     x, y, w, h = cv2.boundingRect(contour)
        #     cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
            M = cv2.moments(contour)
            yX = int(M["m10"] / M["m00"])
            yY = int(M["m01"] / M["m00"])
            cord.append([yX, yY])
            # ycord.append(yY)
            print("Yellow: ")
            print(yX, yY)
        k = k + 1
        # print("k = ")
        # print(k)

# i = 0
# if len(cntrwhite) != 0:
#     for contour in cntrwhite:
        # print(cv2.contourArea(contour))
        # if cv2.contourArea(contour) > 1000:
        #     cv2.drawContours(img, cntrwhite, i, (80, 0, 255), 3)
        #     M = cv2.moments(contour)
        #     wX = int(M["m10"] / M["m00"])
        #     wY = int(M["m01"] / M["m00"])
        #     xcord.append(wX)
        #     ycord.append(wY)
        #     print("White: ")
        #     print(wX, wY)
        # i = i + 1

# getting green contours
i = 0
if len(cntrgreen) != 0:
    for contour in cntrgreen:
        #print(cv2.contourArea(contour))
        if cv2.contourArea(contour) > 1000:
            cv2.drawContours(img, cntrgreen, i, (0, 255, 0), 3)
            M = cv2.moments(contour)
            gX = int(M["m10"] / M["m00"])
            gY = int(M["m01"] / M["m00"])
            cord.append([gX, gY])
            # ycord.append(gY)
            print("Green: ")
            print(gX, gY)

        i = i + 1

# getting pink contours
i = 0
if len(cntrpink) != 0:
    for contour in cntrpink:
        #print(cv2.contourArea(contour))
        if cv2.contourArea(contour) > 1000:
            cv2.drawContours(img, cntrpink, i, (255, 255, 200), 3)
            M = cv2.moments(contour)
            pX = int(M["m10"] / M["m00"])
            pY = int(M["m01"] / M["m00"])
            cord.append([pX, pY])
            # ycord.append(pY)
            print("Pink: ")
            print(pX, pY)
        i = i + 1

#calling the function
threelargest(cord)
cv2.imshow("color detection", img)

# Wait Key
cv2.waitKey(0)
# Destroy window
cv2.destroyAllWindows()
