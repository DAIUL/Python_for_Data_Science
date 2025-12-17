import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def rotate(array: np.array):
    '''
    Take the array of an image and transpose it
    then displays it

    :param array: image array
    '''
    try:
        cols, rows = array.shape
        transposed_array = np.zeros((rows, cols), dtype=array.dtype)

        for i in range(rows):
            for j in range(cols):
                transposed_array[i, j] = array[j, i]

        plt.imshow(transposed_array, cmap='gray')
        plt.xticks(np.arange(0, transposed_array.shape[1], 50))
        plt.yticks(np.arange(0, transposed_array.shape[0], 50))

        plt.show()

        print(f"New shape after Transpose: {transposed_array.shape}")
        return transposed_array

    except FileNotFoundError:
        print("Error: file not found")
        return None

    except OSError:
        print("Error: unsupported or corrupted file")
        return None


def main():

    print(rotate(ft_load('Animal.jpeg')))
    return


if __name__ == '__main__':
    main()
