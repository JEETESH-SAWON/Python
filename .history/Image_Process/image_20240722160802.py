from PIL import Image
from matplotlib import pyplot as plt
# input image from Directory
input_image = Image.open("image/test.jpg")
# create pixel map from image or dummy pixel frame
pixel_map = input_image.load()
# extract height and width from input_image
width,height = input_image.size
# formula for grayscale G = (0.299R + 0.587G + 0.114B)
# loop for iterating input_image and extract pixel value
for i in range(width):
    for j in range(height):
        # extract color value from a pixel
        r, g, b = input_image.getpixel((i,j))
        grayscale = (0.299*r + 0.587*g + 0.114*b)
        # set computed grayscale value to pixel_map
        pixel_map[i,j] = (int(grayscale), int(grayscale), int(grayscale))
# save modified image
input_image.save("image/modifyImage.jpg")
# create subplot of 1 row 2 column of 10inch width 5inch tall
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# ploting both image in both ax1 ax2
ax1.imshow(input_image)
ax1.set_title('Original Image')
ax1.axis('off')  # Hide the axes

ax2.imshow("image/modifyImage.png")
ax2.set_title('Modified Image')
ax2.axis('off')  # Hide the axes
plt.show()
