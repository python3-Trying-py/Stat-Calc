def mean(data):
	"""
	returns the mean of the data set passed in

	Parameters:
	data (int/float[]): data set to use for calculation

	Returns:
	float: the average of the data
	"""
	total = sum(data)
	return total / len(data)
