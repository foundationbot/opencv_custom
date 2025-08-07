# Git LFS Setup and Push Instructions

Your OpenCV binaries are too large for regular Git. You need to use Git LFS (Large File Storage).

## Commands to run in the opencv_custom directory:

```bash
cd /path/to/opencv_custom

# 1. Install Git LFS (if not already installed)
git lfs install

# 2. The .gitattributes file is already created to track large files

# 3. Since there are no commits yet, just clear the staging area
git rm --cached -r . 2>/dev/null || true  # Remove from staging, ignore errors if nothing staged
git add .gitattributes

# 4. Add files again (LFS will handle large files)
git add .

# 5. Commit with LFS
git commit -m "Initial OpenCV custom build with LFS for large binaries

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 6. Push to GitHub (LFS will handle large files automatically)
git push -u origin main
```

## Alternative: Clean repository approach

If the above doesn't work, start fresh:

```bash
# 1. Remove the wheel file (it's 894MB!)
rm cv2/download/opencv_custom-4.13.0-py3-none-any.whl

# 2. Remove .git directory and start over
rm -rf .git

# 3. Initialize fresh repo with LFS
git init
git lfs install
git add .gitattributes
git add .
git commit -m "Initial OpenCV custom build with LFS"
git remote add origin git@github.com:foundationbot/opencv_custom.git
git push -u origin main
```

## Files being tracked by LFS:
- All `.so` files (shared libraries)
- All `.so.*` files (versioned shared libraries)  
- All `.whl` files (Python wheels)

## GitHub LFS limits:
- Free: 1GB storage, 1GB bandwidth/month
- You may need to upgrade for large OpenCV distributions