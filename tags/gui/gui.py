import subprocess
from PIL import Image
from time import sleep
from tags.tag_types.species_code import SpeciesCode
from tags.logic.hamming_distance import get_top_n_closest_species_codes

with Image.open("../DSC09961.JPG") as img:
    img.show()
    sleep(1)
    subprocess.call(['osascript', '-e', 'tell application "iTerm" to activate'])

    def get_input():
        tag = input("Add 4-letter species code? ").upper()
        suggested_tags = get_top_n_closest_species_codes(tag, 7)
        if suggested_tags[0].name == tag:
            print(f"tag {tag} accepted.")
            return True
        else:
            print(f"tag {tag} invalid. did you mean: {suggested_tags}")
            # TODO: GET MORE SUGGESTIONS
            return False

    while True:
        if get_input():
            subprocess.call(['osascript', '-e', 'tell application "Preview" to quit'])
            break






# ========< tkinter appraoch >=======================================================

# from tags.logic.tags import add_tag, get_photos
# from tags.types.photo import Photo
# from tags.tag_types.species_code import SpeciesCode

# from tkinter import *
# from PIL import ImageTk,Image


# WIDTH = 1200
# HEIGHT = 900


# root = Tk()

# # ========< background image >=======================================================
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()

# root.geometry("%dx%d" % (width, height))

# image1 = Image.open("../DSC09961.JPG").resize((width, height))
# test = ImageTk.PhotoImage(image1)

# label1 = Label(image=test)
# label1.image = test

# # Position image
# label1.place(x=0, y=0)

# # ========< button >=================================================================
# canvas = Canvas(root, width = WIDTH, height = HEIGHT)
# canvas.pack()

# def add_tags_cmd():
#    global entry
#    string = entry.get()
#    label.configure(text=string)
#    species_code = SpeciesCode(SpeciesCode[string])
#    add_tag(photo=Photo("../DSC09961.JPG"), tag=species_code)
#    print(get_photos(species_code))

# #Initialize a Label to display the User Input
# label=Label(canvas, text="Add tags?", font=("Courier 22 bold"))
# label.pack()

# #Create an Entry widget to accept User Input
# entry= Entry(canvas, width= 40)
# entry.focus_set()
# entry.pack()

# #Create a Button to validate Entry Widget
# Button(canvas, text= "Okay",width= 20, command=add_tags_cmd).pack(pady=20)

# # ========< main loop >=================================================================
# root.mainloop() 



