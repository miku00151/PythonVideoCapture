# Capture Card Viewer

A simple Python application using Tkinter to select and display video from a capture card. Users can choose the video device, resolution, and FPS before starting the stream.

## Features
- List and select available video capture devices
- Choose from predefined 16:9 resolutions (640x360, 1280x720, 1920x1080)
- Set FPS (15, 30, 60) before starting the capture
- Display the video stream in a separate window

## Requirements
- Python 3.7+
- `tkinter` (included in standard Python distribution)
- `opencv-python`
- `pillow`
- `pygrabber`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/miku00151/PythonVideoCapture.git
   cd PythonVideoCapture
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python pillow pygrabber
   ```

## Usage
Run the script:
```sh
python main.py
```

## Author
ChatGPT

## License
This project is licensed under the MIT License.

