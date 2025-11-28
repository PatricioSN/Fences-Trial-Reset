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


