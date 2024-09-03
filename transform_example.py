# import the necessary packages
from transform import four_point_transform
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
ap.add_argument("-c", "--coords", required=True, help="Comma-separated list of source points")
args = vars(ap.parse_args())

# load the image and grab the source coordinates (i.e., the list of (x, y) points)
image = cv2.imread(args["image"])
if image is None:
    raise ValueError("Image not found or path is incorrect.")

pts = np.array([float(x) for x in args["coords"].split(",")], dtype="float32").reshape(-1, 2)

# apply the four-point transform to obtain a "bird's eye view" of the image
warped = four_point_transform(image, pts)

# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)



