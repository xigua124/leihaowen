import torch
import numpy as np


a = torch.tensor(3)
print(a)
print(type(a))

b = torch.tensor([[1, 2],
                  [3, 4]])
print(type(b))
c = np.array([[1, 2],
              [3, 4]])
print((type(c)))
e = torch.from_numpy(c)
print(type(e))
f = b.numpy()
print(type(f))
