"""Script for Qt GUI client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
#import form
import newform
import ctypes  # An included library with Python install.

import time


class ExampleApp(QtWidgets.QMainWindow, newform.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле form.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.label_2.setText("1")
        self.plainTextEdit.setMaximumBlockCount(1)
        self.plainTextEdit.setReadOnly(1)
        self.pushButton_6.clicked.connect(self.next_question)
        self.pushButton_2.clicked.connect(self.var4)
        self.pushButton_3.clicked.connect(self.var3)
        self.pushButton_4.clicked.connect(self.var2)
        self.pushButton_5.clicked.connect(self.var1)

    def next_question(self):
        global res
        self.active()
        self.pushButton_5.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(buttom_color.jpg);\n""")
        self.pushButton_4.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(buttom_color.jpg);\n""")
        self.pushButton_3.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(buttom_color.jpg);\n""")
        self.pushButton_2.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(buttom_color.jpg);\n""")
        #send()
        msg = self.label_2.text()
        next = int(msg) + 1
        if(next != 17):
            self.label_2.setText(str(next))
            send()
        else:
            ctypes.windll.user32.MessageBoxW(0, "Ваш результат "+str(res)+"/16", "Результат", 1)
            self.close()

    def nonactive(self):

        self.pushButton_5.setEnabled(0)

        self.pushButton_4.setEnabled(0)

        self.pushButton_3.setEnabled(0)

        self.pushButton_2.setEnabled(0)

    def active(self):

        self.pushButton_5.setEnabled(1)

        self.pushButton_4.setEnabled(1)

        self.pushButton_3.setEnabled(1)

        self.pushButton_2.setEnabled(1)

    def true(self):
        global an
        if (an == "1"):
            self.pushButton_5.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
        if (an == "2"):
            self.pushButton_4.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
        if (an == "3"):
            self.pushButton_3.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
        if (an == "4"):
            self.pushButton_2.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")



    def var1(self):
        global an
        global res
        if(an == "1"):
            self.pushButton_5.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
            res = res + 1
        else:
            self.pushButton_5.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_wrong_answer.jpg);\n""")
            self.true()
        self.nonactive()

    def var2(self):
        global an
        global res
        if (an == "2"):
            self.pushButton_4.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
            res = res + 1
        else:
            self.pushButton_4.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_wrong_answer.jpg);\n""")
            self.true()
        self.nonactive()

    def var3(self):
        global an
        global res
        if (an == "3"):
            self.pushButton_3.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
            res = res + 1
        else:
            self.pushButton_3.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_wrong_answer.jpg);\n""")
            self.true()
        self.nonactive()

    def var4(self):
        global an
        global res
        if (an == "4"):
            self.pushButton_2.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_true_answer.jpg);\n""")
            res = res + 1
        else:
            self.pushButton_2.setStyleSheet("color: rgb(0, 122, 89);\n""border-image: url(button_wrong_answer.jpg);\n""")
            self.true()
        self.nonactive()

def receive():
    global an
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            #header.config(text=msg)
            time.sleep(0.05)
            data1 = client_socket.recv(BUFSIZ).decode()
            #first.config(text=data1)
            time.sleep(0.05)
            data2 = client_socket.recv(BUFSIZ).decode()
            #second.config(text=data2)
            time.sleep(0.05)
            data3 = client_socket.recv(BUFSIZ).decode()
            #third.config(text=data3)
            time.sleep(0.05)
            data4 = client_socket.recv(BUFSIZ).decode()
            #fourth.config(text=data4)
            time.sleep(0.05)
            an = client_socket.recv(BUFSIZ).decode()
            time.sleep(0.05)
            window.plainTextEdit.appendPlainText(msg)

            #window.textBrowser.insertPlainText(msg)

            window.pushButton_5.setText(data1)

            window.pushButton_4.setText(data2)

            window.pushButton_3.setText(data3)

            window.pushButton_2.setText(data4)

            #msg_list.insert(tkinter.END, msg)

        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = window.label_2.text()
    number = int(msg) + 99
    #window.label_2.setText("")  # Clears input field.
    client_socket.send(bytes(str(number), "utf8"))




#----Now comes the sockets part----
HOST = 'localhost'
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

an = " "
res = 0

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = ExampleApp()  # Создаём объект класса ExampleApp
window.show()  # Показываем окно
send()
app.exec_()  # и запускаем приложение
