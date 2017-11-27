from PIL import Image
import numpy as np


import numpy as np
img=Image.open("D:\\img\\apple.jpg")
face=np.array(img)

print("shape:"+str(face.shape),"type:"+ str(face.dtype))

face.tofile('D:\\img\\face.raw') # Create raw file
face_from_raw = np.fromfile('D:\\img\\face.raw', dtype=np.uint8)
face_from_raw.shape = (225, 225, 3)
print(type(face_from_raw))

im = Image.fromarray(face_from_raw)
im.save('D:\\img\\test.jpg')

#f = misc.face(gray=True)  # retrieve a grayscale image
#import matplotlib.pyplot as plt
#plt.imshow(f, cmap=plt.cm.gray)



#You could use ndarray.dumps() to pickle it to a string then write it to a BLOB field? Recover it using numpy.loads()

