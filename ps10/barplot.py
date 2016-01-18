import numpy as np
import matplotlib.pylab as plt

mu, sigma = 2, 0.5

v = np.random.normal( mu , sigma , 1000000 )

plt.hist( v , bins=500 )
plt.show()
