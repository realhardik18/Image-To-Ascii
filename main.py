import cv2

Image = cv2.imread("images/test.jpg")
Image_blac_and_white = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(
    Image_blac_and_white, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("final", Image_blac_and_white)
cv2.waitKey(0)
cv2.destroyAllWindows
