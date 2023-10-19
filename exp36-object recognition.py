import cv2
image = cv2.imread("C:\\Users\\Hari Naidu\\Downloads\\watch.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
detected_watches = []
min_watch_area = 500
max_watch_area = 2000
for contour in contours:
    area = cv2.contourArea(contour)
    if min_watch_area < area < max_watch_area:
        detected_watches.append(contour)
for contour in detected_watches:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Watch Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
