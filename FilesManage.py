import os
import logging
import crossfiledialog


class FilesManage:
    DEFAULT_PATH = r"C:\ProgramData\Stardock\Fences4"
    REQUIRED_FILES = {"License.sig", "Cache.dat"}

    def __init__(self, base_path: str | None = None):
        self.path = base_path or self.DEFAULT_PATH


    #This function checks if the chache and license files are present in the default path
    def verify_files(self, path: str | None = None) -> bool:
        target = path or self.path
        try:
            files = set(os.listdir(target))
            return self.REQUIRED_FILES.issubset(files)
        except FileNotFoundError:
            logging.warning("Path not found: %s", target)
            return False


    #Deletes the Cache & License files, reseting the application
    def reset_cache(self) -> None:
        for file in self.REQUIRED_FILES:
            file_path = os.path.join(self.path, file)
            try:
                os.remove(file_path)
                logging.info("File %s deleted successfully.", file_path)
            except FileNotFoundError:
                logging.warning("File %s not found.", file_path)
            except PermissionError as e:
                logging.error("Permission error removing %s", file_path, exc_info=e)



    def manual_find_files(self) -> str:
        # User selects the path to the Fences4 folder
        selected_file = crossfiledialog.open_file(
            title="Select the 'License.sig' file."
        )
        license_locate = os.path.dirname(selected_file)

        if not self.verify_files(license_locate):
            #TODO: Criar um método para salvar essa informação,
            # para o usuário não precisar informar toda vez
            # (pensei em usar um .txt).
            raise RuntimeError("Required files not found in selected directory")

        self.path = license_locate
        return license_locate


    def auto_find_files(self, root, terms):
        results = []
        terms = [t.lower() for t in terms]

        for root, dirs, files in os.walk(root):
            logging.info(root)
            for f in files:
                name_lower = f.lower()
                if any(t in name_lower for t in terms):
                    results.append(os.path.join(root, f))

        #Breakpoint for the user certify is the file found is correct.
        logging.info("Results:", results)
        logging.info("Is this correct?")
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
                "[3] - Files have already been deleted."
            ))
            if choice == 1:
                return self.manual_find_files()
            elif choice == 2:
                return self.auto_find_files(r"C:\\", ["Cache.dat", "License.sig"])
            elif choice == 3:
                return None
            else:
                print("Invalid input.")


    def run(self):
        if not self.verify_files():
            self.find_files()
        self.reset_cache()


if __name__ == "__main__":
    trial = FilesManage()
    trial.run()