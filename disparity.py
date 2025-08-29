import cv2
import numpy as np

# Load stereo image pair
img_left = cv2.imread("left.png", cv2.IMREAD_GRAYSCALE)
img_right = cv2.imread("right.png", cv2.IMREAD_GRAYSCALE)

#Works by sliding a small window (block) in the left image and searching for the best match in the right image along the same row. This shift between the two is called disparity.
#BM = Block Matching
stereo = cv2.StereoBM_create(numDisparities=16*6, blockSize=15)

# Compute disparity map
#The values are in fixed-point format (scaled by 16).
#Larger disparity → object is closer, Smaller disparity → object is farther.
disparity = stereo.compute(img_left, img_right)


# actual disparity numbers could be in a range like -1 to 1600.
# Normalize for visualization = maps it into 0–255 so the depth differences become visible.
#0 (black) to 255 (white) = can see the depth gradient as shades of gray.
disparity_normalized = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
disparity_normalized = np.uint8(disparity_normalized)


#Disparity (d) to Depth (Z) ( Triangulation = Z: focal length* baseline / d )
#Z is inversely Proportional to d.
# Assumed focal length and baseline 
focal_length_px = 554.0  # in pixels
baseline_m = 0.06        # in meters (6 cm)

depth_map = (focal_length_px * baseline_m) / (disparity + 1e-6)

# Normalize for visualization
#np.uint8 = (0–255 integers) for grayscale or color images. 
disparity_normalized = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
disparity_normalized = np.uint8(disparity_normalized)

depth_vis = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)
depth_vis = np.uint8(depth_vis) #Converts to 8-bit grayscale for display.

# Show results
cv2.imshow("Left Image", img_left)
cv2.imshow("Right Image", img_right)
cv2.imshow("Disparity Map", disparity_normalized)
cv2.imshow("Depth Map", depth_vis)
cv2.waitKey(0)
cv2.destroyAllWindows()

