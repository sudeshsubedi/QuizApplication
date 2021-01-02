# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Quiz(object):
    def setupUi(self, Quiz):
        if not Quiz.objectName():
            Quiz.setObjectName(u"Quiz")
        Quiz.resize(766, 563)
        Quiz.setStyleSheet(u"background-color:rgb(20, 53, 100)\n"
"")
        self.label = QLabel(Quiz)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 20, 231, 21))
        self.label.setStyleSheet(u"font: 75 16pt \"Inconsolata Expanded Bold\";\n"
"color:rgb(123, 67, 27)")
        self.questionBox = QTextEdit(Quiz)
        self.questionBox.setObjectName(u"questionBox")
        self.questionBox.setGeometry(QRect(40, 80, 711, 87))
        self.questionBox.setStyleSheet(u"font: 87 italic 14pt \"Noto Sans\";\n"
"color: Black;")
        self.option1 = QPushButton(Quiz)
        self.option1.setObjectName(u"option1")
        self.option1.setGeometry(QRect(40, 190, 311, 61))
        self.option1.setStyleSheet(u"background-color:rgb(241, 213, 232);\n"
"color:black;\n"
"")
        self.option1.setCheckable(True)
        self.option2 = QPushButton(Quiz)
        self.option2.setObjectName(u"option2")
        self.option2.setGeometry(QRect(440, 190, 311, 61))
        self.option2.setStyleSheet(u"background-color:rgb(241, 213, 232);\n"
"color:black;")
        self.option2.setCheckable(True)
        self.option4 = QPushButton(Quiz)
        self.option4.setObjectName(u"option4")
        self.option4.setGeometry(QRect(440, 300, 311, 61))
        self.option4.setStyleSheet(u"background-color:rgb(241, 213, 232);\n"
"color:black;")
        self.option4.setCheckable(True)
        self.option3 = QPushButton(Quiz)
        self.option3.setObjectName(u"option3")
        self.option3.setGeometry(QRect(40, 300, 311, 61))
        self.option3.setStyleSheet(u"background-color:rgb(241, 213, 232);\n"
"color:black;")
        self.option3.setCheckable(True)
        self.submitButton = QPushButton(Quiz)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(330, 420, 121, 41))
        self.submitButton.setStyleSheet(u"background-color:rgb(241, 213, 232);\n"
"color:black;")

        self.retranslateUi(Quiz)

        QMetaObject.connectSlotsByName(Quiz)
    # setupUi

    def retranslateUi(self, Quiz):
        Quiz.setWindowTitle(QCoreApplication.translate("Quiz", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Quiz", u"Generic Quiz Title", None))
        self.questionBox.setHtml(QCoreApplication.translate("Quiz", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:14pt; font-weight:80; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Which movie won the oscar this year?</p></body></html>", None))
        self.option1.setText(QCoreApplication.translate("Quiz", u"Marriage Story", None))
        self.option2.setText(QCoreApplication.translate("Quiz", u"Parasite", None))
        self.option4.setText(QCoreApplication.translate("Quiz", u"Irishmen", None))
        self.option3.setText(QCoreApplication.translate("Quiz", u"Joker", None))
        self.submitButton.setText(QCoreApplication.translate("Quiz", u"Submit", None))
    # retranslateUi

