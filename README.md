# OpenCV Custom Build with CUDA Support

Custom OpenCV build with CUDA support and contrib modules, packaged for easy installation via pip.


## Requirements

- Python >= 3.10, < 3.11
- CUDA-compatible GPU (for GPU acceleration)
- Linux x64 (other platforms coming soon)

## Dependencies

- numpy >= 1.21.0, < 2.0.0

## Usage

```python
import cv2
print(cv2.__version__)
print(cv2.cuda.getCudaEnabledDeviceCount())  # Check CUDA devices
```