import os
from tkinter import filedialog

class Trial:
    def __init__(self, path):
        self.path = r"C:\ProgramData\Stardock\Fences4"


    #This function checks if the chache and license files are present in the default path
    @staticmethod
    def verify_files(self, path):
        for file in os.listdir(path):
            if "License.sig" in file and "Cache.dat" in file:
                return True
        return False


    #Deletes the Cache & License files, reseting the application
    def reset_cache(self, path):
        #Nota: O arquivo já deve ter sido verificado e retornado como True a esse ponto.
        try:
            cache_path = os.path.join(self.path, "Cache.dat")
            license_path = os.path.join(self.path, "License.sig")
            os.remove(cache_path)
            os.remove(license_path)
        #Nota: Arrumar esse except feioso.
        except:
            print("Error deleting files.")



    def manual_find_files(self):
        # User selects the path to the Fences4 folder
        license_locate = filedialog.askopenfilename(title="Select the 'License.sig' file.")
        if self.verify_files(self, license_locate):
            path = license_locate
            return path
        else:
            print("File not found.")
            return


    def auto_find_files(self):
        #TODO: terminar essa func
        pass


    # If the program doesn't find the files, this class will be called to find them'
    def find_files(self):
        while True:
            input(r"Your files were not found. :/ \n "
                  "Do you want to enter manually or perform an automatic search?: \n"
                  "[1] - Manually \n"
                  "[2] - Automatic")
            if input == 1:
                return self.manual_find_files()
            elif input == 2:
                return self.auto_find_files()
            else:
                print("Invalid input.")


    def run(self):
        if not self.verify_files(self.path):
            path = self.find_files()
        self.reset_cache(self.path)

   if __name__ == "__main__":
        run()