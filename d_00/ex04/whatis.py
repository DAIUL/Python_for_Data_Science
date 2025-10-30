import sys

def odd_or_even():
	try:
		if len(sys.argv) == 1:
			return		
		if len(sys.argv) != 2:
			raise AssertionError("more than one argument is provided")
		
		if not sys.argv[1].lstrip("-").isdigit():
			raise AssertionError("argument is not an integer")
		nb = int(sys.argv[1])
		
		if nb % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	
	except AssertionError as e:
		print(f"Assertion error : {e}")

odd_or_even()