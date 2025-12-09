import sys


def filterstring(s, n):
    '''
    This function prints the given string with words how have
    even or more caracters than the given number only

    :param s: base string
    :param n: min limit of word lense
    '''
    lst = s.split(" ")
    return [w for w in lst if (lambda x: len(x) >= n)(w)]


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")

        punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        for c in sys.argv[1]:
            if c in punctuation_chars:
                raise AssertionError(
                    "Strings must not contain any special characters"
                    "(punctuation or invisible)")

        filterstring(sys.argv[1], int(sys.argv[2]))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
