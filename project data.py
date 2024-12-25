import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# initialize webcam
cap = cv2.VideoCapture(0)
# Initialize the hand detector from cvzone library.
detector = HandDetector(maxHands=1)

# Set offset(Padding around the cropped hand) and image size(Desired size of the square output image) parameters.
offset = 20
imgSize = 300

# Specify the folder to save cropped hand images.
folder = "C:\\Users\\sarod\\OneDrive\\Desktop\\Data\\R"

# Counter for the number of saved images.
counter = 0

# To process webcam feed.
while True:
    # Read a frame from the webcam
    success, img = cap.read()

    # Detect hands in the frame and get their bounding boxes
    hands, img = detector.findHands(img)

    if hands:
        # Get information about the first detected hand.
        hand = hands[0]
        # Bounding box coordinates and dimensions.
        x, y, w, h = hand['bbox']

        # Create a blank white image of specified size.
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        # Crop the detected hand area from the webcam frame with some padding.
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape
        # Calculate the aspect ratio of the hand region.
        aspectRatio = h / w
        # Adjust the cropped image to fit the square white image.
        if aspectRatio > 1:
            # If height > width, resize based on height.
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            # Center the resized image horizontally.
            imgWhite[:, wGap:wCal + wGap] = imgResize
        else:
             # If width > height, resize based on width.
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            # Center the resized image vertically.
            imgWhite[hGap:hCal + hGap, :] = imgResize
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)
    # Display the original webcam feed
    cv2.imshow("Image", img)
    # Check for user input to save the processed image.
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)