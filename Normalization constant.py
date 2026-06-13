import numpy as np
from scipy.integrate import quad

# Define the wavefunctions
'''
psi0 = lambda x: np.exp(-x**2 / 2)
psi1 = lambda x: x * np.exp(-x**2 / 2)
'''

# Define the wavefunctions using regular functions
def psi0(x):
    return np.exp(-x**2 / 2)

def psi1(x):
    return x * np.exp(-x**2 / 2)

# Define the integrands for normalization
def psi0_squared(x):
    return psi0(x)**2

def psi1_squared(x):
    return psi1(x)**2

norm0, _ = quad(psi0_squared, -np.inf, np.inf)
norm1, _ = quad(psi1_squared, -np.inf, np.inf)

'''# Normalization integrals
norm0, _ = quad(lambda x: psi0(x)**2, -np.inf, np.inf)
norm1, _ = quad(lambda x: psi1(x)**2, -np.inf, np.inf)
'''

# Normalization constants
A0 = 1 / np.sqrt(norm0)
A1 = 1 / np.sqrt(norm1)

#print(f"Normalization constant for 0: {A0:.4f}")
#print(f"Normalization constant for 1: {A1:.4f}")

print("Normalization constant for psi0: {:.4f}".format(A0))
print("Normalization constant for psi0: {:.4f}".format(A1))

'''
Output:
Normalization constant for psi0: 0.7511
Normalization constant for psi0: 1.0623
'''