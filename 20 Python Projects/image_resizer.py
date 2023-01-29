#import pillow 
#open image we want on python 
# open up the want to resize using python 
#print curent size image 
# specify size we want 
# save the new resize image 

from PIL import Image

def resize_imag3(size1, size2):
    image =Image.open('.png')

    print(f"current size : {image.size}")

    resized_image = image.resize((size1,size2))

    resized_image.save('newqr.jpg')

#size1 = input('Enter width: ')
#size2 = input('Enter height: ')
#resize_imag3(size1, size2)
    