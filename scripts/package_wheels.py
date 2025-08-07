#!/usr/bin/env python3
"""
Script to package OpenCV wheels from built binaries
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def main():
    """Package wheels from existing OpenCV build"""
    
    # Ensure we're in the right directory
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)
    
    print("Packaging OpenCV custom build into wheel...")
    
    # Clean previous builds
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('opencv_custom.egg-info'):
        shutil.rmtree('opencv_custom.egg-info')
    
    # Build wheel
    try:
        subprocess.run([sys.executable, '-m', 'build', '--wheel'], check=True)
        print("✓ Wheel built successfully")
        
        # List generated wheels
        if os.path.exists('dist'):
            wheels = list(Path('dist').glob('*.whl'))
            print(f"Generated wheels: {len(wheels)}")
            for wheel in wheels:
                size_mb = wheel.stat().st_size / (1024 * 1024)
                print(f"  - {wheel.name} ({size_mb:.1f} MB)")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Wheel build failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())