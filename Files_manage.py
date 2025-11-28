import os
from tkinter import filedialog
import crossfiledialog
import win32api
import win32con
import win32gui

class Trial:
    def __init__(self):
        self.path = r"C:\ProgramData\Stardock\Fences4"


    #This function checks if the chache and license files are present in the default path
    def verify_files(self, default_path=None):
        if default_path is None:
            default_path = self.path
        files = os.listdir(default_path)
        return "License.sig" in files and "Cache.dat" in files


    #Deletes the Cache & License files, reseting the application
    def reset_cache(self):
        #Nota: O arquivo já deve ter sido verificado e retornado como True a esse ponto.
        try:
            cache_path = os.path.join(self.path, "Cache.dat")
            license_path = os.path.join(self.path, "License.sig")
            os.remove(cache_path)
            os.remove(license_path)
        #Nota: Arrumar esse except feioso.
        except Exception as e:
            print("Error deleting files: ", e)



    def manual_find_files(self):
        # User selects the path to the Fences4 folder
        license_locate = crossfiledialog.open_file(title="Select the 'License.sig' file.")
        license_locate = os.path.dirname(license_locate)

        if self.verify_files(license_locate):
            #TODO: Criar um método para salvar essa informação,
            # para o usuário não precisar informar toda vez
            # (pensei em usar um .txt).
            self.path = license_locate
            return license_locate
        else:
            print("File not found.")
            raise SystemError


    def auto_find_files(self, root, terms):
        results = []
        terms = [t.lower() for t in terms]

        for root, dirs, files in os.walk(root):
            print(root)
            for f in files:
                name_lower = f.lower()
                if any(t in name_lower for t in terms):
                    results.append(os.path.join(root, f))

        #Breakpoint for the user certify is the file found is correct.
        print("Results:", results)
        print("Is this correct?")
        response = input("Press 'Y' to continue...")

        if response.upper() == "Y":
            return results
        return None

    # If the program doesn't find the files, this class will be called to find them'
    def find_files(self):
        while True:
            choice = int(input(
                "Your files were not found. :/ \n"
                "Do you want to enter manually or perform an automatic search?:\n"
                "[1] - Manually\n"
                "[2] - Automatic\n"
            ))
            if choice == 1:
                return self.manual_find_files()
            elif choice == 2:
                return self.auto_find_files(r"C:\\", ["Cache.dat", "License.sig"])
            else:
                print("Invalid input.")



    #TODO: Definir um modo para que o caminho informado pelo user não se perca.
    # Provavelmente o melhor modo seja retornar um arquivo txt simples que armazena o caminho.
if __name__ == "__main__":
    trial = Trial()
    if not trial.verify_files():
        path = trial.find_files()
    trial.reset_cache()