from PIL import Image
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

input_image.show()