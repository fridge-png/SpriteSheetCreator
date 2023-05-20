from PIL import Image
import os
    
# This script create a sprite sheet from a set of images
# The order of the image must be appended to the end of its name like so: SampleImage_1.png

#========================================
# FIELDS TO CHANGE 
# path of the directory that contains your images 
imageDir = "SampleImages/"
# path of the directory that you want your final image to be saved in 
saveDir = "SavedImage/"
# what you want your final image to be called
finalImageName = "FinalImage"
# x,y dimensions of your images (all images will be resized to this size)
imageDim = [40,40]
# set to true if the spritesheet images should go horizontally
byCol = True
# number of columns in each row / num of rows in each column
colRowNum = 5
# margin between each image on the spritesheet
imageXMargin = 0
imageYMargin = 0
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

# crops image to the imageDim values
def resizeImage(image):
    #left top right bottom
    image = image.resize((imageDim[0],imageDim[1]))
    return image

# uses the PIL library to paste the images and saves to the save directory
def layerImages():
    images = os.listdir(imageDir)
    images.sort(key=getNum)
    try:
        if(byCol):
            spriteSheet = Image.new("RGBA",(colRowNum*(imageDim[0]+imageXMargin),(int(len(images)/colRowNum))*(imageDim[1]+imageYMargin)))
        else:
            spriteSheet = Image.new("RGBA",((int(len(images)/colRowNum))*(imageDim[1]+imageXMargin),colRowNum*(imageDim[0]+imageYMargin)))
    except Exception as e:
        print("Error while creating image.")
        print(e)
        return
    for i,image in enumerate(images):
        if(image[-4:].lower() == ".png"):
            if (getNum(image) == float('inf')):
                print("File {image} is not named correctly.\nMake sure the file ends with \'_\' and its order.\n".format(image = image))
            else:
                try:
                    img = Image.open(imageDir + image)
                    img = resizeImage(img)
                    if(byCol):
                        spriteSheet.paste(img, ((((i)%colRowNum)*(imageDim[0]+imageXMargin),int((i)/colRowNum)*(imageDim[1]+imageYMargin))),img)
                    else:
                        spriteSheet.paste(img, (((int((i)/colRowNum)*(imageDim[1]+imageXMargin),(i%colRowNum)*(imageDim[0]+imageYMargin)))),img)
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