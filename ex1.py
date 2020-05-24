from PySide2.QtWidgets import *
from ex2 import *
#étape1
class SQLClientWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()

        self.Buttons = ButtonsPanel()
        self.layout.addWidget(self.Buttons)

        self.notificationPanel = QTextEdit()
        self.layout.addWidget(self.notificationPanel)

        self.resultTable = QTableWidget(5,3)
        self.layout.addWidget(self.resultTable)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setLayout(self.layout)


#étape2
class ButtonsPanel(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.ButtonConfig = QPushButton("Configure")
        self.ButtonConn = QPushButton("Connect")
        self.ButtonDisconn = QPushButton("Disconnect")

        self.layout.addWidget(self.ButtonConfig)
        self.layout.addWidget(self.ButtonConn)
        self.layout.addWidget(self.ButtonDisconn)

        self.setLayout(self.layout)




if __name__ == "__main__" :
    app = QApplication([])
    win = SQLClientWindow()
    win2 = ConfigurationDialog()
    win.show()
    win2.show()
    app.exec_()

print("u")
