import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    '''
    This function converts two lists of heights et weights
    into a list of BMI values

    :param height: list of height values
    :param weight: list if weight values
    :return: list of the BMI values
    '''
    try:
        if (
            not all(isinstance(x, (int, float)) for x in height)
            or not all(isinstance(x, (int, float)) for x in weight)
        ):
            raise Exception("parameters must be list of int or float only")

        h = np.array(height, dtype=float)
        w = np.array(weight, dtype=float)

        if h.shape != w.shape:
            raise Exception("lists must be the same size")
        if np.any(h == 0):
            return Exception("height cannot be 0")

    except Exception as e:
        print(e)
        return []

    return (w / (h * h)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    This function returns a list of True/False values
    depending on if they're above the given limit or not

    :param bmi: list of BMI values
    :param limit: min limit of BMI value to be considered True
    :return: list of True/False values
    '''
    return (np.array(bmi) >= limit).tolist()
