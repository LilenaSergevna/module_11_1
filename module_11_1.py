import random

import matplotlib.pyplot as plt
import numpy as np


mat= np.random.randint(0,20, size=10)

print(np.sort(mat))
print(np.min(mat))
print(np.max(mat))

mat2= np.ones((3,2))

print(mat2)


# plot
fig, ax = plt.subplots()
x=[]
for i in range(10):
    x.append(i**2)
print(x)
ax.plot(x, label='**2')

plt.legend()
plt.show()

