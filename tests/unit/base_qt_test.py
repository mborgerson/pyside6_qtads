import  unittest 
import gc
from PySide6.QtWidgets import QApplication

class BaseQtTest(unittest.TestCase):   
    def setUp(self) -> None:
        super().setUp()
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication([])

    def tearDown(self):
         gc.collect()
         self.app.processEvents()
         super().tearDown()