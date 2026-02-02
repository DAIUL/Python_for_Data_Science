import pandas as pd


def load(path: str):
    '''
    This function takes a path as argument,
    writes the dimensions of the data set
    and returns it

    :param path: csv file path
    :type path: str
    :return: Dataset
    :rtype: Any
    '''
    try:
        dataset = pd.read_csv(path)
        dataset = dataset.set_index('country')
        print(f"Loading dataset of dimensions {dataset.shape}")
    except Exception as e:
        print(e)
        return None

    return dataset
