import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QPushButton, QTabWidget, QTimeEdit, QVBoxLayout,
                             QHBoxLayout, QLineEdit, QTableWidget, QDateEdit,
                             QMainWindow, QApplication, QMenu, QAction, QTextEdit, QLabel,
                             QFrame, QSplitter, QListWidget, QStyleFactory, QFileDialog, QFontDialog,
                             QColorDialog, QPlainTextEdit, QScroller, QScrollBar, QListWidgetItem, QDialog,
                             QProgressBar, QMessageBox)
from PyQt5.QtGui import QIcon, QFont, QColor, QPalette,QClipboard,QKeySequence
from PyQt5.QtCore import Qt
from time import sleep
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myclipboar = ""
        self.notebook = QTabWidget()
        self.notebook.setTabShape(QTabWidget.Triangular)
        self.notebook.setTabsClosable(1)
        self.notebook.setMovable(1)
        self.notebook.setStyleSheet("QTabWidget{background-color: rgb(46, 52, 54);}")
        self.name_with_path = []
        self.name_of_file = []
        self.text_edit_array = []
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.setGeometry(200, 300, 1000, 800)
        self.setWindowTitle("Nv Text Editor")
        self.main_page()

    def main_page(self):
        menu = self.menuBar()
        file = menu.addMenu("&File")
        menu.triggered.connect(self.which_action)
        edit = menu.addMenu("&Edit")
        tools = menu.addMenu("&Tools")
        help = menu.addMenu("&Help")

        # ____________________________________FILE______________________________________

        new = QAction("New", self)
        new.setShortcut("Ctrl+N")
        new.setStatusTip("Create a new File")
        new.triggered.connect(lambda: self.new_tab(name='Untitled'))
        open = QAction("Open", self)
        open.setStatusTip("Open a File")
        open.setShortcut("Ctrl+O")
        save = QAction("Save", self)
        save.setStatusTip("Save A File")
        save.setShortcut("Ctrl+S")
        saveas = QAction("Save as", self)
        saveas.setStatusTip("Save a file As")
        saveas.setShortcut("Ctrl+Alt+S")
        print = QAction("Print", self)
        print.setShortcut("Ctrl+P")
        print.setStatusTip("Print this file")
        exit = QAction("Exit", self)
        exit.setStatusTip("Quit Nv Text Editor")

        array1 = [new, open, save, saveas, print, exit]

        for i in range(len(array1)):
            if i == 1 or i == 4:
                file.addAction(array1[i])
                file.addSeparator()
            else:
                file.addAction(array1[i])

        # ___________________________________________________________________________________

        # ______________________________EDIT_____________________________________________how to

        redo = QAction("Redo", self)
        undo = QAction("Undo", self)

        copy = QAction("Copy",self)
        copy.setStatusTip("Copy")
        #copy.triggered.connect(self.textedit.copy)
        paste = QAction("Paste", self)
        #paste.triggered.connect(self.textedit.paste)
        cut = QAction("Cut", self)
        #cut.triggered.connect(self.textedit.cut)
        de = QAction("Del", self)

        fg = QAction("Foreground", self)
        bg = QAction("Background", self)
        font = QAction("Font", self)

        array2 = [redo, undo, copy, paste, cut, de, fg, bg, font]

        edit.addAction(QAction("Hello World"))

        for i in range(len(array2)):
            if i == 2 or i == 6 or i == 9:
                edit.addSeparator()
                edit.addAction(array2[i])
            else:
                edit.addAction(array2[i])
        # self.new_tab()
        self.menu_page()
        # ______________________________________________________________________________

        # ____________________________Tools_________________________________________________

        lang = tools.addMenu("<b>Select Language<b>")
        lang.addAction(QAction("C", self))
        lang.addAction(QAction("Python", self))

        com = QAction("Build", self)
        com.setShortcut("Ctrl+B")
        run = QAction("Run", self)
        run.setShortcut("Ctrl+F5")

        tools.addActions([com, run])

        # ____________________________________________________________________________________

        # ____________________________Help_______________________________________________________

        h = QAction("Documentation", self)
        about = QAction("About", self)

        help.addActions([h, about])

        # ______________________________________________________________________________________

    def index_of(self, txt):
        for i in self.name_with_path:
            if i == txt:
                return int(self.name_with_path.index(i))

    def new_tab(self, name="Untitled"):
        self.textedit = QPlainTextEdit()
        self.textedit.setTabStopWidth(10000)
        self.textedit.setTabStopDistance(QtGui.QFontMetricsF(self.textedit.font()).horizontalAdvance(' ') * 4)
        if name == "Untitled":
            name = name + ' ' + str(self.notebook.count() + 1)
            self.notebook.addTab(self.textedit, name)
            # f = open('main.py', 'r+')
            # self.textedit.setPlainText(f.read())
            self.textedit.setFocus()
            self.name_of_file.append(name)
            self.name_with_path.append(name)
            print(name,self.name_of_file.append(name)," ",self.name_with_path.append(name))
        else:
            print(name)
            if name in (self.name_with_path):
                self.notebook.setCurrentIndex(self.index_of(name))
                print(name + " :", self.index_of(name))
            else:
                with open(name, "r+") as f:
                    self.name_with_path.append(name)
                    p = name.split('/')
                    file = p[len(p) - 1]
                    self.name_of_file.append(file)
                    self.notebook.addTab(self.textedit, file)
                    self.textedit.setPlainText(f.read())
                    print(self.name_with_path)
        self.textedit.setFocus()
        self.textedit.setStyleSheet("QPlainTextEdit{background-color: rgb(46, 52, 54);color: rgb(186, 189, 182);}")
        # self.notebook.setCurrentIndex(self.notebook.currentIndex())
        self.notebook.setCurrentWidget(self.textedit)
        self.text_edit_array.append(self.textedit)
        print('Current Tab ' + self.notebook.tabText(self.notebook.currentIndex()))
    def index_of_tabname(self,name):
        for i in self.name_of_file:
            if i == name:
                return self.name_of_file.index(i)
    def menu_page(self):
        wid = QWidget()

        vbox = QVBoxLayout()
        vspl = QSplitter(Qt.Vertical)
        hspl = QSplitter(Qt.Horizontal)

        vspl.addWidget(hspl)
        self.List = QListWidget()
        self.List.setStyleSheet("QListWidget{background-color: rgb(46, 52, 54);color: rgb(186, 189, 182);}")
        self.List.addItems(os.listdir())
        self.List.currentItemChanged.connect(self.open_from_list)
        self.List.setVisible(0)
        hspl.addWidget(self.List)
        hspl.addWidget(self.notebook)
        vbox.addWidget(vspl)
        wid.setLayout(vbox)
        self.txt = QTextEdit()
        self.txt.setStyleSheet("QTextEdit{background-color: rgb(46, 52, 54);color: rgb(186, 189, 182);}")
        t = '"' + os.path.abspath('venv/python') + '"  "' + os.path.abspath('main.py') + '"'
        self.txt.setText(t)
        vspl.addWidget(self.txt)
        self.txt.setVisible(0)
        self.setCentralWidget(wid)
        self.notebook.tabCloseRequested.connect(self.close_tab)
        # QApplication.setStyle(QStyleFactory.create('cleanlooks'))
        self.new_tab()

    def open_from_list(self):
        txt = self.List.currentItem()
        self.new_tab(name=txt.text())
        # f = open(txt.text(),'a+')
        # self.notebook.currentWidget().setText(f.read())

    def close_tab(self, index):
        dial = QMessageBox()

        # v=QVBoxLayout()
        msg = "Your Changes will be lost if you don't save"
        resp = dial.question(self,"Do You Want To Save the changes You Made to "+self.notebook.tabText(self.notebook.currentIndex()),msg, dial.Save | dial.Cancel | dial.Discard)
        # v.addWidget(QLabel("Would you lisked to close "+self.notebook.tabText(self.notebook.currentIndex())))

        # dial.setLayout(v)
        if resp == QMessageBox.Discard:
            print(123)
            self.notebook.removeTab(index)

    def save(self):
        if self.notebook.tabText(self.notebook.currentIndex()).split(" ")[0] == "Untitled":

            file, _ = QFileDialog.getSaveFileName(self, 'Save File')
            with open(file, "w+") as f:
                f.write(self.textedit.toPlainText())
            # print('Current Tab ' + self.notebook.tabText(self.notebook.currentIndex()))
            p = file.split('/')
            p = str(p[len(p) - 1])
            ancien = self.notebook.tabText(self.notebook.currentIndex())
            self.name_with_path[self.index_of(ancien)] = file
            print(self.name_of_file,self.index_of(ancien))
            self.name_of_file[self.index_of(ancien)] = p
            self.notebook.setTabText(self.notebook.currentIndex(), p)
        else:
            file = self.notebook.tabText(self.notebook.currentIndex())
            with open(file, "w+") as f:
                f.write(self.textedit.toPlainText())
    def path(self,filedir,name):
        r = ''
        d = filedir.split('/')
        for i in range(len(d)):
            r += '/'+d[i]
        return r[1:]
    def build(self):
        if self.notebook.tabText(self.notebook.currentIndex()).split(" ")[0] == "Untitled":
            self.save()
            self.build()
        else:
            print('one ')
            tabname = self.notebook.tabText(self.notebook.currentIndex())
            pos = self.find_index(tabname)
            print("pos = ",pos)
            file = str(self.name_with_path[pos])
            print("file = ",file)
            path = self.path(file,tabname)
            print('path = ',path,' tabname = ',tabname)
            if tabname.endswith('.w'):
                os.system("gcc "+file+" -o "+path+'/'+tabname.split('.')[0])
                self.txt.setVisible(1)
                t = "gcc "+file+" -o "+path+'/'+tabname.split('.')[0]
                print('Compile path : = ',t)
                self.txt.setText("gcc "+file+" -o "+path+'/'+tabname.split('.')[0]+"\nCompled SuccesFully")
                print("compliled")
            if tabname.endswith('.py'):
                self.txt.setVisible(1)
                self.txt.setText(sys.executable +' '+ path)
                t = path
                print('t = ',t)
                print('text = ',sys.executable +' '+t)
                txt = str('python3') + " " + str(os.curdir()) + tabname
                os.system(txt)



    def find_index(self,tabname):
        for i in range(len(self.name_with_path)):
            print(self.name_with_path[i],"  ",self.name_with_path[i]," tab = ",tabname)
            t = self.name_with_path[i].split("/")
            print("split = ",t)
            n = t[len(t)-1]
            if n == tabname:
                return i
    def which_action(self, e):
        try:
            print(e.text())
        except:
            if isinstance(e,str):
                print(e)
        if e.text() == "Font":
            font, ok = QFontDialog().getFont()
            if ok:
                for i in self.text_edit_array:
                    i.setFont(QFont(font))

        if e.text() == 'Foreground':
            color = QPalette()
            color.setColor(QPalette.Text, QColorDialog().getColor())
            for i in self.text_edit_array:
                i.setPalette(color)
        if e.text() == 'Background':
            color = QColorDialog().getColor().getRgb()
            for i in self.text_edit_array:
                i.setStyleSheet('QPlainTextEdit{background-color:rgb' + str(color) + ';}')
        if e.text() == "Undo":
            self.textedit.undo()
        if e.text() == "Redo":
            self.textedit.redo()
        if e.text() == "Save":
            self.save()
        if e.text() == "Save as":
            file, _ = QFileDialog.getSaveFileName(self, 'Save As')
            with open(file, "w+") as f:
                f.write(self.textedit.toPlainText())
            # print('Current Tab ' + self.notebook.tabText(self.notebook.currentIndex()))
            p = file.split('/')
            p = str(p[len(p) - 1])
            ancien = self.notebook.tabText(self.notebook.currentIndex())
            self.name_with_path[self.index_of(ancien)] = file
            self.name_of_file[self.index_of(ancien)] = p
            self.notebook.setTabText(self.notebook.currentIndex(), p)

        if e.text() == "Open":
            self.textedit.cursor()
            file, _ = QFileDialog.getOpenFileName(self, "Open File", )
            print(file)
            self.new_tab(name=file)
            tabname = self.notebook.tabText(self.notebook.currentIndex())
            pos = self.find_index(tabname)
            print("pos = ",pos)
            file = str(self.name_with_path[pos])
            print("file = ",file)
            path = self.path(file,tabname)
            print(path)
            if tabname.endswith(".c"):
                os.system("gcc "+file+" -o "+path+'/'+tabname.split('.')[0])
                self.txt.setVisible(1)
                self.txt.setText("gcc "+file+" -o "+path+'/'+tabname.split('.')[0]+"\nCompled SuccesFully")
                print("compliled")
            # QFileDialog(self,"Open File",'/',(".c",'.py')).exec_()

        #____________________IMPORTANT PART IN THIS PROGRAM___________________________________-

        if e.text() == 'Run':
            tabname = self.notebook.tabText(self.notebook.currentIndex())
            pos = self.find_index(tabname)
            print("pos = ", pos)
            file = str(self.name_with_path[pos])
            print("file = ", file)
            path = self.path(file, tabname)
            print(path)
            if tabname.endswith(".c"):
                #os.system("gcc " + file + " -o " + path + '/' + tabname.split('.')[0])
                self.txt.setVisible(1)
                #self.txt.setText("gcc " + file + " -o " + path + '/' + tabname.split('.')[0] + "\nCompled SuccesFully")

        if e.text() == "Build":
            self.build()
        #________________________________________________________________________________________

        if e.text() == 'Copy':
            self.myclipboar = ""
            txt = self.textedit.textCursor()
            self.myclipboar = txt.selectedText()
            print(self.myclipboar)
        if e.text() == 'Paste':
            cur = self.textedit.textCursor()
            cur.insertText(self.myclipboar)
        if e.text() == 'About':
            wind = QDialog(self)
            wind.setWindowTitle("Nv Text Editor")
            vh = QVBoxLayout()
            txt1 = "Nv Text Editor\n"
            text = "Nv Text Editor Was created  By Tomdieu Ivan\n" \
                   "Version 1.0.0" \
                   ""
            txt2 = "Copyright ♾ 2020 - 2022"
            lb1 = QLabel()
            lb1.setAlignment(Qt.AlignCenter)
            lb1.setStyleSheet("font: 75 20pt " + "Ubuntu Condensed" + ";")
            lb1.setText(txt1)
            lb2 = QLabel()
            lb2.setAlignment(Qt.AlignCenter)
            # lb2.setStyleSheet("font: 75 20pt "+"Ubuntu Mono"+";")
            lb2.setText(txt2)
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            label.setText(text)
            vh.addWidget(lb1)
            vh.addWidget(label)
            vh.addWidget(lb2)
            wind.setLayout(vh)
            wind.exec_()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()
