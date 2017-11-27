from PIL import Image
import numpy as np
img=Image.open("D:\\apple.jpg")
imgarray=np.array(img)

print(len(imgarray))


#np.savetxt("D:\\foo_img.csv", imgarray, delimiter=",")

imgarray.tofile('D:\\foo_img.csv',sep=',',format='%10.5f')

#data = np.random.random((100,100))

#Rescale to 0-255 and convert to uint8
rescaled = (255.0 / imgarray.max() * (imgarray - imgarray.min())).astype(np.uint8)

im = Image.fromarray(rescaled)
im.save('D:\\test.png')