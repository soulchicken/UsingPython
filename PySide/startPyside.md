# Pyside 시작하기

## PySide

    - GUI를 구현하는데 도와주는 크로스 플랫폼. (맥에서도 쓰고 윈도우에서도 리눅스에서도 쓸 수 있게 함)
    - [`PySide6`](https://doc.qt.io/qtforpython/quickstart.html)를 참고했다.

## PySide 버전 확인

```python
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__) # 결과 : 6.2.3 출력 됨

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__) # 결과 : 6.2.3 출력 됨
```

## PySide Hello World

```python
import sys
import random
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
```