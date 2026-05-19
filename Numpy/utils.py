from PIL import Image
import numpy as np


def load_image(path):
    image = Image.open(path)
    return np.array(image)


def save_image(array, path):
    image = Image.fromarray(array.astype(np.uint8))
    image.save(path)


def show_image(array, title="Image"):
    import matplotlib.pyplot as plt
    plt.imshow(array)
    plt.title(title)
    plt.axis("off")
    plt.show()
