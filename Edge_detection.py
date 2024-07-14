import cv2
import time
import numpy as np

CAMERA_DEVICE_ID = 0
IMAGE_WIDTH = 320
IMAGE_HEIGHT = 240
MOTION_BLUR = True

cnt_frame = 0
fps = 0

def mse(image_a, image_b):
    err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])
    return err

def lighting_compensation(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray)

if __name__ == "__main__":
    try:
        cap = cv2.VideoCapture(CAMERA_DEVICE_ID)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            exit()
        
        cap.set(3, IMAGE_WIDTH)
        cap.set(4, IMAGE_HEIGHT)
        
        frame_gray_p = None  # Initialize the previous frame variable

        while True:
            start_time = time.time()
            
            ret, frame_raw = cap.read()
            if not ret:
                print("Error: Failed to capture image")
                break

            if MOTION_BLUR:
                frame = cv2.GaussianBlur(frame_raw, (3, 3), 0)
            else:
                frame = frame_raw

            compensated_frame = lighting_compensation(frame)
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(frame_gray, 100, 200)

            if cnt_frame > 0 and frame_gray_p is not None:
                if mse(frame_gray, frame_gray_p) > 100:
                    print(f'Frame {cnt_frame}: Motion Detected using MSE!')
            
            cv2.imshow('Original', frame)
            cv2.imshow('Compensated', compensated_frame)
            cv2.imshow('Gray', frame_gray)
            cv2.imshow('Edge', edges)

            end_time = time.time()
            seconds = end_time - start_time
            fps = 1.0 / seconds
            print(f"Estimated fps: {fps:.1f}")

            cnt_frame += 1
            frame_gray_p = frame_gray
            
            if cv2.waitKey(1) == 27:
                break

    except Exception as e:
        print(e)
    finally:
        cv2.destroyAllWindows()
        cap.release()
