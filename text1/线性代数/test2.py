from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\hp\Desktop\workspace\text1\高等数学\image\Address.PNG")
img_data = np.array(img)

# print(img_data.shape)
# img_data = img_data.transpose(1, 0, 2)
# img = Image.fromarray(img_data)
# img.show()
img_data = img_data.transpose(2, 0, 1)
print(img_data)
