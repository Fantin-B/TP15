from PySide2.QtWidgets import *

#étape1
class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.__text = text

        self.layout = QHBoxLayout()

        self.label = QLabel(self.__text)
        self.TextEdit = QTextEdit()
        self.TextEdit.setMaximumHeight(30)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.TextEdit)

        self.setLayout(self.layout)


class ConfigurationDialog(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.layout = QVBoxLayout()
        self.labelTextField1 = LabeledTextField("IP address")
        self.labelTextField2 = LabeledTextField("User")
        self.labelTextField3 = LabeledTextField("Password")

        self.layout.addWidget(self.labelTextField1)
        self.layout.addWidget(self.labelTextField2)
        self.layout.addWidget(self.labelTextField3)

        self.setLayout(self.layout)
