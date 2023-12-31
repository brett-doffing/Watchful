from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2

class TKCamera(Frame):
    def __init__(self, parent, name=""):
        """A tkinter Frame that displays a camera feed"""
        Frame.__init__(self, parent, highlightbackground="black", highlightthickness=1)

        self.name = name
        self.width  = 320
        self.height = 240
        
        self.label = Label(self, text=name)
        self.label.pack()

        self.img_label = Label(self, width=self.width, height=self.height)
        self.img_label.pack()

        print('[tkCamera] source:', self.name)

        self.image = None

    def update_feed(self, img):
        """Updates the feed of the camera widget with the given image"""
        if img is not None:
            self.image = img
            image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (self.width, self.height))
            self.image = Image.fromarray(image)
            self.photo = ImageTk.PhotoImage(image=self.image)
            self.img_label.config(image=self.photo)
            self.img_label.image = self.photo
            
        self.img_label.update()