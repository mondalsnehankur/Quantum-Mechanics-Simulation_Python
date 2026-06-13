import numpy as np
import matplotlib.pyplot as plt

def josephson_simulation(V_func, t_end=10, dt=0.01, phi0=np.pi/2, Ic=1):
    times = np.arange(0, t_end, dt)
    phi = phi0
    I_values = []

    for t in times:
        V = V_func(t)
        dphi_dt = V
        phi += dphi_dt * dt
        I = Ic * np.sin(phi)
        I_values.append(I)

    return times, I_values

# (i) Constant voltage V = 5
V_constant = lambda t: 5
t1, I1 = josephson_simulation(V_constant)
plt.plot(t1, I1,'.-',c='green',label='V = 5')
#plt.title("Josephson Current with V = 5")
plt.xlabel("$Time$")
plt.ylabel("$I(t)$")
plt.grid(True)

# (ii) Sinusoidal voltage V(t) = 5cos(t)
V_sinusoidal = lambda t: 5 * np.cos(t)
t2, I2 = josephson_simulation(V_sinusoidal)
plt.plot(t2, I2,'.-',c='red',label='V(t) = 5cos(t)')
#plt.title("Josephson Current with V(t) = 5cos(t)")
plt.xlabel("$Time$")
plt.ylabel("$I(t)$")
plt.legend(loc='best')

plt.axvline(0,c='k')
plt.axhline(0,c='k',lw='1.2')
plt.grid(True)

plt.show()
