from PIL import Image
import numpy as np


import numpy as np
img=Image.open("D:\\img\\apple.jpg")
imgarray=np.array(img)

print(len(imgarray))


#np.savetxt("D:\\foo_img.csv", imgarray, delimiter=",")

imgarray.tofile('D:\\img\\foo_img.csv',sep=',',format='%10.5f')


#data = np.loadtxt("D:\\foo_img.csv",skiprows=0)

imgarray_read = np.fromfile("D:\\img\\foo_img.csv",sep=",", dtype=np.uint8)



print(len(imgarray_read))

rescaled = (255.0 / imgarray_read.max() * (imgarray_read - imgarray_read.min())).astype(np.uint8)

im = Image.fromarray(rescaled)
im.save('D:\\test_new.png')