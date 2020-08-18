import cv2,time

video=cv2.VideoCapture(0)
a=1

while True:
    a=a+1
    check,frame=video.read()
    print(frame)
    cv2.imshow('Capturing',frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('D:\\Programming\\Face Detection OpenCV\\face.jpg')

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('Gray',img)

print(a)
video.release()
cv2.destroyAllWindows()

