import os
from tkinter import *


def create_user():
    root = Tk()
    root.geometry("320x240")

    def cr_button():
        getinput = userentry.get("1.0","end-1c")
        os.chdir(f"{os.getcwd()}")
        os.mkdir(f"{getinput}")
        os.chdir(f"{os.getcwd()}\{getinput}")
        with open("new.txt","w") as createnew:
            createnew.write("")
        with open("old.txt","w") as createnew:
            createnew.write("")
        print(os.getcwd())
    
    create_label = Label(root, text="CREATE",
                        font = "bold",
                        )

    userentry = Text(root, width=10,height= 1)

    create_button = Button(root, text="Create",
                            command=cr_button)
    
    create_label.pack(pady= 20)
    userentry.pack()
    create_button.pack(pady=8)
    root.mainloop()
