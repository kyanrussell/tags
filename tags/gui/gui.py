# import subprocess
# from PIL import Image
# from time import sleep

# with Image.open("../DSC09961.JPG") as img:
#     img.show()
#     subprocess.call(['xdotool', 'click', '1'])
#     tag = input("Add tags?")
#     print(tag)
#     subprocess.call(['osascript', '-e', 'tell application "Preview" to quit'])
from tags.logic.tags import add_tag, get_photos
from tags.types.photo import Photo
from tags.tag_types.species_code import SpeciesCode

from tkinter import *
from PIL import ImageTk,Image


WIDTH = 1200
HEIGHT = 900


root = Tk()
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("../DSC09961.JPG").resize((WIDTH, HEIGHT)))
canvas.create_image(0, 0, anchor=NW, image=img)


def add_tags_cmd():
   global entry
   string= entry.get()
   label.configure(text=string)
   add_tag(photo=Photo("../DSC09961.JPG"), tag=SpeciesCode(string))
   print(get_photos(SpeciesCode(string)))

#Initialize a Label to display the User Input
label=Label(canvas, text="Add tags?", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(canvas, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
Button(canvas, text= "Okay",width= 20, command=add_tags_cmd).pack(pady=20)



root.mainloop() 



