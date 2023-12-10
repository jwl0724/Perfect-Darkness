import PIL
from PIL import Image
import os


DARKEN_FACTOR = 0.3
PIXELATION_FACTOR = 60
IMG_FILE_NAME = 'example.jpg'


def print_process(function):
    """
    Decorator for image processing that prints the process the program is current at
    """
    def wrap_print(*args, **kwargs):
        """
        Wrap print messages for function process

        This function prints a start message before the function begins its process, and a finished message after
        the function has finished its process

        :param args: Positional arguments passed into the decorator function
        :param kwargs: Keyword arguments passed into the decorator function
        :postcondition: A start and finish message will be printed onto terminal
        """
        print(f'{function.__name__} the image...')
        processed_item = function(*args, **kwargs)
        print(f'Image has now {function.__name__}')
        return processed_item
    return wrap_print


@print_process
def darken(img, pixels, darken_factor: float) -> None:
    """
    Darken image

    This function darkens a given file by an amount determined by the darken_factor parameter, where a factor
    closer to 0 equates to a darker image.

    :param img: A PIL image class that contains the image file data
    :param pixels: A PixelAccess object that represents the pixels of the given image file
    :param darken_factor: A float between 0 and 1 that determines how dark the image will be
    :precondition: All parameters must be the correct types
    :postcondition: All pixels within the given image will be darkened
    """
    for x_coord in range(img.size[0]):
        for y_coord in range(img.size[1]):
            new_pixels = tuple([int(num * darken_factor) for num in pixels[x_coord, y_coord]])
            pixels[x_coord, y_coord] = new_pixels


@print_process
def pixelate(img, pixelation_factor: int) -> object:
    """
    Pixelate image

    This function pixelates an image by an amount determined by the pixelation_factor parameter, where a smaller
    pixelation factor yields larger pixelation.

    :param img: A PIL image class that contains the image file data
    :param pixelation_factor: An integer that represents the amount of pixelation for a given image
    :precondition: All parameters must be correct types
    :postcondition: The image inputted will be pixelated and lose the original resolution
    :return: The PIL image class that represents the newly pixelated image is returned
    """
    sm_img = img.resize((pixelation_factor, pixelation_factor))
    pixelated = sm_img.resize(img.size, Image.NEAREST)
    return pixelated


def main():
    """
    Run image changer
    """
    img_file_path = os.path.join(os.path.dirname(__file__), f'Unfiltered_Images/{IMG_FILE_NAME}')
    try:
        img = Image.open(img_file_path)
        pixels = img.load()
    except FileNotFoundError:
        print('Could not find file, please ensure the file name is correct.')
        return
    except PIL.UnidentifiedImageError:
        print('Error reading file, the file is not an image.')
        return

    darken(img, pixels, DARKEN_FACTOR)
    pixelated_img = pixelate(img, PIXELATION_FACTOR)
    pixelated_img.save(f'changed-{IMG_FILE_NAME}')
    pixelated_img.close()
    img.close()
    print(f'{IMG_FILE_NAME} has been successfully processed')


if __name__ == '__main__':
    main()
