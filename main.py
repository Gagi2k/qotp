from PySide6 import QtCore, QtWidgets, QtGui

import pyotp
import time
import sys

class OTPTray():
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.menu = QtWidgets.QMenu()
        self.quitAction = QtGui.QAction("Quit")
        self.quitAction.triggered.connect(app.quit)
        self.menu.addAction(self.quitAction)

        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setContextMenu(self.menu)
        self.tray.setToolTip("OTP")
        self.tray.setIcon(QtGui.QIcon("otp.svg"))
        self.tray.setIcon(QtGui.QIcon.fromTheme(QtGui.QIcon.ThemeIcon.Phone))
        self.tray.activated.connect(self.copyOtp)
        self.tray.show()

        self.totp = pyotp.TOTP('CHANGE_ME')

    @QtCore.Slot()
    def copyOtp(self):
        self.app.clipboard().setText(self.totp.now())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    otptray = OTPTray(app)

    sys.exit(app.exec())
