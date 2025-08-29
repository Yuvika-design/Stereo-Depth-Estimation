# Stereo Depth Estimation

**Date:** July 2025  
**Tech Stack:** Python, OpenCV, NumPy

## 📌 Overview
This project implements a **stereo vision pipeline** to compute **depth maps** from a pair of stereo images.  
It uses **block matching** to calculate disparity between left and right images, then converts disparity values to real-world depth using triangulation.

**Applications:**  
- Robotics navigation  
- Augmented/Virtual Reality  
- Autonomous vehicles  
- 3D scene reconstruction

---

## 🖼 How It Works
1. Load left and right stereo images.
2. Compute disparity map using OpenCV’s `StereoBM` algorithm.
3. Convert disparity to depth using:
   \[
   Z = \frac{f \cdot B}{d}
   \]
   where:
   - **f** = focal length in pixels  
   - **B** = baseline distance between cameras (in meters)  
   - **d** = disparity in pixels  
4. Normalize both disparity and depth maps for visualization.
5. Display results.

---

## Requirements
- Python 3.x  
- OpenCV  
- NumPy  

Install dependencies:
```bash
pip install opencv-python numpy
```

## Usage

Place left.png and right.png in the project folder.

Run:

python stereo_depth.py


## Output windows:

Left Image

Right Image

Disparity Map

Depth Map

## 📂 File Structure
StereoDepthEstimation/
│── stereo_depth.py       # Main script
│── left.png              # Left stereo image
│── right.png             # Right stereo image
│── README.md             # Project documentation

🛠 Example Output
Left Image	Right Image	Disparity Map	Depth Map

	
## Future Improvements

Implement camera calibration for accurate depth.

Use StereoSGBM for better quality disparity maps.

Generate 3D point clouds.

Add real-time webcam stereo processing.