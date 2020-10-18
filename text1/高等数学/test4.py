import random
import matplotlib.pyplot as plt

_x = [i/100 for i in range(100)]
_y = [3*e + 4 + random.random()/10 for e in _x]
w, b = random.random(), random.random()

# plt.plot(x, y, ".")
# plt.scatter(x, y)
# plt.show()
plt.ion()
for i in range(30):
    for x, y in zip(_x, _y):
        z = w*x + b
        loss = (z - y)**2
        dw = 2*(z - y)*x
        db = 2*(z - y)
        w = w - 0.01*dw
        b = b - 0.01*db
        print(w, b, loss)
    v = [w*e + b for e in _x]
    plt.cla()
    plt.plot(_x, v)
    plt.plot(_x, _y, '.')
    plt.pause(0.1)
plt.ioff()
plt.show()
