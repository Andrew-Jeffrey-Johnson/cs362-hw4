
def ave (list=[], *args):
	total = 0
	for x in list:
		total += x
	if len(list)==0:
		return 0
	else:
		return (total / len(list))