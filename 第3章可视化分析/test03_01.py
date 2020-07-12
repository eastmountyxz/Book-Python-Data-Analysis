import numpy as np  
import matplotlib.pyplot as plt  
X = np.arange(0,4)
print(X)

#绘制图形
plt.plot(X, X*0.5, label="y=x*0.5")
plt.plot(X, X*1.5, label="y=x*1.5")
plt.plot(X, X*3.0, label="y=x*3.0")
plt.legend()
plt.show() 
