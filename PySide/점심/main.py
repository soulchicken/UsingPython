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
        solution = ['맘스터치','닭곰탕','발바리네',
            '국시와가래떡','상수봉봉','포보',
            '북촌손만두','식스티즈버거','슈슈짬뽕',
            '비비리', '피자스쿨']
        place = ['정문으로 가','정문에서 왼쪽으로 건너가','정문에서 오른쪽으로 가',
            '정문에서 왼쪽으로 건너가','상수쪽으로 가','정문에서 왼쪽으로 건너가',
            '정문 오른쪽 아니면 기숙사쪽으로 가', '정문에서 오른쪽으로 건너가', '정문에서 오른쪽으로 건너가',
            '티동쪽으로 가', '상수쪽으로 가']
        mb_lunch = QMessageBox()
        a = random.randint(0,len(solution) - 1)
        b = random.randint(0,len(solution) - 1)
        while b == a:
            b = random.randint(0,len(solution) - 1)
        mb_lunch.setText(f"{solution[a]} 어때?")
        answer = mb_lunch.addButton(f"GO GO", QMessageBox.ActionRole)
        no_answer= mb_lunch.addButton(f"{solution[b]} (은)는 어때?", QMessageBox.ActionRole)
        mb_lunch.exec()

# solution = ['맘스터치','닭곰탕','발바리네',
#             '국시와가래떡','상수봉봉','포보',
#             '북촌손만두','식스티즈버거','슈슈짬뽕',
#             '비비리', '피자스쿨']

# i = random.randint(0,len(solution) - 1) # 정수 랜덤
# print(solution[i])


        if mb_lunch.clickedButton() == answer:
            mb_success = QMessageBox()
            mb_success.setText(place[a])
            mb_success.exec()
        elif mb_lunch.clickedButton() == no_answer:
            # print("틀렸어")
            mb_fail = QMessageBox()
            mb_fail.setText(place[b])
            mb_fail.exec()

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())