# BlueBallDetector Documentation

## Overview

The `BlueBallDetector` class is designed to detect a blue-colored ball in real-time video streams using a webcam. The program utilizes the OpenCV library to capture video from the webcam, process the frames, and detect the blue object based on its color properties. It applies a series of image processing techniques such as Gaussian blur, color space conversion, and morphological operations to identify the blue object and display it on the video feed.

### Features:

- Real-time blue object detection.
- Displays the position of the blue object by drawing a circle and labeling it as "Blue Object."
- Interactive interface that shows the processed video frames along with the mask used for detection.
- Can be exited by pressing the "q" key.

## Requirements

- Python 3.x
- OpenCV (`cv2` package)
- Numpy (`numpy` package)

Install the required libraries with the following command:

```bash
pip install opencv-python numpy
```

## Class: `BlueBallDetector`

### Constructor: `__init__(self, camera_index=0)`

The constructor initializes the `BlueBallDetector` instance, setting up the video capture from the webcam. By default, it captures from the first available camera (camera index 0).

- **Parameters**:

  - `camera_index` (int): The index of the camera to capture from (default is 0 for the first camera).

- **Raises**:
  - `Exception`: If the webcam cannot be opened.

```python
self.cap = cv2.VideoCapture(camera_index)
```

### Method: `process_frame(self, frame)`

This method processes a given video frame to detect the blue object in the image. It applies several image processing techniques to highlight the blue object and returns the processed frame along with the mask.

- **Parameters**:

  - `frame` (numpy.ndarray): The current frame captured from the webcam.

- **Returns**:
  - `processed_frame` (numpy.ndarray): The frame with the detected blue object marked with a circle and labeled.
  - `mask` (numpy.ndarray): A binary mask highlighting the blue regions.

#### Processing steps:

1. **Gaussian Blur**: Blurs the frame to reduce noise and improve contour detection.

   ```python
   blurred = cv2.GaussianBlur(frame, (11, 11), 0)
   ```

2. **HSV Conversion**: Converts the frame from BGR to HSV color space.

   ```python
   hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
   ```

3. **Color Masking**: Filters the frame to isolate blue objects using a predefined range of HSV values for the color blue.

   ```python
   mask = cv2.inRange(hsv, self.blueLower, self.blueUpper)
   ```

4. **Morphological Operations**: Erodes and dilates the mask to remove noise and improve object detection.

   ```python
   mask = cv2.erode(mask, None, iterations=2)
   mask = cv2.dilate(mask, None, iterations=2)
   ```

5. **Contour Detection**: Finds contours in the mask and identifies the largest contour, which is assumed to be the blue object.

   ```python
   cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   ```

6. **Object Detection**: If a contour is found, a circle is drawn around the object, and a label is added.
   ```python
   cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
   cv2.putText(frame, "Blue Object", (int(x - radius), int(y - radius)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
   ```

### Method: `run(self)`

This method continuously captures frames from the webcam and processes them using `process_frame()`. It displays the processed video feed and the binary mask. The program will run until the user presses the "q" key to quit.

- **Returns**:
  - None

#### Main loop:

- Continuously grabs frames from the webcam.
- Calls `process_frame()` to detect and mark the blue object.
- Displays the processed frame and mask using `cv2.imshow()`.
- Exits the loop when the "q" key is pressed.

```python
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
```

## Example Usage

```python
if __name__ == '__main__':
    detector = BlueBallDetector()
    detector.run()
```

### How to use:

1. Connect a webcam to your computer.
2. Run the script.
3. The program will open two windows:
   - The **Frame** window will show the video feed with detected blue objects.
   - The **Mask** window will show a binary mask indicating the blue areas.
4. Press the "q" key to quit the program.

## Customization

You can adjust the following parameters to fine-tune the detection:

- `self.blueLower` and `self.blueUpper`: These define the HSV color range for detecting blue objects. You can modify these values to detect different shades of blue or other colors.

```python
self.blueLower = np.array([100, 150, 50])
self.blueUpper = np.array([140, 255, 255])
```

## Notes

- The performance of the object detection may vary based on lighting conditions and the quality of the webcam.
- The program currently detects objects based on color alone, so objects of similar colors may interfere with detection.
