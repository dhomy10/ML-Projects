import cv2
import mediapipe as mp

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set up MediaPipe Hands and Drawing Utils
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    # Read a frame from the webcam
    success , img = cap.read()
    img = cv2.flip(img,1)

    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
           for id , lm in enumerate(handLms.landmark):
               h , w , c = img.shape 
               cx , cy = int(lm.x * w) , int(lm.y * h)
               

               lmList.append([id , cx, cy])
               
                
               mpDraw.draw_landmarks(img , handLms , mpHands.HAND_CONNECTIONS)
               if id == 8 :
                   cv2.circle(img, (cx , cy) , 10 , (0 , 255 , 0) , cv2.FILLED)
               if len(lmList) == 21:
                  #print(lmList[4:10], lmList[12])

                  for i in lmList[8:21:4]:

                    for j in lmList[0:21]:
                        for n in lmList[5:7]:
                      

                           if lmList[4][1] < i[1] and lmList[4][2] > j[2]:
                              if lmList[4][1] > n[1] > 
                              print('C')


                  
                   
                   
               

            

    cv2.imshow('Hand Tracker', img)
    if cv2.waitKey(5) & 0xff == 27:
        break
