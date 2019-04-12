import cv2
img=cv2.imread("/home/anshul/Desktop/obama.jpg")


#resized=cv2.resize(img, (600,600))
resized=cv2.resize(img,(int(img.shape[1]*5),int(img.shape[0]*2)))
cv2.imshow("legend",resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()

