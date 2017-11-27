
from numpy import genfromtxt
data = genfromtxt('D:\\output_file.csv', delimiter=',')

from PIL import Image
import numpy as np

#data = np.random.random((100,100))

#Rescale to 0-255 and convert to uint8
rescaled = (255.0 / data.max() * (data - data.min())).astype(np.uint8)

im = Image.fromarray(rescaled)
im.save('D:\\test.png')



#import matplotlib.pyplot as plt
#import numpy as np
#plt.imshow(rescaled)
#plt.savefig('D:\\img3.jpg')