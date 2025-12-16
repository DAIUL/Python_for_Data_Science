import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        if (
            not isinstance(family, list)
            or not all(isinstance(x, list) for x in family)
        ):
            raise Exception("family must be a list of list")
        if type(start) is not int or type(end) is not int:
            raise Exception("start and end must be integers")
        row_lenght = {len(x) for x in family}
        if len(row_lenght) != 1:
            raise Exception("all lists must be the same size")

        f_array = np.array(family)
        print(f"My shape is : {f_array.shape}")

        f_array = f_array[start:end]
        print(f"My new shape is : {f_array.shape}")

    except Exception as e:
        print(e)
        return []

    return f_array.tolist()
