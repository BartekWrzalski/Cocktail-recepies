from login_app import LoginApp
from PyQt5 import QtWidgets
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginApp()
    login.show()
    sys.exit(app.exec_())
