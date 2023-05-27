from tkinter import *
import os
import create
def enter():
    root = Tk()
    root.geometry("320x240")
    root.title("LOGIN")
    Username=Text(root, height=1, width=20)
    label = Label(root, text = "Username",font = ("Baskerville Old Face","14"))
    def get_username():
        inputValue=Username.get("1.0","end-1c")
        os.chdir(f"{os.getcwd()}\{inputValue}")
        root.destroy()
    button = Button(root, text="LOGIN",
            command = get_username,
            borderwidth = 2)
    create_button = Button(root, text="CREATE",
                            command=create.create_user
                            )
    label.pack(padx=30, pady= 10)
    Username.pack(padx = 30,pady = 20)
    button.pack(padx= 50,pady= 5)
    create_button.pack(padx= 50,pady=10)
    root.mainloop()



        