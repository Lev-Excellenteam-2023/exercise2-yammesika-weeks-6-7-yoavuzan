import imageio as iio

# read an image
im = iio.v3.imread('resources/code.png')
height_weight = im.shape
list_of_numbers = []
for j in range(0, height_weight[1]):
    for i in range(0, height_weight[0]):
        pixel_value = im[i, j]
        if pixel_value != 255:
            list_of_numbers.append(i)

for number in list_of_numbers:
    print(chr(number), end="")



