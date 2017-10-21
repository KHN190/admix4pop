import numpy as np
import scipy.optimize as optimize

def likelihood(feats, pops, frac):
	return - np.sum(np.log(np.abs([feats - pop * w for pop, w in zip(pops, frac)])))

def estimate(mix_pop, pops, tol):
	k_pop = len(pops)
	assert k_pop > 1
	assert mix_pop.shape[0] == pops[0].shape[0]
	# fractions should be in [0, 1] and sum up to 1
	constraints = ({'type': 'eq', 'fun': lambda af: 1 - np.sum(af)})
	bounds = tuple((0, 1) for _ in range(k_pop))
	# uniformly distributed at initiation
	initial_guess = np.ones(k_pop) / k_pop
	# create likelihood function
	likelihood_func = lambda af: likelihood(mix_pop, pops, af)

	return optimize.minimize(
		likelihood_func,
		initial_guess,
		bounds=bounds,
		constraints=constraints,
		tol=tol).x
