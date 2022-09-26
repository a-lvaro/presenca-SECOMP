import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime, date

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


time = datetime.now()
# if time.hour == 13 and time.day == 4:
#     file = f'presenca/presencaWorshopEleflow{date.today()}.csv'
# elif time.hour == 13 and time.day == 6:  # aqui vão acontecer dois workshops
#     file = f'presenca/presencaWorshopEleflow{date.today()}.csv'
# elif time.hour == 13 and time.day == 7:
#     file = f'presenca/presencaWorshopFusca{date.today()}.csv'

if time.hour < 18:
    file = f'presenca/presenca{date.today()}.csv'
else:
    file = f'presenca/presencaAposIntervalo{date.today()}.csv'


with open('presenca/myDataFile.txt') as f:
    myDataList = f.read().splitlines()

with open(file, 'a'):
    pass

presenceList = np.loadtxt(file, delimiter=",", dtype=str)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode(
            'utf-8').encode('shift-jis').decode('utf-8')

        myOutput = myData
        myColor = (0, 255, 0)

        if myData in myDataList:
            myOutput = myData
            myColor = (0, 255, 0)

            if myData not in presenceList:
                time = datetime.now()
                with open(file, 'a') as p:
                    p.write(myData + ',')
                    p.write(f'{time.hour}:{time.minute}:{time.second}\n')

                presenceList = np.loadtxt(
                    file, delimiter=",", dtype=str, usecols=(0))

        else:
            myOutput = myData
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, myColor, 2)

        if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
            break

    img = cv2.flip(img, 1)
    cv2.imshow('Result', img)
    cv2.waitKey(1)
