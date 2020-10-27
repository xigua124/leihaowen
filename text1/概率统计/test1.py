import torch
import matplotlib.pyplot as plt
from torch import optim
from torch import nn

xs = torch.arange(-1.0, 1.0, 0.01)
print(xs.shape)
xs = xs.unsqueeze(1)
ys = xs**3 + torch.rand(200, 1)/3 + 4


class net(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(1, 32))
        self.b1 = nn.Parameter(torch.randn(32))
        self.w2 = nn.Parameter(torch.randn(32, 24))
        self.b2 = nn.Parameter(torch.randn(24))
        self.w3 = nn.Parameter(torch.randn(24, 12))
        self.b3 = nn.Parameter(torch.randn(12))
        self.w4 = nn.Parameter(torch.randn(12, 1))
        self.b4 = nn.Parameter(torch.randn(1))

    def forward(self, x):
        h1 = torch.sigmoid(x.matmul(self.w1) + self.b1)
        h2 = torch.sigmoid(h1.matmul(self.w2) + self.b2)
        h3 = torch.sigmoid(h2.matmul(self.w3) + self.b3)
        h4 = (h3.matmul(self.w4) + self.b4)
        return h4


Net = net()
opt = optim.Adam(Net.parameters(), lr=0.01)
plt.ion()
for epoch in range(20000):
    h = Net(xs)
    print(h.shape)
    loss = torch.sum((ys - h)**2)
    opt.zero_grad()
    loss.backward()
    print("loss=", loss)
    opt.step()
    if epoch % 5 == 0:
        plt.cla()
        plt.plot(xs, ys, '.')
        plt.plot(xs, h.detach().numpy())
        plt.pause(0.01)
plt.ioff()
plt.show()
