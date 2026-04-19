import numpy as np

ages = np.array([[20, 36, 16, 44, 56, 20],
                  [34, 55, 78, 90, 41, 19]])

#filtering as follows -->

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 50)]
seniors = ages[ages >= 50]

print(teenagers)

print(adults)

print(seniors)
