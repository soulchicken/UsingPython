import sys 
import random

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from clickme import Ui_btn_clickme

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.clickme = Ui_btn_clickme()
        self.clickme.setupUi(self)
        
        self.clickme.pushButton.clicked.connect(self.click)
        
    def click(self):
        # self.clickme.pushButton.setText("눌렀어요")
        # print("클릭 슬롯 입니다.")
        mb_hi  = QMessageBox()
        mb_hi.setText("잘 눌렀네?")
        mb_hi.exec()

        mb_quiz = QMessageBox()
        a = random.randint(1,100)
        b = random.randint(1,100)
        mb_quiz.setText(f"{a} + {b} = ?")
        answer = mb_quiz.addButton(f"{a+b}", QMessageBox.ActionRole)
        no_answer= mb_quiz.addButton(f"{a-b}", QMessageBox.ActionRole)
        mb_quiz.exec()

        if mb_quiz.clickedButton() == answer:
            # print("정답이야")
            mb_success = QMessageBox()
            mb_success.setText("정답이야")
            mb_success.exec()
        elif mb_quiz.clickedButton() == no_answer:
            # print("틀렸어")
            mb_fail = QMessageBox()
            mb_fail.setText("틀렸어")
            mb_fail.exec()
            
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())