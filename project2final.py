
import numpy as np
import argparse
import cv2
import datetime

refPt = []
refPt2 = []
refPt3 = []
refPt4 = []
cropping = False
cropping2 = False
cropping3 = False
cropping4 = False
drawing = False
drawing2 = False
drawing3 = False
drawing4 = False
watermark = False

def click_and_crop(event, x, y, flags, param):

    global refPt, drawing, cropping, closeres

    cv2.imshow("image", closeres)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            closeres = cloneclone.copy()
            cv2.rectangle(closeres, refPt[0], (x,y),(0,255,0),2)
        
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        refPt.append((x, y))
        cropping = False

        cv2.rectangle(closeres, refPt[0], refPt[1], (0, 255, 0), 2)

def click_and_crop2(event, x, y, flags, param):

    global refPt2, cropping2, drawing2, closerevres
    
    cv2.imshow("image", closerevres)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing2 = True
        refPt2 = [(x, y)]
        cropping2 = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing2 == True:
            closerevres = clone2clone2.copy()
            cv2.rectangle(closerevres, refPt2[0], (x,y),(0,255,0),2)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing2 = False
        refPt2.append((x, y))
        cropping2 = False
 
        cv2.rectangle(closerevres, refPt2[0], refPt2[1], (0, 255, 0), 2)

def click_and_crop3(event, x, y, flags, param):

    global refPt3, cropping3, drawing3, holres
    
    cv2.imshow("image", holres)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing3 = True
        refPt3 = [(x, y)]
        cropping3 = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing3 == True:
            holres = clone3clone3.copy()
            cv2.rectangle(holres, refPt3[0], (x,y),(0,255,0),2)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing3 = False
        refPt3.append((x, y))
        cropping3 = False
 
        cv2.rectangle(holres, refPt3[0], refPt3[1], (0, 255, 0), 2)

def click_and_crop4(event, x, y, flags, param):

    global refPt4, cropping4, drawing4, holrevres
    
    cv2.imshow("image", holrevres)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing4 = True
        refPt4 = [(x, y)]
        cropping4 = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing4 == True:
            holrevres = clone4clone4.copy()
            cv2.rectangle(holrevres, refPt4[0], (x,y),(0,255,0),2)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing4 = False
        refPt4.append((x, y))
        cropping4 = False
 
        cv2.rectangle(holrevres, refPt4[0], refPt4[1], (0, 255, 0), 2)
        
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-j", "--image2", required = True, help = "Path to the image")
ap.add_argument("-k", "--hol", required = True, help = "Path to the image")
ap.add_argument("-l", "--holrev", required = True, help = "Path to the image")
ap.add_argument("-m", "--watermark", type= bool, required = True, help = "True or False")
ap.add_argument("-n", "--text", type = str, required = False, help = "Name of company")
ap.add_argument("-o", "--sn", type = str, required = True, help = "Serial Number")
args = vars(ap.parse_args())

if args["watermark"] is True:
    watermark = True


if watermark is True and args["text"]is not None:
    watermarkstr = "Copyright " + str(datetime.datetime.now().year) + " " + args["text"]
else:
    watermark = False
    watermarkstr = ""

serialnumber = args["sn"]

bluetitle = serialnumber + ".jpg"
holtitle = serialnumber + "HOL.jpg"
holrevtitle = serialnumber + "HOLREV.jpg"

image = cv2.imread(args["image"])
image2 = cv2.imread(args["image2"])
image3 = cv2.imread(args["hol"])
image4 = cv2.imread(args["holrev"])

background = cv2.imread('blue_temp.jpg')
background2 = background.copy()

closeres = cv2.resize(image, (1400,927), interpolation = cv2.INTER_CUBIC)
closerevres = cv2.resize(image2, (1400,927), interpolation = cv2.INTER_CUBIC)

holres = cv2.resize(image3, (1400,927), interpolation = cv2.INTER_CUBIC)
holrevres = cv2.resize(image4, (1400,927), interpolation = cv2.INTER_CUBIC)

clone = closeres.copy()
cloneclone = closeres.copy()
clone2 = closerevres.copy()
clone2clone2 = closerevres.copy()
clone3 = holres.copy()
clone3clone3 = holres.copy()
clone4 = holrevres.copy()
clone4clone4 = holrevres.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
    cv2.imshow("image", closeres)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        closeres = clone.copy()
    
    elif key == ord("c"):
        cv2.destroyAllWindows()
        break

if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop2)

while True:
    cv2.imshow("image", closerevres)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("r"):
        closerevres = clone2.copy()
    
    elif key == ord("c"):
        cv2.destroyAllWindows()
        break

if len(refPt2) == 2:
    roi2 = clone2[refPt2[0][1]:refPt2[1][1], refPt2[0][0]:refPt2[1][0]]

rightsize = cv2.resize(roi, (635,640), interpolation = cv2.INTER_CUBIC)
rightsize2 = cv2.resize(roi2, (635,640), interpolation = cv2.INTER_CUBIC)

cv2.rectangle(background2, (55,25), (690,665), (0, 255, 0), 2)


cv2.rectangle(background2, (710,25), (1345,665), (0, 255, 0), 2)

ret, thresh = cv2.threshold(background, 127, 255, cv2.THRESH_BINARY)

for i in range(25, 665):
    for j in range(55, 690):        
        pixel = thresh[i,j]
        whitePixel = [255,255,255]
        if np.array_equal(pixel,whitePixel):
            background[i,j] = rightsize[i-25,j-55]

for i in range(25, 665):
    for j in range(710, 1345):
        pixel = thresh[i,j]
        whitePixel = [255,255,255]
        if np.array_equal(pixel,whitePixel):
            background[i,j] = rightsize2[i-25,j-710]


if watermark == True:
    x = 490
    y = 625
    overlay = background.copy()
    cv2.putText(overlay, watermarkstr,(x,y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, 2)
    cv2.addWeighted(overlay, 0.4, background, 0.6, 0, background)


cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop3)

while True:
    cv2.imshow("image", holres)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("r"):
        closeres = clone3.copy()
    
    elif key == ord("c"):
        cv2.destroyAllWindows()
        break

if len(refPt3) == 2:
    roi3 = clone3[refPt3[0][1]:refPt3[1][1], refPt3[0][0]:refPt3[1][0]]

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop4)

while True:
    cv2.imshow("image", holrevres)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("r"):
        holrevres = clone4.copy()
    
    elif key == ord("c"):
        cv2.destroyAllWindows()
        break

if len(refPt4) == 2:
    roi4 = clone4[refPt4[0][1]:refPt4[1][1], refPt4[0][0]:refPt4[1][0]]


rightsizehol = cv2.resize(roi3, (974,1050), interpolation = cv2.INTER_CUBIC)
rightsizeholrev = cv2.resize(roi4, (974,1050), interpolation = cv2.INTER_CUBIC)

if watermark == True:
    x = 265
    y = 1035
    overlay2 = rightsizehol.copy()
    cv2.putText(overlay2, watermarkstr,(x,y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, 0)
    cv2.addWeighted(overlay2, 0.4, rightsizehol, 0.6, 0, rightsizehol)

if watermark == True:
    x = 265
    y = 600
    overlay3 = rightsizeholrev.copy()
    cv2.putText(overlay3, watermarkstr,(x,y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, 0)
    cv2.addWeighted(overlay3, 0.4, rightsizeholrev, 0.6, 0, rightsizeholrev)

cv2.imwrite(holtitle, rightsizehol)
cv2.imwrite(holrevtitle, rightsizeholrev)
cv2.imwrite(bluetitle, background)

