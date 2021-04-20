import numpy as np
def name_generator():
	with open('nouns.txt') as f: nouns=f.readlines()
	with open('adjectives.txt') as f: adj=f.readlines()
	nouns,adj=[[x.strip() for x in dic] for dic in [nouns,adj]]
	m='the '+' '.join([np.random.choice(d) for d in [adj,nouns]])
	return m

print(name_generator())




