import imageio as load_image


def main():
    """
    This function read an image and print the text in the image
    """

# read an image
    my_image = load_image.v3.imread('resources/code.png')
    height_weight = my_image.shape
    list_of_numbers \
        = [height_index for weight_index in range(0, height_weight[1]) for height_index in range(0, height_weight[0]) if my_image[height_index, weight_index] != 255]

    for number in list_of_numbers:
        print(chr(number), end="")


if __name__ == '__main__':
    main()

