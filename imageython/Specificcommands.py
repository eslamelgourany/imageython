import cv2
import os
from .Generalcommands import Loadimages

class Processimages(Loadimages):
    
    
    def __init__(self, images_list):
        Loadimages.__init__(self, images_list)
        
        
        
    def rotate_image(image, degree_of_rotation):
        """
        Function to rotate list of images by defined degree of rotation

        Args:
            images_list: list of images that needs modification. (List of opencv image object)
            degree_of_rotation: Degree of rotation needed to be applied on the images.
            
        Return:
            None

        """
       
        rotated_image = ndimage.rotate(image, degree_of_rotation)
        filename = "Image_rotated"
        cv2.imwrite(os.path.join("/" , str(filename) + ".jpg"), rotated_image)


    