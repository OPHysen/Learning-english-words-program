import re
from tkinter import *



def add_word():
    root = Tk()
    root.geometry("320x240")
    root.title("WORD ADD")
    Username=Text(root, height=1, width=20)
    def toenglishword():
            inputValue=Username.get("1.0","end-1c")
            word = re.sub(",","",inputValue)
            word = re.sub("ç","c",word)
            word = re.sub("ş","s",word)
            word = re.sub("ı","i",word)
            word = re.sub("’"," ",word)
            word = re.sub("ö","o",word)
            word = re.sub("ü","u",word)
            word = re.sub("‘"," ",word)
            word = re.sub("ğ","g",word)
            print(word)
            with open("new.txt","a") as new:
                new.write("\n"+word+".")
    addbutton = Button(root, text="ADD",
                      command=toenglishword)
    Username.pack(padx=20,pady=50)
    addbutton.pack(padx=20,pady=10)
    root.mainloop()




