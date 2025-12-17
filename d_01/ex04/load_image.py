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

        width, height = img.size
        left = (width - 150) // 2
        top = height - 675
        right = left + 400
        bottom = top + 400

        croppedImg = img.crop((left, top, right, bottom))
        grayCroppedImg = croppedImg.convert('L')

        grayCroppedImg.show()

        arr = np.array(grayCroppedImg)
        preciseArr = arr[..., np.newaxis]

        print(f"The shape of the image is: {preciseArr.shape} or {arr.shape}")
        print(preciseArr)
        return arr

    except FileNotFoundError:
        print("Error: file not found")
        return None

    except OSError:
        print("Error: unsupported or corrupted file")
        return None
