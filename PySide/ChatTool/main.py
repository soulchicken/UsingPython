import sys
import random
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import QTimer
from ui2 import Ui_MainWindow 

class MainWindow(QMainWindow):
    last_read = 0
    def __init__(self): 
        super(MainWindow,self).__init__()
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self)
 
        self.ui2.btn_send.clicked.connect(self. send)
        self.ui2.edit_text.returnPressed.connect(self.send)

        nickname = self.random_name()
        self.ui2.edit_name.setText(nickname)
        
        # welcome
        with open("./myvenv/UsingPython/Pyside/ChatTool/server.txt","a") as f:
            f.writelines(f"------------{nickname} 님이 입장하셨습니다------------\n")


        self.listen()
        self.timer = QTimer()    
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.listen)
        self.timer.start()


    def send(self):
        nickname = self.ui2.edit_name.text()
        text = self.ui2.edit_text.text()
        msg = f"{nickname} : {text}"
        # 파일 열고 메세지 넣기
        with open("./myvenv/UsingPython/Pyside/ChatTool/server.txt","a") as f:
            f.writelines(msg + "\n")
        self.ui2.edit_text.clear()
        self.listen()

    def random_name(self):
        nickname = random.choice(["나성범", "김광현","김기태"])
        num = random.randint(1,10000)
        return f"{nickname}{num}"

    def listen(self):
        with open("./myvenv/UsingPython/Pyside/ChatTool/server.txt","r") as f:
            lines = f.readlines()
        lines = [x.strip() for x in lines]
        self.ui2.list_chat.addItems(lines[self.last_read:])
        self.last_read = len(lines)
        self.ui2.list_chat.scrollToBottom()

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow() 
    window.show()

    sys.exit(app.exec())