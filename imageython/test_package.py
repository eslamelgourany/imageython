# Import libraries
from imageython import Processimages
from imageython import Loadimages


'''
This is a script to test my package
'''

images = Loadimages.read_image(file_path="images/")
print("Type of images", type(images))
print("Images are", images)