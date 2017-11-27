from skimage import data, io, filters

image = data.coins()
print(image)
# ... or any other NumPy array!
edges = filters.sobel(image)
print(edges)
io.imshow(edges)
io.show()