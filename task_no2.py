from PySide2 import QtCore, QtGui
import sys
from ui import Ui_Form

app = QtGui.QApplication(sys.argv)
 
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

def bp_Create():
    ui.lineEdit.setText('Create'[::-1])
ui.Create.clicked.connect(bp_create)

def bp_Find():
    ui.lineEdit.setText('Find'[::-1])
ui.Find.clicked.connect(bp_Find)

def bp_Edit():
    ui.lineEdit.setText('Edit'[::-1])
ui.Edit.clicked.connect(bp_Edit)

def bp_Delete():
    ui.lineEdit.del_()
ui.Delete.clicked.connect(bp_Delete)

def bp_Exit():
    QtCore.QtCoreApplication.instance().quit
ui.Exit.clicked.connect(bp_Exit)

sys.exit(app.exec_())