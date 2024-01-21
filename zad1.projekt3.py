import numpy as np
import matplotlib.pyplot as plt

K = 100000  
r = 0.4 
t0 = 75  
x0 = 5  

def gompertz_eq(t, x):
    return r * x * np.log(K / x)

def euler(h, t, x):
    for i in range(1, len(t)):
        x[i] = x[i - 1] + h * gompertz_eq(t[i - 1], x[i - 1])
    return x

h = 1
t = np.arange(t0, t0 + 50, h)

x_gompertz = np.zeros(len(t))
x_gompertz[0] = x0

x_gompertz = euler(h, t, x_gompertz)

x_verhulst = K / (1 + ((K / x0) - 1) * np.exp(-r * (t - t0)))

plt.plot(t, x_gompertz, label='Gompertz')
plt.plot(t, x_verhulst, label='Verhulst')
plt.xlabel('Czas')
plt.ylabel('Objętość guza')
plt.legend()
plt.show()
