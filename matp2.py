import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(10, 30, 10)
y = x*x + 100

ax.plot(x, y, label='$y=x^{2}+100$')
ax.plot(x, 1.2*y, linewidth=3, linestyle='--', color='red', label='$y=1.2x^{2}+100$')
ax.plot(x, 1.2*y, 'o', color='black')

ax.set_xlabel('x-axis', fontsize=20)
ax.set_ylabel('y-axis', fontsize=20)
ax.set_xlim(10., 20.)
ax.set_ylim(200., 600.)

ax.legend(handlelength=3, loc='upper left')
ax.grid(True)

fig.savefig('matp2.pdf')
fig.savefig('matp2.png')
