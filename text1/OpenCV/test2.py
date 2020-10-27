import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ax = []
# ay = []
# plt.ion()
# for i in range(1000):
#     ax.append(i)
#     ay.append(i**2)
#     plt.clf()
#     plt.plot(ax, ay)
#     plt.pause(0.001)
# plt.ioff()

# x = np.random.normal(0, 1, 100)
# y = np.random.normal(0, 1, 100)
# z = np.random.normal(0, 1, 100)
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(x, y, z)
# plt.show()
x = np.random.randn(20)
y = np.random.randn(20)
x1 = np.random.randn(10)
y1 = np.random.randn(10)
plt.scatter(x, y, s=60, c="green", marker="^", label="like")
plt.scatter(x1, y1, s=60, c='red', marker='o', label='dislike')
plt.legend()
plt.show()
