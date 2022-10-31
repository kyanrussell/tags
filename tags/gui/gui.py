from tags.logic.tags import add_tag, get_photos
from tags.types.photo import Photo
from tags.tag_types.species_code import SpeciesCode

from tkinter import *
from PIL import ImageTk,Image


WIDTH = 1200
HEIGHT = 900


root = Tk()

# ========< background image >=======================================================
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

image1 = Image.open("../DSC09961.JPG").resize((width, height))
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

# ========< button >=================================================================
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()


def add_tags_cmd():
   global entry
   string= entry.get()
   label.configure(text=string)
   species_code = SpeciesCode(SpeciesCode[string])
   add_tag(photo=Photo("../DSC09961.JPG"), tag=species_code)
   print(get_photos(species_code))

#Initialize a Label to display the User Input
label=Label(canvas, text="Add tags?", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(canvas, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
Button(canvas, text= "Okay",width= 20, command=add_tags_cmd).pack(pady=20)

# ========< main loop >=================================================================
root.mainloop() 



