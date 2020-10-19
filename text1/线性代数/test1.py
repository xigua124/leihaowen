import numpy as np
import torch

# a = np.array([[1, 2],
#               [3, 4]])
# print(np.linalg.det(a))
#
# b = torch.from_numpy(a).float()
# print(b.det())

# a = torch.tensor([[1, 2],
#                   [3, 4]])
#
# b = torch.tensor([[2, 1],
#                   [4, 3]])
# print(torch.matmul(a, b))
# print(a@b)
# a = a.numpy()
# b = b.numpy()
# print(a.dot(b))
# print(np.dot(a, b))

# a = torch.rand(1, 4, 5, 3)
# b = torch.rand(1, 4, 3, 2)
# c = torch.matmul(a, b)
# print(c.shape)

# a = torch.tensor([[1, 2],
#                   [3, 4],
#                   [5, 6]])
# print(a.shape)
# a = a.t()
# print(a.shape)
# a = a.permute(1, 0)
# print(a.shape)
# a = torch.rand(1, 4, 5, 3)
# a = a.permute(2, 1, 0, 3)
# print(a.shape)

a = np.arange(60).reshape(1, 4, 5, 3)
print(a.shape)
a = a.transpose(2, 1, 0, 3)
print(a.shape)
