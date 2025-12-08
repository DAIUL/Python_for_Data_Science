import sys

def filterstring(s, n):
	lst = s.split(" ")
	check = lambda x: len(x) >= n
	result = [x for x in lst if check(x)]
	return print(result)

def main():
	try:
		if len(sys.argv) != 3:
			raise AssertionError("the arguments are bad")
		if not sys.argv[2].isdigit():
			raise AssertionError("the arguments are bad")
		
		punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

		for c in sys.argv[1]:
			if c in punctuation_chars:
				raise AssertionError("Strings must not contain any special characters (punctuation or invisible)")
			
		filterstring(sys.argv[1], int(sys.argv[2]))

	except AssertionError as e:
		print(f"AssertionError: {e}")

if __name__ == '__main__':
	main()