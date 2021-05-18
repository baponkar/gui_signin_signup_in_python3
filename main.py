'''
Reference : https://www.mfitzp.com/tutorials/creating-dialogs-qt-designer/
Build Date : 18/05/2021
Builder Name : Bapon Kar
Last Update : 18/05/2021
Download link : https://github.com/baponkar/gui_signin_signup_in_python 
'''

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from welcome import Ui_WelcomeDialog
from signup_wind import Ui_SignUpDialog
from signin_wind import Ui_MainWindow
from sign_in import sign_in
from sign_up import sign_up



class MainWindow(QMainWindow):
	'''Main Window from Ui_MainWindow'''
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.button = self.ui.setupUi(self).pushButton
		self.ui.pushButton.clicked.connect(self.onSignInBtnClicked)
		self.ui.pushButton_2.clicked.connect(self.onSignUpBtnClicked)
	# Create a slot for launching the welcome dialog
	def onSignInBtnClicked(self):
		self.u = self.ui.textEdit.toPlainText()
		self.p = self.ui.lineEdit.text()
		#print("Username : ",self.u)
		#print("Password : ",self.p)
		self.flag = sign_in(self.u,self.p)
		if self.flag:
			"""Launch the employee dialog."""
			win.hide()
			dlg = EmployeeDlg(self)
			dlg.exec()
		else:
			self.ui.label_3.setText("Your Username or Password is wrong!")
	def val(self):
		return self.u
		#self.ui.labelResponse.setText("Hello")
        	#self.ui.labelResponse.setText("Hello "/
        	#+self.ui.lineEditName.text())
        	
	def onSignUpBtnClicked(self):
		win.hide()
		dlg = SignUpDialog(self)
		dlg.exec()	

class EmployeeDlg(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_WelcomeDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.setWindowTitle(win.val())
        self.ui.label_2.setText("Welcome " + win.val().capitalize())

class SignUpDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_SignUpDialog()
		self.ui.setupUi(self)
		self.setWindowTitle("SignUP")
		self.ui.pushButton.clicked.connect(self.onSignUpBtnClicked)
	def onSignUpBtnClicked(self):
		self.u = self.ui.textEdit.toPlainText()
		self.p = self.ui.lineEdit.text()
		self.flag = sign_up(self.u,self.p)
		if self.flag:
			self.ui.label_3.setText("Your user ID created successfully!")
		else:
			self.ui.label_3.setText("Sorry same user already in exists!")
					


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the application's main window
    #win = Window()
    win = MainWindow()  
    win.show()
    # Run the application's main loop
    sys.exit(app.exec())

