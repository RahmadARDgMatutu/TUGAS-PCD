import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# import numpy
# import matplotlib.pyplot as plt
img = cv2.imread('mad.jpeg')
img = mpimg.imread('mad.jpeg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()