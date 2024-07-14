
# Edge Detection and Motion Detection on Raspberry Pi using OpenCV

This project captures images using a 5MP camera connected to a Raspberry Pi and processes them to highlight object boundaries using edge detection. Additionally, it detects motion based on changes between consecutive frames using Mean Squared Error (MSE).

## Hardware Requirements

- Raspberry Pi
- 5MP Camera Module

## Software Requirements

- Raspberry Pi OS
- Python 3
- OpenCV

## Installation

1. **Update package lists**:
    ```sh
    sudo apt-get update
    ```

2. **Install OpenCV**:
    ```sh
    sudo apt-get install python3-opencv
    ```

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Rishi-Priya01/Edge_detection.git
    cd edge-detection-motion-detection
    ```

2. **Run the script**:
    ```sh
    python3 edge_detection_motion_detection.py
    ```

## Script Overview

### edge_detection_motion_detection.py

- **Imports**: Necessary libraries (`cv2`, `time`, `numpy`).
- **Constants**: 
  - `CAMERA_DEVICE_ID`: ID for the camera device.
  - `IMAGE_WIDTH`, `IMAGE_HEIGHT`: Dimensions for image capture.
  - `MOTION_BLUR`: Boolean to toggle Gaussian blur.

- **Functions**:
  - `mse(image_a, image_b)`: Calculates the Mean Squared Error between two images.
  - `lighting_compensation(frame)`: Performs histogram equalization for lighting compensation.

- **Main Script**:
  - Initializes camera capture.
  - Sets image width and height.
  - Captures frames in a loop.
  - Applies Gaussian blur if enabled.
  - Performs lighting compensation and edge detection.
  - Detects motion by comparing consecutive frames using MSE.
  - Displays original, compensated, grayscale, and edge-detected images.
  - Calculates and prints the estimated frames per second (fps).
  - Breaks the loop on pressing the `Esc` key.

## Example Output

- Original Image
- Compensated Image
- Grayscale Image
- Edge-Detected Image

Motion detection will print a message indicating motion detection in a specific frame.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Acknowledgements

- OpenCV: [https://opencv.org/](https://opencv.org/)
- Raspberry Pi: [https://www.raspberrypi.org/](https://www.raspberrypi.org/)
