import math


def ft_mean(values: tuple) -> float:
    mean_value = sum(values) / len(values)
    return mean_value


def ft_median(values: tuple) -> float:
    values = sorted(values)
    if len(values) % 2 == 0:
        median_mid = (values[(len(values) // 2) - 1], values[len(values) // 2])
        median_value = sum(median_mid) / 2
    else:
        median_value = values[len(values) // 2]
    return median_value


def ft_quartile(values: tuple) -> list:
    values = sorted(values)
    mid = len(values) // 2

    if len(values) % 2 == 0:
        lower_values = values[:mid]
        upper_values = values[mid:]
    else:
        lower_values = values[:mid+1]
        upper_values = values[mid:]

    q1_value = ft_median(lower_values)
    q3_value = ft_median(upper_values)
    return [q1_value, q3_value]


def ft_var(values: tuple) -> float:
    mean = ft_mean(values)
    var = sum([(x - mean)**2 for x in values]) / len(values)
    return var


def ft_std(values: tuple) -> float:
    std = math.sqrt(ft_var(values))
    return std


def ft_statistics(*args, **kwargs) -> None:
    if not args:
        print('ERROR')
        return None

    if not all(isinstance(x, (int, float)) for x in args):
        print('ERROR')
        return None

    operations = {
        'mean': ft_mean,
        'median': ft_median,
        'quartile': ft_quartile,
        'std': ft_std,
        'var': ft_var
    }

    for value in set(kwargs.values()):
        if value in operations:
            print(f"{value} : {operations[value](args)}")
        else:
            print('ERROR')

    return None