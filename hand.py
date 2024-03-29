import cv2
import mediapipe as mp 
cap= cv2.VideoCapture(0)
mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
def drawhandlandmarks(image,hand_landmarks):
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image,landmarks,mp_hands.HAND_CONNECTIONS)
while True:
    success,image=cap.read()
    image=cv2.flip(image,1)
    results=hands.process(image)
    hand_landmarks=results.multi_hands_landmarks
    drawhandlandmarks(image,hand_landmarks)
    cv2.imshow("display",image)
    key=cv2.waitKey(1)
    if key==32:
        break
cv2.destroyAllWindows()

