def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args, **kwargs):
			nonlocal count
			nonlocal limit
			if count >= limit:
				print(f"Error : {function} call too many times")
			else:
				function(*args, **kwargs)
			count += 1
			return None
		return limit_function
	return callLimiter