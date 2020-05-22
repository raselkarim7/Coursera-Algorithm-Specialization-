import matplotlib.pyplot as plt
import numpy as np
import math


n = np.linspace(1, 10 ** 124)
plt.plot(n, n ** .1, label="n^.1")
plt.plot(n, np.log(n) ** 5, label="(log n)^5")
plt.legend(loc='upper left')
plt.show()
