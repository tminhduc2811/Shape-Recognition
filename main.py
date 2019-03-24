from cv2 import *
from ShapeRegconition import ShapeRegconition
import imutils

PATH = 'shapes2.png'

img = imread(PATH)
gray_img = cvtColor(img, COLOR_BGR2GRAY)
# blur_img = GaussianBlur(gray_img, (5, 5), 0)
# blur_img = GaussianBlur(gray_img, (5, 5), 0)
blur_img = medianBlur(gray_img, 3)
thresh_img = threshold(blur_img, 10, 255, THRESH_BINARY)[1]

# Find contours
contours = findContours(thresh_img, RETR_LIST, CHAIN_APPROX_SIMPLE)  # Only get necessary points
for c in contours[0]:
    M = moments(c)
    cx = int((M["m10"] / M["m00"]))
    cy = int((M["m01"] / M["m00"]))
    shape = ShapeRegconition(c).detect()
    drawContours(img, [c], -1, (0, 255, 0), 2)
    putText(img, shape, (cx, cy), FONT_HERSHEY_DUPLEX, 0.5, (155, 222, 250), 1)
imwrite('Result2.jpg', img)
imshow("Image", img)
waitKey(0)
#     print(c)
#     print(len(c))
# print(contours[1][0][0])