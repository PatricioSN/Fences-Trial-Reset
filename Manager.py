from FencesManage import FencesManage
from FilesManage import FilesManage

class Manager:
    def run(self):
        Fences = FencesManage()
        Files = FilesManage()

        Files.run()
        Fences.prepare_email()
        Fences.open_fences()
        Fences.start_trial()
        Fences.listen_email()