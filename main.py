from PIL import Image
import os
from enum import Enum
    
# This script layers png images on top of each other and creates a final layered png file
# The order of the image must be appended to the end of its name like so: SampleImage_1.png
# An image with a lower order will apear behind an image with a higher order

#========================================
# FIELDS TO CHANGE 
# path of the directory that contains your images 
imageDir = "SampleImages/"
# path of the directory that you want your final image to be saved in 
saveDir = "SavedImages/"
# what you want your final image to be called
finalImageName = "FinalImage"
# x,y dimensions of your images (all images will be cropped to this size)
imageDim = [50,50]
# rowNum = 2
colNum = 10
# set to true if you want your cropped images to be saved in the croppedDir set above
saveCroppedImages = True
#========================================

# checks if the directories exist
def checkDir():
    if(os.path.isdir(imageDir) and os.path.isdir(saveDir)):
        return True
    else:
        return False

# gets the order of the image for sorting
def getNum(img):
    try:
        return int(img[img.rindex('_')+1:img.rindex('.')])
    except ValueError:
        return float('inf')

# crops image to the imageDim values with the offsetCrop offset
def cropImage(image):
    #left top right bottom
    image = image.crop((0,0,imageDim[0],imageDim[1]))
    return image

# uses the PIL library to layer images and saves to the save directory
def layerImages():
    images = os.listdir(imageDir)
    images.sort(key=getNum)
    try:
        spriteSheet = Image.new("RGBA",(colNum*imageDim[0],(int(len(images)/colNum))*imageDim[1]))
    except Exception as e:
        print("Error while reading images.")
        print(e)
        return
    for i,image in enumerate(images):
        if(image[-4:].lower() == ".png"):
            if (getNum(image) == float('inf')):
                print("File {image} is not named correctly.\nMake sure the file ends with \'_\' and its order.\n".format(image = image))
            else:
                try:
                    img = Image.open(imageDir + image)
                    # img = cropImage(img)
                    # if(saveCroppedImages):
                    #     img2.save(croppedDir + "Cropped_" + image)
                    # if(i%colNum == 0):
                    print (i+1)
                    spriteSheet.paste(img, ((((i)%colNum)*imageDim[0],int((i)/colNum)*imageDim[1])),img)
                    # else:
                        # img1.paste(img2, (0,0), mask = img2)
                except Exception as e:
                    print("Error while reading images.")
                    print(e)
                    return
        else:
            print("File {image} is not a .png file.\n".format(image = image))

        spriteSheet.save(saveDir + finalImageName + ".png","PNG")


if(checkDir()):
    layerImages()
else:
    print("The image directory you specified was not found.")