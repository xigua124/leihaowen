import torch
from torch import optim
import matplotlib.pyplot as plt

xs = torch.arange(0.01, 1.0, 0.01)
ys = 3 * xs + 4 + torch.rand(99)


class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self, x):
        return x*self.w + self.b


if __name__ == '__main__':
    line = Line()
    opt = optim.SGD(line.parameters(), lr=0.03)
    plt.ion()
    for i in range(30):
        for x, y in zip(xs, ys):
            z = line(x)
            loss = (z - y)**2
            opt.zero_grad()
            loss.backward()
            opt.step()
            plt.cla()
            plt.plot(xs, ys, ".")
            print("w: " + str(line.w.item()) + " b: " + str(line.b.item()) + " loss: " + str(loss.item()))
            v = [line.w * e + line.b for e in xs]
            plt.plot(xs, v)
            plt.pause(0.01)
    plt.ioff()
    plt.show()
