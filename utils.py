import cv2
import os

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

def validate_image(path):
    ext = os.path.splitext(path)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Invalid file format {ext}. Allowed: {ALLOWED_EXTENSIONS}")
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Unable to read image. Check the file.")
    return img
