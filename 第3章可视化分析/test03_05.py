import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(200)
y = np.random.randn(200)
print(x[:10])
print(y[:10])
plt.scatter(x, y)
plt.show()
