import os


def ft_tqdm(lst: range) -> None:
    '''
    This function is a copy of the tqdm function
    It creates a loading bar in your terminal

    :param lst: given lense of the loading bar
    :type lst: range
    '''
    total = len(lst)
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80

    bar_len = max(10, columns - 40)

    for i, elem in enumerate(lst):
        progress = (i + 1) / total
        filled = int(progress * bar_len)
        bar = "[" + ("=" * filled) + ">" + (" " * (bar_len - filled - 1)) + "]"
        percent = int(progress * 100)

        print(f"\r{percent:3d}%|{bar}|{i + 1}/{total}", end="", flush=True)
        yield elem
