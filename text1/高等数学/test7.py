from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image/Address.PNG")
# img.show()
img_data = np.array(img)
# print(img_data)
print(img_data.shape)
print(img_data.ndim)
r, g, b, c = img.split()
image = Image.merge("RGB", (r, g.point(lambda i: i == i*0), b.point(lambda i: i == i*0)))
# r.show()
# g.show()
# b.show()
# r = np.array(r)
# print(r)
# print(r.shape)
# image.show()
image = image.rotate(90)
plt.imshow(image)
plt.show()
