import cv2
import numpy as np


def gammaCorrection(img, gamma):
    table = [((i / 255) ** gamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(img, table)


img = cv2.imread("image.png")
img = cv2.resize(img, (500, 500))
gamma = float(input("Enter the gamma value= "))   
gammaImg = gammaCorrection(img, gamma)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
