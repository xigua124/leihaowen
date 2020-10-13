import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0.1, 10, 0.1)  # 设定x的取值
y = np.tile(np.arange([3]), x.shape)
plt.plot(x, y)
plt.show()