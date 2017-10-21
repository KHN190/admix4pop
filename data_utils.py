import numpy as np

def load_mixture(fname):
	with open(fname) as f:
		return np.array([float(_) for _ in f.read().split()])

def load_populations(fname):
	pop_names = []
	populations = []
	for line in open(fname):
		data = line.split()
		pop_names.append(data[0])
		populations.append(np.array([float(_) for _ in data[1:]]))
	return pop_names, populations
