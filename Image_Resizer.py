# install Pillow 
# import pillow 
# open up the image we want to resize using python
# print the current size of the image 
# specify the size we want to change it to 
# save the new resize image

from PIL import Image

image = Image.open("banner.jpg")

print(image.size)

resize_image = image.resize((620,100))

resize_image.show()

save = resize_image.save("resize_photo.jpg")