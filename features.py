import cv2
import numpy as np
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter

def segment_iris(image):
    edges = canny(image, sigma=2)
    hough_radii = np.arange(20, 60, 2)
    hough_res = hough_circle(edges, hough_radii)
    accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=1)
    if len(cx) == 0:
        raise ValueError("No iris detected.")
    mask = np.zeros_like(image)
    rr, cc = circle_perimeter(cy[0], cx[0], radii[0])
    mask[rr, cc] = 1
    iris_region = image * mask
    return iris_region

def extract_features(image):
    iris_region = segment_iris(image)
    resized = cv2.resize(iris_region, (64, 64))
    haar = cv2.dct(np.float32(resized))
    flat = haar.flatten()
    threshold = np.median(flat)
    binary_features = (flat > threshold).astype(int)
    return binary_features.tolist()
