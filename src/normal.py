import scipy.stats as st

def zscore(xbar, mu, sigma):
	"""
	returns the z-score from the given parameters

	Parameters:
	xbar (float): statistic
	mu (float): parameter
	sigma (float): standard deviation of parameter

	Returns:
	float: z-score (how many standard deviations statistic is from parameter)
	"""
	diff = xbar - mu
	return diff / sigma

def cdf(z):
	"""
	returns the probability of being less than or equal to a given z score on a normal distribution

	Parameters:
	z (float): z-score

	Returns:
	float: probability
	"""
	return st.norm.cdf(z)
