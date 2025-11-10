import os
from tkinter import filedialog

path = r"C:\ProgramData\Stardock\Fences4"

#This function checks if the chache and license files are present in the default path
def verify_files(default_path):
    for file in os.listdir(default_path):
        if "License.sig" in file and "Cache.dat" in file:
            return True
    return False

#Deletes the Cache & License files, reseting the application
def reset_cache(path):
    #TODO: finalizar
    os.remove("License.sig")
    os.remove("Cache.dat")


def Manual_find_files():
    # User selects the path to the Fences4 folder
    license_locate = filedialog.askopenfilename(title="Selecione o arquivo 'License.sig'")

    if verify_files(license_locate):
        path = license_locate
    else:
        print("Arquivo não reconhecido")

def Auto_find_files():
    #TODO: terminar essa func
    pass

# If the program doesn't find the files, this class will be called to find them'
def find_files():
    input(r"Seus arquivos não foram encontrados. :/ \n "
          "Deseja Informar Manualmente ou realizar uma busca automática?: \n"
          "[1] - Manual \n"
          "[2] - Automática")
    if input == 1:
        Manual_find_files()
    elif input == 2:
        Auto_find_files()


if __name__ == "__main__":
    if not verify_files(path):
        find_files()
    reset_cache(path)