
import cv2
import matplotlib.pyplot as plt
wget = "https://mx.pinterest.com/pin/4292562139603925/"
image = cv2.imread("4292562139603925")


plt.rcParams["figure.figsize"] = (5,7)
plt.imshow(image)
detectedEdges = cv2.Canny(image,100,150)

plt.imshow(detectedEdges)


cv2.imshow(detectedEdges)
invertedImage = 255 - detectedEdges
cv2.imshow(invertedImage)
cv2.imwrite("Edges.png", cv2.cvtColor(invertedImage,cv2.COLOR_RGB2BGR))

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow
plt.contour(grayImage, origin="image")
ret,thresh = cv2.threshold(grayImage,150,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawCountours(image, contours, -1, (0,255,0),3)
plt.imshow(image)
cv2.imwrite("SpideyCountours.png", image)