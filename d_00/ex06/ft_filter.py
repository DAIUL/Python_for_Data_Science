import sys


def ft_filter(function, iterable):
    '''
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true.
    '''
    if function is None:
        function = bool
    result = [x for x in iterable if function(x)]
    for x in result:
        yield x


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError(
                "Usage: python ft_filter.py [you function] [your iterable]"
                )
        else:
            ft_filter(sys.argv[1], sys.argv[2])
    except AssertionError as e:
        print(e)

    return


if __name__ == '__main__':
    main()
