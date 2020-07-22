import cv2

fileName=input("Enter the file name \n")  # change the file name if needed
slomo_frame = int(input("Enter the frames you want to change to \n"))
cap = cv2.VideoCapture(fileName) # load the video
while(cap.isOpened()):                    # play the video by reading frame by frame
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame',frame)              # show the video
        if cv2.waitKey(slomo_frame) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
