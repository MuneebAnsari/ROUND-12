import cv2
import numpy as np
import os
import time
# Playing video from file:
cap = cv2.VideoCapture('jab_clearBG.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
ret = True
starttime=time.time()
while(ret):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if currentFrame%7==0:
        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
