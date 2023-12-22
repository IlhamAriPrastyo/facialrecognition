import cv2
import pickle
import serial
import time  # Import the time module

# Setting serial port to COM4 at baud rate of 9600
port = serial.Serial('COM4', 9600)

video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognise = cv2.face.LBPHFaceRecognizer_create()
recognise.read("trainner.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    og_label = pickle.load(f)
    labels = {v: k for k, v in og_label.items()}
    print(labels)

sampleno = 0

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in face:
        face_save = gray[y:y + h, x:x + w]

        ID, conf = recognise.predict(face_save)

        if conf >= 20 and conf <= 115:
            print(ID)
            print(labels[ID])
            cv2.putText(frame, labels[ID], (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (18, 5, 255), 2, cv2.LINE_AA)

            if ID == 2:
                port.write(str.encode('1'))
                print("Selamat Datang")

                # Add a delay of 1000 ms (1 second)
                time.sleep(0.5)
            elif ID == 1:
                port.write(str.encode('2'))
                print("Tamu")

                # Add a delay of 1000 ms (1 second)
                time.sleep(0.5)

            elif ID == 0 :
                port.write(str.encode('0'))

        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 4)

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
