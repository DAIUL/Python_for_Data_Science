import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(path: str):
    '''
    Take the path of an image then turn it grayscale and zoom in
    
    :param path: image path
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

        arr = np.array(grayCroppedImg)
        preciseArr = arr[..., np.newaxis]
        
        plt.imshow(arr, cmap='gray')
        plt.xticks(np.arange(0, arr.shape[1], 50))
        plt.yticks(np.arange(0, arr.shape[0], 50))

        plt.show()
        
        print(f"New shape after slicing: {preciseArr.shape} or {arr.shape}")
        return preciseArr


    except FileNotFoundError:
        print("Error: file not found")
        return None

    except OSError:
        print("Error: unsupported or corrupted file")
        return None


def main():

    print(ft_load('Animal.jpeg'))
    print(zoom('Animal.jpeg'))
    return


if __name__ == '__main__':
    main()