from scipy.optimize import fsolve
import numpy as np

# define the function
def func(k):
    P0 = 250
    M = 3900
    P10 = 275
    return P10 - M / (1 + ((M/P0) - 1) * np.exp(-10 * k))

# initial guess for k
k0 = 0.01

# use fsolve to find k
k = fsolve(func, k0)

print("The value of k is: {:.8f}".format(k[0]))
