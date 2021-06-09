# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copy.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math
import random
import sqlite3
mydb=sqlite3.connect('database.db')
curdb=mydb.cursor()



class Ui_Form(object):

############################################################################################

    def calculate(self):
        team=self.cb0.currentText()
        self.lw1.clear()
        sql1="select players, value from teams where name='"+team+"'"
        cur=curdb.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.lw1.addItems(selected)
        teamttl=0
        self.lw2.clear()
        match=self.cb1.currentText()
        for i in range((self.lw1.count())-1):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.lw1.item(i).text()
            cursor=curdb.execute("select * from match where player='"+nm+"'")
            row=cursor.fetchone()
            row1=(random.randint(0,row[1]))
            row2=(random.randint(0,row[2]))
            row3=(random.randint(0,row[3]))
            row4=(random.randint(0,row[4]))
            row5=(random.randint(0,row[5]))
            row6=(random.randint(0,row[6]))
            row7=(random.randint(0,row[7]))
            row8=(random.randint(0,row[8]))
            row9=(random.randint(0,row[9]))
            row10=(random.randint(0,row[10]))
            row11=(random.randint(0,row[11]))
            try:
                batscore=int(row1/2)
            except:
                batscore=0
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row1>0:
                try:
                    sr=row1/row2
                except:
                    sr=0
                if sr>=80 and sr<100: batscore+=2
                if sr>=100:batscore+=4
            batscore=batscore+row3
            batscore=batscore+2*row4
            bowlscore=row8*10
            if row8>=3: bowlscore=bowlscore+5
            if row8>=5: bowlscore=bowlscore=bowlscore+10
            if row7>0:
                try:
                    er=6*row7/row5
                except:
                    er=0
                if er<=2: bowlscore=bowlscore+10
                if er>2 and er<=3.5: bowlscore=bowlscore+7
                if er>3.5 and er<=4.5: bowlscore=bowlscore+4
            fieldscore=(row9+row10+row11)*10
            ttl=batscore+bowlscore+fieldscore
            self.lw2.addItem(str(ttl))
            teamttl=teamttl+ttl
        self.score.setText(str(teamttl))

#################################################################################################



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cb0 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.cb0.setFont(font)
        self.cb0.setObjectName("cb0")
        self.horizontalLayout.addWidget(self.cb0)
#############################################################################################


        sql="select name from teams"
        cur=curdb.execute(sql)
        teams=[]
        for row in cur:
            self.cb0.addItem(row[0])


########################################################################################################

        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb1 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.cb1.setFont(font)
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.horizontalLayout.addWidget(self.cb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lw1 = QtWidgets.QListWidget(Form)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_3.addWidget(self.lw1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.lw2 = QtWidgets.QListWidget(Form)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_3.addWidget(self.lw2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)



        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)



        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.score = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.horizontalLayout_4.addWidget(self.score)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Choose Team"))
        self.label.setText(_translate("Form", "Choose Match"))
        self.cb1.setItemText(0, _translate("Form", "Match1"))
        self.cb1.setItemText(1, _translate("Form", "Match2"))
        self.cb1.setItemText(2, _translate("Form", "Match3"))
        self.cb1.setItemText(3, _translate("Form", "Match4"))
        self.cb1.setItemText(4, _translate("Form", "Match5"))
        self.label_4.setText(_translate("Form", "Player"))
        self.label_3.setText(_translate("Form", "Score"))
        self.pushButton.setText(_translate("Form", "Claculate"))
        self.score.setText(_translate("Form", "00"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
