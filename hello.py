import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Arianne", help="display a square of a given number")
args = parser.parse_args()
print(args.Arianne)

if args.Arianne=="maganda":
    print ("She's mabait")
elif args.Arianne=="mataray":
    print ("Fallacy")
else:
    print ("Mabait siya sobra yey")

arr=[2,4,6,8,10,12,14,16,18,20]
newvar=[i**2 for i in arr]
print(newvar)

import numpy as np
import cv2

# Load an color image in grayscale
#img = cv2.imread('dlsu2.jpg', cv2.IMREAD_COLOR )    
#cv2.imshow('image',img)
#cv2.imwrite('abc.jpg',img)
#print (img.shape)
#print (img)
#cv2.waitKey(0)
#cap = cv2.VideoCapture('Stranger Things 2  Super Bowl 2017 Ad  Netflix.mp4')

#while(cap.isOpened()):
 #   ret, frame = cap.read()
#
 #   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  #  cv2.imshow('frame',gray)
   # if cv2.waitKey(10) & 0xFF == ord('q'):
    #    break

#cap.release()
#cv2.destroyAllWindows()
cap = cv2.VideoCapture('Stranger Things 2  Super Bowl 2017 Ad  Netflix.mp4')

# Define the codec and create VideoWriter object
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
  ret, frame = cap.read()
 
  if ret == True: 
     
    # Write the frame into the file 'output.avi'
    out.write(frame)
 
    # Display the resulting frame    
    cv2.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()