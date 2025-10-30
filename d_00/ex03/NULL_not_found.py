def NULL_not_found(object: any) -> int:
	if object == None:
		print(f"Nothing: {object} {type(object)}")
	elif isinstance(object, float) and object != object:
		print(f"Cheese: {object} {type(object)}")
	elif object == 0:
		print(f"Zero: {object} {type(object)}")
	elif object == "":
		print(f"Empty: {object} {type(object)}")
	elif object == False:
		print(f"Fake: {object} {type(object)}")
	else:
		print("Type not found")
		return("1")
	return("0")