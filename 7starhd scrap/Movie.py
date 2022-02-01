from turtle import title

from pip import main


class Movie:

    def __init__(self, title, link, image):
        self.title = title
        self.link = link
        self.image = image
    

    # Make Getters and Setters of each Property
    
    # getter method
    def get_title(self):
        return self.title
    
    def set_title(self, x):
        self.title = x
    
    def get_link(self):
        return self.link
      
    def set_link(self, link):
        self.link = link

    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image

