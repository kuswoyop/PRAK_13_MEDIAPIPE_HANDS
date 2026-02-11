import cv2
import mediapipe
capture = cv2.VideoCapture(0)
mediapipehand = mediapipe.solutions.hands
tangan = mediapipehand.Hands()

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = tangan.process(imgRGB)
    if result.multi_hand_landmarks:
        print("tangan")
    else:
        print("tidak ada")
    cv2.imshow("webcam", img)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'): break
capture.realese() # Tutupwebcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()

import cv2 #import module opencv
import mediapipe
capture = cv2.VideoCapture(0)
mediapipehand = mediapipe.solutions.hans
tangan = mediapipehand.Hands(max_num_hands=1)
mpdraw = mediapipe.solutions.drawing_utils

while True:
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = tangan.process(imgRGB)

    if result.multi_hand_landmarks:
        for titiktangan in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,titiktangan,mediapipehand.HAND_CONNECTIONS)
            for id, titik in enumerate(titiktangan.landmark) :
                print (id)
                print(titik.x)
                print(titik.y)

    cv2.imshow("webcam,img")
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'): break
capture.realease()
cv2.destroyAllWindows()

if result.multi_handedness:
    for idx, hand in enumerate(result.multi_handedness):
        if hand.classification[0].index ==1:
            cv2.putText(img,"kanan",(200,50),
                        cv2.FRONT_HERSHEY_PLAIN,5,(255,0,0),3)
        elif hand.classification[0].index ==0:
            cv2.putText(img,"kiri",(200,50),
                        cv2.FRONT_HERSHEY_PLAIN,5,(0,0,255),3)
