# OpenCV Custom Build Distribution Guide

## Quick Install

```bash
pip install opencv_custom-4.13.0-py3-none-any.whl
```

## System Requirements

- **OS**: Linux x86_64
- **Python**: 3.12 or higher
- **CUDA**: Compatible NVIDIA GPU with CUDA drivers (for GPU acceleration)
- **Memory**: ~1GB free space for installation

## Features Included

✅ OpenCV 4.13.0 with CUDA support  
✅ Contrib modules: aruco, face, text, xfeatures2d, ximgproc, etc.  
✅ DNN module with CUDA backend  
✅ Full image/video processing capabilities  

## Usage

```python
import cv2

# Check version
print(cv2.__version__)  # 4.13.0-dev

# Use CUDA features
if cv2.cuda.getCudaEnabledDeviceCount() > 0:
    gpu_frame = cv2.cuda_GpuMat()
    
# Use contrib modules
detector = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
```

## Troubleshooting

**Import Error**: Ensure Python 3.12+ and Linux x86_64  
**CUDA Not Found**: Install NVIDIA drivers and CUDA toolkit  
**Memory Issues**: The wheel is 895MB - ensure sufficient disk space  

## Building From Source

If you need a custom build for different architecture:
1. Clone the repository
2. Modify `pyproject.toml` for your target platform
3. Run: `python -m build --wheel`