__author__ = 'Steve'
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
from PyQt4 import  QtGui
class Hist_Distr(QtGui.QWidget):
    def __init__(self):
        super(Hist_Distr, self).__init__()
        self.center()
        self.UI()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setFixedSize(250, 100)
        self.setWindowTitle('Histogram Distribution')
        self.setWindowIcon(QtGui.QIcon('Normal Distribution Histogram-48.png'))
        grid = QtGui.QGridLayout()
        self.label = QtGui.QLabel('Choose Attribute')
        self.label.setFont(QtGui.QFont('Calibri',11))
        grid.addWidget(self.label, 0 ,0 ,1, 1)
        self.combo = QtGui.QComboBox()
        self.combo.addItems(['Age', 'Height', 'Weight'])
        grid.addWidget(self.combo, 1 ,0 ,1, 1)
        self.plot = QtGui.QPushButton('Plot Histogram')
        self.plot.resize(self.plot.sizeHint())
        self.plot.clicked.connect(self.histogram)
        grid.addWidget(self.plot, 2, 0, 1, 1)

        self.setLayout(grid)
        self.show()
    def histogram(self):
        try:
            item = self.combo.currentText()
            print(item)
            df = pd.read_csv('2015 data.csv')
            print(df.head(5))
            print(df[item].head(5))
            df[item].hist(bins=30)
            plt.xlabel(item)
            plt.ylabel(' Frequency Distribution ')
            plt.title('--- Distribution ---')
            plt.show()
        except:
            self.warn = QtGui.QMessageBox()
            self.warn.setIcon(QtGui.QMessageBox.Warning)
            self.warn.setText('Check Error on Histogram Function!! ')
            self.warn.exec_()
def main2():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = Hist_Distr()
    app.exec_()
if __name__=='__main__':
    main2()












