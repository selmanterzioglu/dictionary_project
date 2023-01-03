from PyQt5.QtWidgets import QMessageBox

def msg_box(title, text):
    dlg = QMessageBox()
    dlg.setWindowTitle(title)
    dlg.setText(text)
    button = dlg.exec()
    