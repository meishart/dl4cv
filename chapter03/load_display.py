import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)

print("Shape- {}".format(image.shape))
cv2.imshow("Image", image)
cv2.waitKey(0)

