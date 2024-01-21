import numpy as np
import matplotlib.pyplot as plt

n1 = [3]
n2 = [4]

e1 = 1.25
y1 = 0.5
h1 = 0.1
e2 = 0.5
y2 = 0.2
h2 = 0.2
h = 0.001
t = np.arange(0, 10, 0.001)

for _ in range(len(t)):
        new_n1 = n1[-1] + h*((e1-y1*(h1*n1[-1]+h2*n2[-1]))*n1[-1])
        new_n2 = n2[-1] + h*((e2-y2*(h1*n1[-1]+h2*n2[-1]))*n2[-1])
        n1.append(new_n1)
        n2.append(new_n2)


n3 = [3]
n4 = [4]

e3 = 5
y3 = 4
h3 = 1
e4 = 5
y4 = 8
h4 = 4
h = 0.001
t = np.arange(0, 10, 0.001)

for _ in range(len(t)):
        new_n3 = n3[-1] + h*((e3-y3*(h3*n3[-1]+h4*n4[-1]))*n3[-1])
        new_n4 = n4[-1] + h*((e4-y4*(h3*n3[-1]+h4*n4[-1]))*n4[-1])
        n3.append(new_n3)
        n4.append(new_n4)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(t, n1[:-1], label='ofiara')
ax1.plot(t, n2[:-1], label='drapieżnik')
ax1.set_title('Pierwszy zestaw danych')
ax1.legend()

ax2.plot(t, n3[:-1], label='ofiara')
ax2.plot(t, n4[:-1], label='drapieżnik')
ax2.set_title('Drugi zestaw danych')
ax2.legend()

plt.show()
