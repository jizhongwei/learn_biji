from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt

import sys
import zhconv
import random

def jian2fan():
    fd = open('all2.txt','r', encoding= 'utf-8')
    content = fd.read()
    con_list = content.split("\t")[:-1]
    jian = random.sample(con_list, 1)[0]
    fan = zhconv.convert(jian, 'zh-tw')
    return jian, fan

def main():
    app = QApplication(sys.argv)
    w = QWidget()

    jian,fan = jian2fan()

    label_jian = QLabel(w)
    label_jian.setText(jian)

    label_jian.setStyleSheet("QLabel{background-color:rgb(225,22,173,255);font-size:50px;font-weight:normal;font-family:Arial;text-align:center;}")
    label_jian.setAlignment(Qt.AlignCenter)
    label_jian.resize(80,80)
    label_jian.move(30,40)

    label_fan = QLabel(w)
    label_fan.setText(fan)

    label_fan.setStyleSheet("QLabel{background-color:rgb(225,22,173,255);font-size:50px;font-weight:normal;font-family:Arial;text-align:center;}")
    label_fan.setAlignment(Qt.AlignCenter)
    label_fan.resize(80,80)
    label_fan.move(190,40)

    def change():
        jian,fan = jian2fan()
        label_jian.setText(jian)
        label_fan.setText(fan)

    btn = QPushButton("下一个", w)
    btn.resize(80,50)
    btn.move(110,140)

    btn.clicked.connect(change)

    w.resize(300,200)
    w.move(300,300)
    w.setWindowTitle("繁体&简体")
    w.setFixedSize(w.width(),w.height())
    w.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    # jian2fan()