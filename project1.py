#Ravinder Singh
#Class 205 MW 10am
#Project 1


from __future__ import print_function #importing functions from the future
from PIL import Image  #importing pillow image filters

def blackwhite (Photos): #this function is used to make the images Black and white
    Photos = Photos.convert('1') #converting photos into black and white
    Photos.show() #printing out the result

def Colors (Photos): #this function is used to turn photos into different filters
    Photos = Photos.convert('L') #Applying the filter
    Photos.show() #printing out the photo in different filter



theImages = [] #its a list of photos

pathtoimages = "/Users/Ravi/desktop/CST205/Images/" #variable to use the path of photos


for myImage in range (1,10): #using loop with range 1 to 10 for 9 photos

    theImages.append(Image.open(pathtoimages + str(myImage) + ".png")) #opening the photo
myCounter = 1 #starting point is 0

for aImage in theImages: # using another loop to find out even and odd photos
    if (myCounter%2==1):
        blackwhite (aImage)   #print("odd")
    else:
        Colors (aImage)  #print("even")

    #print(myCounter%2 == 1):
    #print("odd")

    #print("even")
    myCounter = myCounter + 1 #going back to loop and adding 1


#print (image)
#image = Image.open(image)
#print("Image size is: ")
#print(im.size[0])

#print(im.format, im.size, im.mode)
#im.show()
#image_file = im.convert('1')
#image_file.show()
