from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
mainLine = QVBoxLayout()


window.setLayout(mainLine)
window.show()
app.exec_()