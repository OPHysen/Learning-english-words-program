import random 
from tkinter import *
import login
import words_add


class english_main():
    def main(self):
        self.say = 0
        self.root = Tk()
        self.root.title("Artificial Word Teacher")
        #self.root.attributes("-fullscreen", True)
        self.button = Button(self.root, text="NEW WORDS",
                            command = self.get_words,
                            borderwidth=1,
                            foreground="blue",
                            font="Tahoma").place(x = 55,y = 220)
        self.button = Button(self.root, text="QUIT",
                            command = self.program_exit,
                            borderwidth=1,
                            foreground="red",
                            font="Tahoma").place(x = 1350,y = 220)
        self.button_add = Button(self.root, text="WORD ADD",
                                command= self.wordadd,
                                borderwidth=1,
                                foreground="blue",
                                font="Tahoma").place(x = 55,y = 290)
        self.root.mainloop()
    
    def get_words(self):
        self.say += 1
        if self.say <= 5:
            self.label = Label(self.root, text="word")
            self.label.pack_forget()
            with open("new.txt","r") as read:
                a = read.read()
                a = list(a.split("."))
            with open("old.txt","r") as read:
                b = read.read()
                b = list(b.split("."))
            final_list = []
            for x in a:
                if x not in b:
                    final_list.append(x)
            textword = random.sample(final_list,1)
            with open("old.txt","a") as write:
                write.write(f"{textword[0]}.")
            self.label = Label(self.root, text=f"{textword[0]}",
                            font=('Baskerville Old Face','12','bold'))
            self.label.pack(pady=50)
            print(self.say)
    def wordadd(self):
        words_add.add_word()
    def program_exit(self):
        self.root.destroy()
    
login.enter()
student = english_main()
student.main()