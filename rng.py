import numpy as np

# random number generator -->

rng = np.random.default_rng() # we can also use seed for same rng everytime.

print(rng.integers(low=1, high=101, size=(3, 3))) #least limit is low= , highest limit is high= & size= is to set the size.