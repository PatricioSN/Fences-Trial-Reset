from tkinter import *

root = Tk()

class Application(root):
    def __init__(self):
        self.tela()
        self.root = root
        root.mainloop()


    def tela(self):
        self.root.title("ADkmsadkasldmas")
        self.root.configure(background="#000000")

Application()