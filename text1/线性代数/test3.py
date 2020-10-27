import torch

a = torch.tensor([[1, 2],
                 [3, 4]], dtype=float)
print(a)
print(torch.eig(a, eigenvectors=True))

