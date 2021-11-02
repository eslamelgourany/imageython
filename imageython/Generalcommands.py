import cv2
import os

class Loadimages:
    
    def __init__(self, images_list):
        self.images_list = []
        
        
    def read_image(self, file_path):
        self.image_to_modify = cv2.imread(file_path)
     
        return self.image_to_modify
        
    def read_logo(self, file_path):
        self.logo_to_use = cv2.imread(file_path)
        
        return self.logo_to_use
    
    
    def read_images(self, file_path):
        
        jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
        for file in jpg_files:
            imgs_path = os.path.join(path, file)
            images_to_modify = cv2.imread(imgs_path)
            images_list.append(image_to_modify)
            
        self.images_list = images_list
        
        