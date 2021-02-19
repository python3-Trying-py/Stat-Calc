import math

def sd(p, n):
	"""
	the standard deviation of ^p

	Parameters:
	p (float): probability
	n (int): sample size

	Returns:
	float: σ of ^p
	"""
	return math.sqrt(
		p * (1 - p) /
		n
	)
