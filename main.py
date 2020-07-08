import os
from pip._internal import main
from PIL import Image
from easygui import diropenbox

# path = "C:/Users/user/Pictures/Camera Roll/temp"
# path = "C:/Users/user/Documents/Budget 2018/San Francisco 2018"

fileNamePretext = "_DSC"


def updateCount(count):
    # Function to add digits to the image name so that there are a total of
    # 4 digits in the image name i.e image #21 -> image #0021

    while str(count).__len__() < 4:
        count = "0" + str(count)

    return count


def getAllImagesAndDateTime():
    # Function that creates the list of tuples based on each filename in the specified folder
    # And gets the datetime from each images metadata

    images = list()
    NoneType = type(None)

    for filename in os.listdir(path):
        date_time = Image.open(path + "/" + filename).getexif().get(36867)

        if isinstance(date_time, NoneType):
            date_time = "0000:00:00 00:00:00"

        images.append(tuple((filename, date_time)))

    print(images)
    return images


def sortImages(images):
    # Function that sorts the list of tuples based on the datetime value

    images.sort(key=lambda x: x[1])
    return images


def tempRename(images):
    # Function that temporarily changes each image name by adding a '__' in front of each
    # This is done to prevent any accidental duplicate names clashing during the process

    for image in images:
        image_name = image[0]
        image_path = os.path.join(path, image_name)
        temp_image_path = os.path.join(path, "__" + image_name)

        os.rename(image_path, temp_image_path)


def updateImageName(images):
    # Function that updates the name of each image, so that they are listed in order of the datetime

    count = 1
    for image in images:
        image_name = image[0]
        image_path = os.path.join(path, "__" + image_name)

        new_image_path = os.path.join(path, fileNamePretext + updateCount(count) + ".JPG")
        os.rename(image_path, new_image_path)
        count += 1

# main(["install", "easygui"])

# Main
# Gets all images from a specified folder, and their datetime
# If there are images in the folder, the images are sorted based on the datetime
# The sorted images are renamed with a temporary name, to prevent any duplicate names during the process
# The sorted images are finally renamed with their correct name format (_DSC####) based on their datetime

path = diropenbox()
all_pictures = getAllImagesAndDateTime()

if len(all_pictures) > 0:
    all_pictures = sortImages(all_pictures)
    tempRename(all_pictures)
    updateImageName(all_pictures)
else:
    print("No Pictures")
