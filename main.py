import os
from pip._internal import main
from PIL import Image

path = "C:/Users/user/Pictures/Camera Roll/temp"
#path = "C:/Users/user/Documents/Budget 2018/San Francisco 2018"

fileNamePretext = "_DSC"


def countUpdate(count):
    while str(count).__len__() < 4:
        count = "0" + str(count)

    return count


def getAllPicturesAndDateTime():
    pictures = list()
    NoneType = type(None)

    for filename in os.listdir(path):
        date_time = Image.open(path + "/" + filename).getexif().get(36867)

        if isinstance(date_time, NoneType):
            date_time = "0000:00:00 00:00:00"
        pictures.append(tuple((filename, date_time)))

    print(pictures)
    return pictures


def sortPictures(pictures):
    pictures.sort(key=lambda x: x[1])
    return pictures


def tempRename(pictures):
    for image in pictures:
        image_name = image[0]
        image_path = os.path.join(path, image_name)
        temp_image_path = os.path.join(path, "__" + image_name)

        os.rename(image_path, temp_image_path)


def updateImageName(pictures):
    count = 1
    for image in pictures:
        image_name = image[0]
        image_path = os.path.join(path, "__" + image_name)

        new_image_path = os.path.join(path, fileNamePretext + countUpdate(count) + ".JPG")
        os.rename(image_path, new_image_path)
        count += 1

    print("Updated")

# main(["install", "Pillow"])


all_pictures = getAllPicturesAndDateTime()

if len(all_pictures) > 0:
    all_pictures = sortPictures(all_pictures)
    tempRename(all_pictures)
    updateImageName(all_pictures)
else:
    print("No Pictures")
