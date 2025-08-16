This repository hosts custom OpenCV Python wheels with CUDA support and additional features.

## Quick Installation

Download the latest wheel from our [Releases](https://github.com/foundationbot/opencv_custom/releases) page:

```bash
# Replace with the latest version URL from releases
pip install https://github.com/foundationbot/opencv_custom/releases/download/v4.13.0/opencv_contrib_python-4.13.0-cp310-cp310-linux_x86_64.whl
```

## Features

Our custom OpenCV builds include:

- **CUDA Support** - GPU acceleration for computer vision operations
- **Contrib Modules** - Additional modules including ArUco marker detection
- **GStreamer Integration** - Hardware-accelerated video processing
- **Python Typing Support** - Full cv2.typing module for better IDE experience
- **NumPy 1.x Compatibility** - Works with existing NumPy installations

## Build Information

These wheels are built using the official opencv-python build system with custom configurations for:

- CUDA architectures 8.6 and 9.0
- Hardware acceleration optimizations
- Extended module support
- Typing stub generation

## Installation & Usage

After installing from releases:

```python
import cv2
import cv2.typing

# Verify installation
print(f"OpenCV version: {cv2.__version__}")
print(f"CUDA support: {cv2.cuda.getCudaEnabledDeviceCount() > 0}")
print(f"Typing support: {hasattr(cv2, 'typing')}")

# Test ArUco detection
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
print("ArUco module available")
```