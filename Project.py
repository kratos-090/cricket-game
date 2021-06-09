# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

#made by:Rohit Kumar


from PyQt5 import QtCore, QtGui, QtWidgets
from evaluatewindow import Ui_Form
import sqlite3
mydb=sqlite3.connect('database.db')
curdb=mydb.cursor()


class Ui_MainWindow(object):



        #evaluate function menu
    def evaluate_menu(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(Dialog)
        ret=Dialog.exec()

        #quit menu function
    def quit_menu(self):
        sys.exit()





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 580)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Team = QtWidgets.QHBoxLayout()
        self.Team.setObjectName("Team")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(0, 20, -1, 20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Batsman = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Batsman.setFont(font)
        self.Batsman.setTabletTracking(False)
        self.Batsman.setAcceptDrops(False)
        self.Batsman.setToolTipDuration(20)
        self.Batsman.setStyleSheet("Batmans")
        self.Batsman.setObjectName("Batsman")
        self.gridLayout_3.addWidget(self.Batsman, 0, 0, 1, 1)
        self.Wicketkeeper = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeper.setFont(font)
        self.Wicketkeeper.setObjectName("Wicketkeeper")
        self.gridLayout_3.addWidget(self.Wicketkeeper, 0, 1, 1, 1)
        self.Allrounder = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setChecked(False)
        self.Allrounder.setObjectName("Allrounder")
        self.gridLayout_3.addWidget(self.Allrounder, 0, 2, 1, 1)
        self.Bowler = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Bowler.setFont(font)
        self.Bowler.setObjectName("Bowler")
        self.gridLayout_3.addWidget(self.Bowler, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.Team.addLayout(self.gridLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.TeamName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setStyleSheet("color: rgb(0, 0, 255);")
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_4.addWidget(self.TeamName)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.Team.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.Team, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.PointsAvailable = QtWidgets.QLabel(self.centralwidget)
        self.PointsAvailable.setStyleSheet("color: rgb(0, 0, 255);")
        self.PointsAvailable.setObjectName("PointsAvailable")
        self.horizontalLayout_2.addWidget(self.PointsAvailable)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.PointCount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PointCount.setFont(font)
        self.PointCount.setStyleSheet("color: rgb(0, 0, 255);")
        self.PointCount.setObjectName("PointCount")
        self.horizontalLayout_2.addWidget(self.PointCount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bt.setFont(font)
        self.bt.setIndent(1)
        self.bt.setObjectName("bt")
        self.horizontalLayout.addWidget(self.bt)
        self.Batcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Batcount.setFont(font)
        self.Batcount.setStyleSheet("color: rgb(0, 0, 255);")
        self.Batcount.setObjectName("Batcount")
        self.horizontalLayout.addWidget(self.Batcount)
        self.wk = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wk.setFont(font)
        self.wk.setObjectName("wk")
        self.horizontalLayout.addWidget(self.wk)
        self.Wkcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Wkcount.setFont(font)
        self.Wkcount.setStyleSheet("color: rgb(0, 0, 255);")
        self.Wkcount.setIndent(10)
        self.Wkcount.setObjectName("Wkcount")
        self.horizontalLayout.addWidget(self.Wkcount)
        self.ar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ar.setFont(font)
        self.ar.setObjectName("ar")
        self.horizontalLayout.addWidget(self.ar)
        self.Alrcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Alrcount.setFont(font)
        self.Alrcount.setStyleSheet("color: rgb(0, 0, 255);")
        self.Alrcount.setIndent(10)
        self.Alrcount.setObjectName("Alrcount")
        self.horizontalLayout.addWidget(self.Alrcount)
        self.bow = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bow.setFont(font)
        self.bow.setObjectName("bow")
        self.horizontalLayout.addWidget(self.bow)
        self.Bowlcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlcount.setFont(font)
        self.Bowlcount.setStyleSheet("color: rgb(0, 0, 255);")
        self.Bowlcount.setIndent(10)
        self.Bowlcount.setObjectName("Bowlcount")
        self.horizontalLayout.addWidget(self.Bowlcount)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #new team menu bar
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")


        #open team menu bar
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")

        #save team menu bar
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")


        #evalute team menu bar
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionEvaluate_Team.triggered.connect(self.evaluate_menu)

        #quit menu bar
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.quit_menu)


        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)




        self.menuManage_Teams.addAction(self.actionQuit)
        self.menubar.addAction(self.menuManage_Teams.menuAction())


        #listWidget function
        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)




        #radio button function
        self.Batsman.toggled.connect(self.ctg)
        self.Wicketkeeper.toggled.connect(self.ctg)
        self.Bowler.toggled.connect(self.ctg)
        self.Allrounder.toggled.connect(self.ctg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #menu bar sunction
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)

        #default values
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Batsman.setText(_translate("MainWindow", "Batsman"))
        self.Wicketkeeper.setText(_translate("MainWindow", "WicketKeeper"))
        self.Allrounder.setText(_translate("MainWindow", "AllRounder"))
        self.Bowler.setText(_translate("MainWindow", "Bowler"))
        self.label_3.setText(_translate("MainWindow", "Team Name:"))
        self.TeamName.setText(_translate("MainWindow", "########"))
        self.label_2.setText(_translate("MainWindow", "Points Available:"))
        self.PointsAvailable.setText(_translate("MainWindow", "###"))
        self.label_5.setText(_translate("MainWindow", "Points Used:"))
        self.PointCount.setText(_translate("MainWindow", "###"))
        self.label_4.setText(_translate("MainWindow", "Your Selection:"))
        self.bt.setText(_translate("MainWindow", "Batsman(Bat)"))
        self.Batcount.setText(_translate("MainWindow", "##"))
        self.wk.setText(_translate("MainWindow", "WicketKeeper(WK)"))
        self.Wkcount.setText(_translate("MainWindow", "##"))
        self.ar.setText(_translate("MainWindow", "Allrounder (ALR)"))
        self.Alrcount.setText(_translate("MainWindow", "##"))
        self.bow.setText(_translate("MainWindow", "Bowlers (Bowl)"))
        self.Bowlcount.setText(_translate("MainWindow", "##"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionNew_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionOpen_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionSave_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionEvaluate_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Esc"))

#######################################################################################

#show value function
    def show(self):
        self.Batcount.setText(str(self.bat))
        self.Bowlcount.setText(str(self.bwl))
        self.Alrcount.setText(str(self.ar))
        self.Wkcount.setText(str(self.wk))
        self.PointsAvailable.setText(str(self.avl))
        self.PointCount.setText(str(self.used))


########################################################################################

#menu bar function
    def menu(self,action):
        txt=(action.text())

        if txt=='New Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.listWidget_2.clear()
            self.listWidget.clear()
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
            if ok:
                self.TeamName.setText(str(text))

            self.show()

        if txt=='Save Team':
            count=self.listWidget.count()
            selected=""
            for i in range(count):
                selected+=self.listWidget.item(i).text()
                if i<count:
                    selected+=","
            self.saveteam(self.TeamName.text(),selected,self.used)

        if txt=='Open Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.listWidget_2.clear()
            self.listWidget.clear()
            self.show()
            self.openteam()

#################################################################################################

#criteria function
    def criteria(self,ctgr,item):

        sql="select value from stats where player='"+item.text()+"'"
        cur=curdb.execute(sql)
        row=cur.fetchone()


        msg=''
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
        if ctgr=="BWL" and self.bwl>=5:msg="bowlers not more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
        if self.used+int(row[0])>=1000:msg="All points used"
        if msg!='':
            self.showdlg(msg)
            return False

        if self.avl<=0:
            msg="You Have Exhausted your Points"
            self.showdlg(msg)
            return False

        if ctgr=="BAT":self.bat+=1
        if ctgr=="BWL":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1



        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True

#########################################################################################################3

    def removelist1(self,item):

        if self.bat+self.bwl+self.ar+self.wk>=11:
            self.showdlg(" Team complete (11 players selected)")
            return

            printf(self.used)

        if self.used>=1000:
            self.showdlg("All points used select diffrent player")
            return

        ctgr=''
        if self.Batsman.isChecked()==True:ctgr='BAT'
        if self.Bowler.isChecked()==True:ctgr='BWL'
        if self.Allrounder.isChecked()==True:ctgr='AR'
        if self.Wicketkeeper.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr,item)

        if ret==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))

            self.listWidget.addItem(item.text())
            self.show()


############################################################################################################



    #radio button function
    def ctg(self):
        ctgr=''
        if self.Batsman.isChecked()==True:ctgr='BAT'
        if self.Wicketkeeper.isChecked()==True:ctgr='WK'
        if self.Bowler.isChecked()==True:ctgr='BWL'
        if self.Allrounder.isChecked()==True:ctgr='AR'
        self.fillList(ctgr)


    #########################################################################################################



    def removelist2(self,item):
        self.listWidget.takeItem(self.listWidget.row(item))

        cursor = curdb.execute("SELECT player,value, ctg from stats where player='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.Batsman.isChecked()==True:self.listWidget_2.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.Bowler.isChecked()==True:self.listWidget_2.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.Allrounder.isChecked()==True:self.listWidget_2.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.Wicketkeeper.isChecked()==True:self.listWidget_2.addItem(item.text())
        self.show()
##########################################################################################################



    def fillList(self,ctgr):
        if self.TeamName.text()=='########':
            self.showdlg("Enter name of team")
            return

        self.listWidget_2.clear()
        sql="select players from players where ctg='"+ctgr+"';"
        cur=curdb.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.listWidget.count()):
                selected.append(self.listWidget.item(i).text())
            if row[0] not in selected:self.listWidget_2.addItem(row[0])

#############################################################################################


    def openteam(self):

        sql="select name from teams;"
        cur=curdb.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])

        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.TeamName.setText(str(team))

        sql1="SELECT players,value from teams where name='"+team+"';"
        cur=curdb.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.listWidget.addItems(selected)
        self.used=row[1]

        self.avl=1000-row[1]
        count=self.listWidget.count()

        for i in range(count-1):
            ply=self.listWidget.item(i).text()
            sql="select ctg from stats where player='"+ply+"';"

            cur=curdb.execute(sql)

            row=cur.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1

        self.show()

####################################################################################################

    def saveteam(self,nm,ply,val):
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Insufficient players")
            return

        sql="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        try:
            cur=curdb.execute(sql)
            self.showdlg("Team Saved Succesfully")
            mydb.commit()
        except:
            self.showdlg("Error in Operation")
            mydb.rollback()

#######################################################################################################

    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle('Training Project:Made By Rohit Kumar')
        ret=Dialog.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
