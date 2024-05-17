import cv2



print(cv2.__version__)

cam = cv2.VedioCapture(0)
cam.set(1,640)
cam.set(4,480)

detector = cv2.CascdeClassifier('haarcascade_frontalface_default.xml')

face_id = input("Enter a numeric user ID here")
print("taking samples,look at camera ....")
count = 0

while True:
    ret, img = cam.read()
    converted_image = cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)
    faces = detector.detecMultiScale(converted_image,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0), 2)
        count += 1


        cv2.imwrite("samples/faces." +str(face_id) + '.' + str(count) + ".jpg",converted_image[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitkey(100) & 0xff
    if k == 27:
        break
    elif count >= 20:
        break

print("sample taken now closing the program sir")
cam.release()
cv2.destroyAllWindows()
