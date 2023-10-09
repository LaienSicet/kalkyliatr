from PyQt5 import QtCore, QtGui, QtWidgets

STROKA = ""   #строка в "экране" колькулятора
sohran = ["", "", ""] # сохранённые числа
kotel = [] #  прошлое число и тд
vvod = False #маркер ввода

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 100, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 5, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")



        if sohran[0] != "":
            self.pushButton_s_1 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_s_1.setGeometry(QtCore.QRect(20, 30, 130, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_s_1.setFont(font)
            self.pushButton_s_1.clicked.connect(kno_soh_1)
            self.pushButton_s_1.setObjectName("pushButton_s_1")

        if sohran[1] != "":
            self.pushButton_s_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_s_2.setGeometry(QtCore.QRect(185, 30, 130, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_s_2.setFont(font)
            self.pushButton_s_2.clicked.connect(kno_soh_2)
            self.pushButton_s_2.setObjectName("pushButton_s_2")

        if sohran[2] != "":
            self.pushButton_s_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_s_3.setGeometry(QtCore.QRect(350, 30, 130, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_s_3.setFont(font)
            self.pushButton_s_3.clicked.connect(kno_soh_3)
            self.pushButton_s_3.setObjectName("pushButton_s_3")


        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(125, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.clicked.connect(lambda: kno_0("1"))
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(215, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(lambda: kno_0("2"))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(305, 180, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(lambda: kno_0("3"))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(125, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.clicked.connect(lambda: kno_0("4"))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(215, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.clicked.connect(lambda: kno_0("5"))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(305, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.clicked.connect(lambda: kno_0("6"))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(125, 360, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.clicked.connect(lambda: kno_0("7"))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(215, 360, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.clicked.connect(lambda: kno_0("8"))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(305, 360, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.clicked.connect(lambda: kno_0("9"))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(215, 450, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_0.setFont(font)
        self.pushButton_0.clicked.connect(lambda: kno_0("0"))
        self.pushButton_0.setObjectName("pushBut0ton_0")

        self.pushButton_00 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_00.setGeometry(QtCore.QRect(125, 450, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_00.setFont(font)
        self.pushButton_00.clicked.connect(kno_00)
        self.pushButton_00.setObjectName("pushButton_00")

        self.pushButton_pl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pl.setGeometry(QtCore.QRect(10, 250, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_pl.setFont(font)
        self.pushButton_pl.clicked.connect(lambda: kno_deistvie("+"))
        self.pushButton_pl.setObjectName("pushButton_pl")

        self.pushButton_mi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mi.setGeometry(QtCore.QRect(400, 250, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mi.setFont(font)
        self.pushButton_mi.clicked.connect(lambda: kno_deistvie("-"))
        self.pushButton_mi.setObjectName("pushButton_mi")

        self.pushButton_ym = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ym.setGeometry(QtCore.QRect(10, 360, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ym.setFont(font)
        self.pushButton_ym.clicked.connect(lambda: kno_deistvie("x"))
        self.pushButton_ym.setObjectName("pushButton_ym")

        self.pushButton_de = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_de.setGeometry(QtCore.QRect(400, 360, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_de.setFont(font)
        self.pushButton_de.clicked.connect(lambda: kno_deistvie(":"))
        self.pushButton_de.setObjectName("pushButton_de")

        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(400, 100, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_del.setFont(font)
        self.pushButton_del.clicked.connect(de_ll)
        self.pushButton_del.setObjectName("pushButton_del")

        self.pushButton_RO = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RO.setGeometry(QtCore.QRect(305, 470, 185, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_RO.setFont(font)
        self.pushButton_RO.clicked.connect(kno_ravno)
        self.pushButton_RO.setObjectName("pushButton_RO")

        self.pushButton_cohr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cohr.setGeometry(QtCore.QRect(20, 100, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cohr.setFont(font)
        self.pushButton_cohr.clicked.connect(so_hr)
        self.pushButton_cohr.setObjectName("pushButton_cohr")

        self.pushButton_sbros = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sbros.setGeometry(QtCore.QRect(10, 470, 90, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sbros.setFont(font)
        self.pushButton_sbros.clicked.connect(sbros)
        self.pushButton_sbros.setObjectName("pushButton_cohr")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 570, 820, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "калькулятор"))

        if sohran[0] != "":
            self.pushButton_s_1.setText(_translate("MainWindow", sohran[0]))
        if sohran[1] != "":
            self.pushButton_s_2.setText(_translate("MainWindow", sohran[1]))
        if sohran[2] != "":
            self.pushButton_s_3.setText(_translate("MainWindow", sohran[2]))

        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_00.setText(_translate("MainWindow", ","))

        self.pushButton_pl.setText(_translate("MainWindow", "+"))
        self.pushButton_mi.setText(_translate("MainWindow", "-"))
        self.pushButton_ym.setText(_translate("MainWindow", "x"))
        self.pushButton_de.setText(_translate("MainWindow", ":"))

        self.pushButton_del.setText(_translate("MainWindow", "<del"))
        self.pushButton_RO.setText(_translate("MainWindow", "="))
        self.pushButton_cohr.setText(_translate("MainWindow", "сохр."))
        self.pushButton_sbros.setText(_translate("MainWindow", "сброс"))
        self.label.setText(_translate("MainWindow", "")) #*тех. строка***************************
        self.label_11.setText(_translate("MainWindow", "разработчик Тарасов Д. Л."))

        self.textBrowser.setText(p_minys_0(STROKA))


def sbros():
    'сброс'
    global STROKA, sohran, kotel, vvod
    STROKA = ""
    sohran = ["", "", ""]
    kotel = []
    vvod = False
    ui.setupUi(MainWindow)


def kno_0(a):
    'ввод цифры'
    ui.label.setText("")
    global STROKA, vvod
    if vvod == False:
        STROKA= ""
        vvod = True
    if len(STROKA) < 12:
        STROKA += a
    ui.textBrowser.setText(p_minys_0(STROKA))


def kno_00():
    'ввод запятой'
    ui.label.setText("")
    global STROKA
    if 0 < len(STROKA) < 12 and not("." in STROKA) and vvod == True:
        STROKA += "."
    ui.textBrowser.setText(STROKA)


def de_ll():
    'удаление'
    ui.label.setText("")
    global STROKA
    if len(STROKA) > 0 and vvod == True:
        STROKA = STROKA[0:len(STROKA)-1]
    ui.textBrowser.setText(p_minys_0(STROKA))


def so_hr():
    'сохранение'
    ui.label.setText("")
    global sohran, STROKA
    if STROKA == "":
        return False
    try:
        a = float(ui.textBrowser.toPlainText())
        if a % 1 == 0:
            a = int(a)
    except:
        return False
    if a == 0:
        return False
    q = 0
    for j, i in enumerate(sohran):
        if i == "" and q == 0:
            sohran[j] = str(a)
            q = 1
    if q == 0:
        sohran.append(str(a))
    STROKA = ""
    ui.textBrowser.setText(STROKA)
    if len(sohran) > 3:
        del sohran[0]
    ui.setupUi(MainWindow)


def kno_soh_1():
    'вызов сохр. значения'
    global sohran, STROKA
    STROKA = sohran[0]
    ui.textBrowser.setText(STROKA)
    sohran[0] = ""
    ui.setupUi(MainWindow)


def kno_soh_2():
    'вызов сохр. значения'
    global sohran, STROKA
    STROKA = sohran[1]
    ui.textBrowser.setText(STROKA)
    sohran[1] = ""
    ui.setupUi(MainWindow)


def kno_soh_3():
    'вызов сохр. значения'
    global sohran, STROKA
    STROKA = sohran[2]
    ui.textBrowser.setText(STROKA)
    sohran[2] = ""
    ui.setupUi(MainWindow)


def kno_deistvie(a):
    '+, -, :, x'
    ui.label.setText("")
    global kotel, STROKA, vvod
    if len(STROKA) == 0:
        return False
    try:
        s = float(STROKA)
    except:
        return False
    vvod = False
    kotel.append(s)
    kotel.append(a)
    if len(kotel) > 3:
        STROKA = shet(kotel[len(kotel)-4], kotel[len(kotel)-3], kotel[len(kotel)-2])

        kotel = [float(kotel[len(kotel)-2]), a]
    ui.textBrowser.setText(p_minys_0(STROKA))


def kno_ravno():
    '='
    ui.label.setText("")
    global kotel, STROKA, vvod
    if len(STROKA) == 0 or len(kotel) < 2:
        return False
    try:
        s = float(STROKA)
    except:
        return False
    vvod = False
    kotel.append(s)
    if kotel[len(kotel) - 1] == 0 and kotel[len(kotel) - 2] == ":":
        STROKA = ""
        kotel = []
        vvod = False
        ui.setupUi(MainWindow)
        ui.label.setText("на 0 делить нельзя.")
        return False

    STROKA = shet(kotel[len(kotel) - 3], kotel[len(kotel) - 2], kotel[len(kotel) - 1])
    ui.textBrowser.setText(p_minys_0(STROKA))
    kotel = []


def shet(a_1, d, a_2):
    'осуществление действия'
    if d == "+":
        return str(a_1 + a_2)
    elif d == "-":
        return str(a_1 - a_2)
    elif d == "x":
        return str(a_1 * a_2)
    elif d == ":":
        return str(a_1 / a_2)


def p_minys_0(a):
    'подгонка результата для отображения в окне.'
    if len(a) > 12 and float(a) % 1 != 0:
        a = a[0:12:]
        ui.label.setText("Произведено округление значения.")
    elif len(a) > 12:
        ui.label.setText("Ошибка: превышение диапазона.")
        return ""

    if len(a) != 0:
        a = float(a)
        if float(a) % 1 == 0:
            return str(int(a))
        else:
            return str(a)
    else:
        return a


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
