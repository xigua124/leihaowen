import torch
from torch import optim
import matplotlib.pyplot as plt

xs = torch.arange(0.01, 1, 0.01)
ys = 3 * xs + 4 + torch.rand(99)


class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.rand(1))  # 定义一个可学习的变量
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self, x):
        return self.w * x + self.b


if __name__ == '__main__':
    print("hello")
    line = Line()
    #  opt = torch.optim.SGD(line.parameters(), lr=0.1)
    opt = torch.optim.Adam(line.parameters(), lr=0.1)
    plt.ion()
    for epoch in range(30):
        for _x, _y in zip(xs, ys):
            z = line(_x)
            loss = (z - _y)**2
            opt.zero_grad()  # 清空梯度
            loss.backward()  # 前向计算
            opt.step()  # 更新参数
            print(line.w.item(), line.b.item())
            v = [line.w * e + line.b for e in xs]
            plt.cla()
            plt.plot(xs, ys, ".")
            plt.plot(xs, v)
            plt.pause(0.01)
    plt.ioff()
    plt.show()
