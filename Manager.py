from Fences_manage import Fences_manage
from Files_manage import Trial

class Manager:
    def run(self):
        Fences = Fences_manage()
        Files = Trial()

        Files.run()
        Fences.prepare_email()
        Fences.open_fences()
        Fences.start_trial()
        Fences.listen_email()