import itertools

def flatten(nested_array):
    return list(itertools.chain(*nested_array))
