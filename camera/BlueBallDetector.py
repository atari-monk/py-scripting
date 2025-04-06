import cv2
import numpy as np

class BlueBallDetector:
    def __init__(self, event_bus, camera_index=0):
        self.event_bus = event_bus
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Cannot open webcam")

        self.blueLower = np.array([100, 150, 50])
        self.blueUpper = np.array([140, 255, 255])

    def process_frame(self, frame):
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, self.blueLower, self.blueUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        if cnts:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.putText(frame, "Blue Object", (int(x - radius), int(y - radius)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                self.event_bus.publish("blue_ball_position", (int(x), int(y)))
        return frame, mask

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            processed_frame, mask = self.process_frame(frame)

            cv2.imshow("Frame", processed_frame)
            cv2.imshow("Mask", mask)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    detector = BlueBallDetector()
    detector.run()
