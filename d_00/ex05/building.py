import sys

def main():
	try:
		if len(sys.argv) > 2:
			raise AssertionError("more than one argument is provided")
		if len(sys.argv) == 2:
			str = sys.argv[1]
		else:
			try:
				str = input("What is the text to count?\n")
			except EOFError:
				str = ""

		punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

		digit = sum(1 for c in str if c.isdigit())
		up_case = sum(1 for c in str if c.isupper())
		lo_case = sum(1 for c in str if c.islower())
		spaces = sum(1 for c in str if c.isspace())
		ponct_mark = sum(1 for c in str if c in punctuation_chars)
	
		print(f"the text contains {len(str)} characters:")
		print(f"{up_case} upper letters")
		print(f"{lo_case} lower letters")
		print(f"{ponct_mark} ponctuation marks")
		print(f"{spaces} spaces")
		print(f"{digit} digits")

	except AssertionError as e:
		print(f"Assertion error : {e}")

if __name__ == "__main__":
	main()