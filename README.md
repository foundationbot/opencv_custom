# OpenCV Custom Build with CUDA Support

Custom OpenCV build with CUDA support and contrib modules, packaged for easy installation via pip.

## Features

- OpenCV 4.13.0 with CUDA acceleration
- Full contrib modules included
- Optimized for Python 3.10
- Pre-built wheels for Linux x64
- Hardware accelerated video encoding/decoding

## Installation

### From Pre-built Wheels (Recommended)

```bash
pip install opencv-custom
```

### From Source

```bash
git clone git@github.com:foundationbot/opencv_custom.git
cd opencv_custom
pip install .
```

## Requirements

- Python >= 3.10, < 3.11
- CUDA-compatible GPU (for GPU acceleration)
- Linux x64 (other platforms coming soon)

## Dependencies

- numpy >= 1.21.0, < 2.0.0
- depthai >= 2.30.0.0 (optional, for OAK camera support)

## Usage

```python
import cv2
print(cv2.__version__)
print(cv2.cuda.getCudaEnabledDeviceCount())  # Check CUDA devices
```

## Building Wheels

This repository includes GitHub Actions for automated wheel building:

- Wheels are built automatically on releases
- Support for multiple Python versions can be added
- Cross-compilation support planned
