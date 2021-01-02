import sqlite3
cxn = sqlite3.connect('/run/media/sudesh/random_bs/.sqlitedatabases/quizApp.db')
cursor = cxn.cursor()

import sys
from PySide6.QtWidgets import QApplication, QDialog, QStackedWidget
from PySide6.QtCore import Qt
from ui_quizDialog import Ui_Quiz

class QuizWindow(QDialog):
    def __init__(self):
        super(QuizWindow, self).__init__()
        self.ui = Ui_Quiz()
        self.ui.setupUi(self)
        self.ui.questionBox.setReadOnly(True)
        self.ui.questionBox.setAlignment(Qt.AlignCenter)
        self.selectedOption = None
        self.ui.option1.clicked.connect(lambda x: self.selectOption(x, self.ui.option1))
        self.ui.option2.clicked.connect(lambda x: self.selectOption(x, self.ui.option2))
        self.ui.option3.clicked.connect(lambda x: self.selectOption(x, self.ui.option3))
        self.ui.option4.clicked.connect(lambda x: self.selectOption(x, self.ui.option4))
        self.ui.submitButton.clicked.connect(self.submit)


    def submit(self):
        originalStyle = 'background-color:rgb(241, 213, 232);color:black;'
        correctStyle = 'background-color:rgb(71, 255, 20);color:black;'
        wrongStyle = 'background-color:rgb(255, 6, 18);color:black;'
        answer = ''
        if self.selectedOption:
            answer = self.selectedOption.text()
        else:
            print('option was not selected')
            return
        print(answer)

    def selectOption(self, x, option):
        originalStyle = 'background-color:rgb(241, 213, 232);color:black;'
        selectedStyle = 'background-color:rgb(50, 50, 50);'
        if x:
            if self.selectedOption:
                self.selectedOption.setChecked(False)
                self.selectedOption.setStyleSheet(originalStyle)
            option.setStyleSheet(selectedStyle)
            self.selectedOption = option
        else:
            option.setStyleSheet(originalStyle)
            self.selectedOption = None





if __name__=='__main__':
    app = QApplication(sys.argv)
    quizwindow = QuizWindow()
    widgets = QStackedWidget()
    widgets.addWidget(quizwindow)
    widgets.setFixedWidth(800)
    widgets.setFixedHeight(600)
    widgets.show()
    sys.exit(app.exec_())