"""the name generator is a function that
generates a name from an adjective and a noun"""
import numpy as np


def name_generator():
    """returns a random name constructed from an adjective and a noun"""
    with open('nouns.txt') as ns_file:
        nouns = ns_file.readlines()
    with open('adjectives.txt') as ad_file:
        adj = ad_file.readlines()
    nouns, adj = [[x.strip() for x in dic] for dic in [nouns, adj]]
    the_name = 'the '+' '.join([np.random.choice(d) for d in [adj, nouns]])
    return the_name


print(name_generator())
