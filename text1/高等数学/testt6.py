import torch
import numpy as np

# # a = np.array([1])
# # print(a)
# # print(a.shape)
# # print(a.ndim)

# b = torch.tensor(2)
# print(b)
# print(b.shape)
# print(b.ndim)

# a = np.array([1, 3])
# print(a)
# print(a.shape)
# print(a.ndim)
#
# b = torch.tensor([1, 3])
# print(b)
# print(b.shape)
# print(b.ndim)

a = np.array([[[1, 3],
               [2, 4]],
              [[1, 3],
               [2, 4]]]
             )
print(a)
print(a.shape)
print(a.ndim)

b = torch.tensor([[[1, 3],
               [2, 4]],
              [[1, 3],
               [2, 4]]]
             )
print(b)
print(b.shape)
print(b.ndim)
