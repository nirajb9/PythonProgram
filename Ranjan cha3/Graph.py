from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 510, height = 325)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("I1.PNG"))  
canvas.create_image(0, 0, anchor=NW, image=img) 

canvas1 = Canvas(root, width = 510, height = 325)  
canvas1.pack()  
img1 = ImageTk.PhotoImage(Image.open("I2.PNG"))  
canvas1.create_image(20, 0, anchor=NW, image=img1) 
root.mainloop() 