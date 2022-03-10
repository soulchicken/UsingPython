import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

# 디자이너 경로 : ./myvenv/lib/python3.10/site-packages/PySide6/Designer.app/Contents/MacOS/Designer
# uci 경로 : ./myvenv/lib/python3.10/site-packages/PySide6/Qt/libexec/uic
#  (uci 경로) -g python (해당파일명).ui > (만들경로/만들파일명).py
# ./myvenv/lib/python3.10/site-packages/PySide6/Qt/libexec/uic -g python (해당파일경로/해당파일명).ui > (만들경로/만들파일명).py

# ./myvenv/lib/python3.10/site-packages/PySide6/Qt/libexec/uic -g python myvenv/UsingPython/PySide/ChatTool/ui2.ui > myvenv/UsingPython/PySide/ChatTool/ui2.py