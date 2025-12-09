import sys


def sos(s):
    '''
    This function convert a string into morse code and prints it

    :param s: given string to convert
    '''
    MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
        'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
        'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
        'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',

        ' ': '/',
    }

    result = " ".join(MORSE.get(c.upper()) for c in s)
    return print(result)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        for c in sys.argv[1]:
            if c in punctuation_chars:
                raise AssertionError("the arguments are bad")

        sos(sys.argv[1])

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
