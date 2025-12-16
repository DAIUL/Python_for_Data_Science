import numpy as np
from PIL import Image


def ft_load(path: str):
    '''
    This function takes a path to an image,
    convert it into an array of rgb values for each of it's pixels
    and prints it

    :param path: image's path
    :return: array
    '''
    try:
        img = Image.open(path)
        img = img.convert('RGB')
        arr = np.array(img)

        print(f"The shape of image is: {arr.shape}")
        return arr

    except FileNotFoundError:
        print("Error: file not found")
        return None

    except OSError:
        print("Error: unsupported or corrupted file")
        return None
