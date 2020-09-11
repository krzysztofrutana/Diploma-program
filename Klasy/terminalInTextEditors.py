from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QApplication


class MyStdoutLineText:
    def __init__(self, buffer):
        self.buffer = buffer

    def write(self, string):
        if string:
            if "Kolumny" in string:
                self.buffer.setText(string)
                QApplication.processEvents()

class MyStdoutTextEdit:
    def __init__(self, buffer):
        self.buffer = buffer

    def write(self, string):
        if string:
            if 'Test ilosci klastrow' in string or 'Liczenie eps' in string:

                self.buffer.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
                self.buffer.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                self.buffer.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
                storeCursorPos = self.buffer.textCursor()
                self.buffer.textCursor().removeSelectedText()
                self.buffer.textCursor().deletePreviousChar()
                self.buffer.setTextCursor(storeCursorPos)
                self.buffer.insertPlainText(string)
                self.buffer.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
            else:
                self.buffer.append(string)
                self.buffer.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
            QApplication.processEvents()