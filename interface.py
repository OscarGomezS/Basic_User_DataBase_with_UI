from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Interface:

    def __init__(self):
        pass

    def display_welcome_message(self):
        text = "User DataBase"
        
        myfont = ImageFont.truetype("verdanab.ttf", 10)
        size = myfont.getsize(text)
        img = Image.new("1",size,"black")
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, "white", font=myfont)
        pixels = np.array(img, dtype=np.uint8)
        chars = np.array([' ','#'], dtype="U1")[pixels]
        strings = chars.view('U' + str(chars.shape[1])).flatten()
        print( "\n".join(strings))
        print("\n")

    def display_description_message(self):
        print(
            "Welcome to the user database, where you can manage the entire database." + "\n" + "\n" +
            "You can Create, Read, Update, and Delete users." + "\n" + "\n" +
            "If you want to Create a user, digit 1 and press Enter" + "\n" +
            "If you want to Read a user, digit 2 and press Enter" + "\n" +
            "If you want to Update a user, digit 3 and press Enter" + "\n" +
            "If you want to Delete a user, digit 4 and press Enter" + "\n" +
            "If you want to Display all users, digit 5 and press Enter" + "\n" 
            "Digit 6 to leave the session: "+ "\n"
        )