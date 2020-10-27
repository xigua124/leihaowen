import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r"C:\Users\hp\Desktop\workspace\text1\高等数学\image\Address.PNG")
image_data = np.array(img)
print(img.mode)
h, w, c = image_data.shape
image_data = image_data.reshape(1, h, 1, w, c)
image_data = image_data.reshape(2, h//2, 2, w//2, c)
image_data = image_data.transpose(0, 2, 1, 3, 4)
image_data = image_data.reshape(4, h//2, w//2, c)
image_all = np.split(image_data, 4, axis=0)
for i, image in enumerate(image_all):
    img = Image.fromarray(image[0])
    img.show()
