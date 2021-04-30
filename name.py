
def name (first = None, last = None):
	if first is None:
		if last is None:
			return ""
		else:
			return last + ""
	else: 
		if last is None:
			return first + ""
		else:
			return first + " " + last + ""
	