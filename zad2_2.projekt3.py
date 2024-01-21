import numpy as np
import matplotlib.pyplot as plt

n1_1 = [4]
n2_1 = [8]
n1_2 = [8]
n2_2 = [8]
n1_3 = [12]
n2_3 = [8]

e1 = 0.8
y1 = 1.0
h1 = 0.3
e2 = 0.4
y2 = 0.5
h2 = 0.4
h = 0.001
t = np.arange(0, 50, 0.0001)

for _ in range(len(t)):
        new_n1_1 = n1_1[-1] + h*((e1-y1*(h1*n1_1[-1]+h2*n2_1[-1]))*n1_1[-1])
        new_n2_1 = n2_1[-1] + h*((e2-y2*(h1*n1_1[-1]+h2*n2_1[-1]))*n2_1[-1])
        new_n1_2 = n1_2[-1] + h*((e1-y1*(h1*n1_2[-1]+h2*n2_2[-1]))*n1_2[-1])
        new_n2_2 = n2_2[-1] + h*((e2-y2*(h1*n1_2[-1]+h2*n2_2[-1]))*n2_2[-1])
        new_n1_3 = n1_3[-1] + h*((e1-y1*(h1*n1_3[-1]+h2*n2_3[-1]))*n1_3[-1])
        new_n2_3 = n2_3[-1] + h*((e2-y2*(h1*n1_3[-1]+h2*n2_3[-1]))*n2_3[-1])
        n1_1.append(new_n1_1)
        n2_1.append(new_n2_1)
        n1_2.append(new_n1_2)
        n2_2.append(new_n2_2)
        n1_3.append(new_n1_3)
        n2_3.append(new_n2_3)


gradient = np.meshgrid(np.arange(0, 14, 0.5), np.arange(0, 10, 0.5))
n1_1prim =(e1 - y1*(h1*gradient[0]+h2*gradient[1])*gradient[0])
n2_1prim =(e2 - y2*(h1*gradient[0]+h2*gradient[1])*gradient[1])
n1_2prim =(e1 - y1*(h1*gradient[0]+h2*gradient[1])*gradient[0])
n2_2prim =(e2 - y2*(h1*gradient[0]+h2*gradient[1])*gradient[1])
n1_3prim =(e1 - y1*(h1*gradient[0]+h2*gradient[1])*gradient[0])
n2_3prim =(e2 - y2*(h1*gradient[0]+h2*gradient[1])*gradient[1])

plt.plot(n1_1[0:-1], n2_1[0:-1], label = "1:2 ofiara-drapieżnik")
plt.plot(n1_2[0:-1], n2_2[0:-1], label = "1:1 ofiara-drapieżnik")
plt.plot(n1_3[0:-1], n2_3[0:-1], label = "3:2 ofiara-drapieżnik")
plt.quiver(gradient[0], gradient[1], n1_1prim, n2_1prim, color='gray', alpha=1)
plt.quiver(gradient[0], gradient[1], n1_2prim, n2_2prim, color='gray', alpha=1)
plt.quiver(gradient[0], gradient[1], n1_3prim, n2_3prim, color='gray', alpha=1)
plt.legend()
plt.show()
