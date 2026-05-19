import numpy as np 

def grayscale(image):
    gray = (
        0.299 * image[:, :, 0] +
        0.587 * image[:, :, 1] +
        0.114 * image[:, :, 2]
    )
    return gray

def negative(image):
    return 255 - image

def brightness(image, value=50):
    bright = image + value
    return np.clip(bright, 0, 255)
