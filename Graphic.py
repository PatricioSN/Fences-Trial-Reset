import tkinter as tk
from tkinter import filedialog

def seletor():
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.update()
    caminho = filedialog.askopenfilename(title="Selecione o arquivo")
    root.destroy()
    print("Caminho selecionado:", caminho)

if __name__ == "__main__":
    seletor()



# import tkinter as tk
# from tkinter import filedialog
#
# class Graphic:
#     def __init__(self, master):
#         self.ourGraphic = master
#         self.menu_bar = tk.Menu(self.ourGraphic)
#         self.ourGraphic.config(menu=self.menu_bar)
#         self.menu_bar.add_command(label="Ler Arquivo", command=self.readFile)
#         self.menu_bar.add_command(label="Abrir diretório do arquivo", command=self.openDir)
#
#     def readFile(self):
#         self.file = filedialog.askopenfile(mode='r', title= "Selecione um arquivo")
#         self.content = self.file.read()
#         print(self.content)
#
#     def openDir(self):
#         self.file_2 = filedialog.askopenfilename(title="Selecione o local do arquivo")
#         self.path = self.file_2
#         print(self.path)
#
# root = tk.Tk()
# Graphic(root)
# root.mainloop()
