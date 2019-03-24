from cv2 import *
from math import *


class ShapeRegconition:
    def __init__(self, image_contour):
        self.image_contour = image_contour

    def detect(self):
        # Default case
        shape = 'Unidentified'
        # Create approximates from contour
        approx = approxPolyDP(self.image_contour, 0.04*arcLength(self.image_contour, True), True)  # arg2 is accuracy, arg3 is connect all approx when true
        # Triangle
        if len(approx) == 3:
            shape = '3, Triangle'
        # Rectangle or Square
        elif len(approx) == 4:
            c = self.image_contour
            vectorA = [c[0][0][0] - c[3][0][0], c[0][0][1] - c[3][0][1]]
            vectorB = [c[0][0][0] - c[7][0][0], c[0][0][1] - c[7][0][1]]
            # print(vectorB)
            # print(vectorA)
            print(c)
            if vectorA[0]*vectorB[0] + vectorA[1]*vectorB[1] == 0:
                x, y, w, h = cv2.boundingRect(approx)
                ar = w / float(h)
                shape = "4, Square" if (ar >= 0.95) and (ar <= 1.05) else "4, Rectangle"

            else:

                shape = "4, Other Quadrilaterals"
        # Pentagon
        elif len(approx) == 5:
            shape = '5, Pentagon'
        # Hexagon
        elif len(approx) == 6:
            shape = '6, Hexagon'
        else:
            shape = 'Circle'
        return shape
