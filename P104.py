import cv2

ss = cv2.imread("solar-system.jpg")
cv2.putText(ss, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Mercury", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Venus", (190,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Earth", (300,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Mars", (400,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Jupiter", (500,90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Saturn", (720,110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Uranus", (950,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(ss, "Neptune", (1080,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.imshow("The solar system", ss)
cv2.waitKey(0)