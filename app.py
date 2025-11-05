import os
import sys

path = r"C:\ProgramData\Stardock\Fences4"

#This function checks if the chache and license files are present in the default path
def verify_files(default_path):
    for file in os.listdir(default_path):
        if "License.sig" in file and "Cache.dat" in file:
            return True
    return False

#Deletes the Cache & License files, reseting the application
def reset_cache(path):
    #TODO: Precisa primeiro pegar a parte inteira do path dos arquivos.
    # Precisamos pegar o caminho atua, e dar .join() com o nome dos arquivos, o resultado será o parâmetro para a func remove deletar.
    os.remove("License.sig")
    os.remove("Cache.dat")



if __name__ == "__main__":
    verify_files(path)
    if not verify_files(path):
        # TODO: Caso o programa não consiga achar os arquivos na pasta padrão, esta funcao deve ser chamada para procurar onde os arquivos estao
        pass