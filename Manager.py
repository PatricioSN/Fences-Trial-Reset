from FencesManage import FencesManage
from FilesManage import FilesManage
import logging
import sys

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
)
handler.setFormatter(formatter)

logging.getLogger().handlers.clear()
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.INFO)

class Manager:
    def run(self):
        fences = FencesManage()
        files = FilesManage()

        files.run()
        fences.prepare_email()
        fences.open_fences()
        fences.start_trial()
        fences.listen_email()