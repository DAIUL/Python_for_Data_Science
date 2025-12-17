import numpy as np
from PIL import Image


def ft_invert(array):
    '''
    Invert de rgb values of the given array

    :param array: image rgb values
    '''
    try:
        inverted_array = 255 - array

        reverse_img = Image.fromarray(inverted_array)
        reverse_img.show()

        # CONDITIONS CHECK
        # print(f"array shape: {array.shape}")
        # print(f"inverted_array shape: {inverted_array.shape}")
    except Exception as e:
        print(e)
        return None

    return inverted_array


def ft_red(array):
    '''
    Returns the given array keeping only red values

    :param array: image rgb values
    '''
    try:
        red_array = array.copy()
        red_array[:, :, 1] = 0   # G
        red_array[:, :, 2] = 0   # B

        red_image = Image.fromarray(red_array)
        red_image.show()

        # CONDITIONS CHECK
        # print(f"array shape: {array.shape}")
        # print(f"red array shape: {red_array.shape}")

    except Exception as e:
        print(e)
        return None

    return red_array


def ft_green(array):
    '''
    Returns the given array keeping only green values

    :param array: image rgb values
    '''
    try:
        green_array = array.copy()
        green_array[:, :, 0] = 0   # R
        green_array[:, :, 2] = 0   # B

        green_image = Image.fromarray(green_array)
        green_image.show()

        # CONDITIONS CHECK
        # print(f"array shape: {array.shape}")
        # print(f"green array shape: {green_array.shape}")

    except Exception as e:
        print(e)
        return None

    return green_array


def ft_blue(array):
    '''
    Returns the given array keeping only blue values

    :param array: image rgb values
    '''
    try:
        blue_array = array.copy()
        blue_array[:, :, 0] = 0   # R
        blue_array[:, :, 1] = 0   # G

        blue_image = Image.fromarray(blue_array)
        blue_image.show()

        # CONDITIONS CHECK
        # print(f"array shape: {array.shape}")
        # print(f"blue array shape: {blue_array.shape}")

    except Exception as e:
        print(e)
        return None

    return blue_array


def ft_grey(array):
    '''
    Convert the given array into grey values while keeping the same shape

    :param array: image rgb values
    '''
    try:
        grey_array = (
            (array[:, :, 0] / (1 / 0.299)) +
            (array[:, :, 1] / (1 / 0.587)) +
            (array[:, :, 2] / (1 / 0.114))
        ).astype(np.uint8)
        grey_rgb = np.stack([grey_array, grey_array, grey_array], axis=2)

        grey_img = Image.fromarray(grey_rgb)
        grey_img.show()

        # CONDITIONS CHECK
        # print(f"array shape: {array.shape}")
        # print(f"grey_array shape: {grey_rgb.shape}")

    except Exception as e:
        print(e)
        return None

    return grey_rgb
