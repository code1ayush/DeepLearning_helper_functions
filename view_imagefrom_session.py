import matplotlib.image as mpimg
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt

pizza1=mpimg.imread("pizza1.jpg")
plt.imshow(pizza1)
plt.axis(False)