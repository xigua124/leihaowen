import numpy as np
import matplotlib.pyplot as plt
import torch


x = np.arange(-10, 10, 0.1)  # 设定x的取值
y = np.tile(np.array([3]), x.shape)
y1 = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
plt.plot(x, y1)
plt.show()
