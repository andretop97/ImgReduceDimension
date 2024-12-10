import cv2 as cv
import numpy as np

class ImageDimensionReducer():
    def toGrey(self, imagePath: str) -> np.ndarray:
        img = cv.imread(imagePath)
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    def toBlackEndWithe(self,imagePath: str, threshold: int = 127) -> np.ndarray:
        imgGrey = self.toGrey(imagePath)
        (thresh, blackAndWhiteImage) = cv.threshold(imgGrey, threshold, 255, cv.THRESH_BINARY)
        return blackAndWhiteImage

if __name__ == "__main__":
    idr = ImageDimensionReducer()

    imgGrey = idr.toGrey("test.jpeg")
    cv.imshow("Grey scale", imgGrey)

    imgBlackAndWithe = idr.toBlackEndWithe("test.jpeg", 105)
    cv.imshow("Black and Withe scale", imgBlackAndWithe)

    cv.waitKey(0)