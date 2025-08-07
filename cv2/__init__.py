"""
Custom OpenCV Python bindings with CUDA and contrib modules support.

This wheel is built specifically for Python 3.10 on Linux x86_64.
Requires CUDA drivers for GPU functionality.
"""

import os
import sys

# Get the current directory where cv2 package is installed
_current_dir = os.path.dirname(__file__)


# Warn if LD_LIBRARY_PATH does not include the cv2 directory
if sys.platform.startswith('linux'):
    ld_path = os.environ.get('LD_LIBRARY_PATH', '')
    if _current_dir not in ld_path.split(':'):
        import warnings
        warnings.warn(
            f"LD_LIBRARY_PATH does not include the cv2 directory ({_current_dir}). "
            "If you get ImportError for missing .so files, set LD_LIBRARY_PATH before starting Python: "
            f"export LD_LIBRARY_PATH={_current_dir}:$LD_LIBRARY_PATH"
        )

# Import the Python 3.10 cv2 extension
try:
    import importlib.util
    
    cv2_path = os.path.join(_current_dir, 'cv2.cpython-310-x86_64-linux-gnu.so')
    if not os.path.exists(cv2_path):
        raise ImportError(f"OpenCV Python 3.10 extension not found at {cv2_path}")
    
    spec = importlib.util.spec_from_file_location("cv2", cv2_path)
    _cv2_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(_cv2_module)
    
    # Import all symbols from the cv2 module into this namespace
    for name in dir(_cv2_module):
        if not name.startswith('_'):
            globals()[name] = getattr(_cv2_module, name)
            
    __version__ = "4.13.0"
    
except ImportError as e:
    import platform
    python_version = platform.python_version()
    
    error_msg = f"""
Failed to import OpenCV for Python {python_version}.

This wheel is built specifically for Python 3.10 on Linux x86_64.
You are using Python {python_version}.

To fix this:
- Use Python 3.10 on Linux x86_64
- Install CUDA drivers for GPU functionality
- Ensure all OpenCV dependencies are available

Original error: {e}
"""
    raise ImportError(error_msg) from e