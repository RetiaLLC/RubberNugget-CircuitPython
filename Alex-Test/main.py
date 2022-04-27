import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication


class ExitButton(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('CKing')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = ExitButton()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
