import cv2 as cv
import random

# Load Haar Cascade for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Mock expressions list (replace with real model output later)
expressions = ["Happy", "Sad", "Neutral", "Angry", "Surprised"]

# Initialize webcam
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("Webcam error")
        break

    flip = cv.flip(frame, 1)
    gray = cv.cvtColor(flip, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Random expression placeholder — replace with real prediction later
        expression = random.choice(expressions)

        # Draw green box
        cv.rectangle(flip, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put expression text
        cv.putText(flip, expression, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow("Expression Detector", flip)

    if cv.waitKey(10) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
