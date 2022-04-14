import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     # Loading classifier

# Read the input image
img = cv2.imread('test.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # CV2 processes image in BGR and not in traditional RGB approach

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4) # (Image itself, Sacle factor, minNeighbours)

# Draw rectangle around the faces
for (x, y, w, h) in faces:  # (Coordinate x, coordinate y, rect width, rect height)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Drawing rectangle ((Blue, Green, Red) Thickness)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()   # Wait for a keypress to close the image