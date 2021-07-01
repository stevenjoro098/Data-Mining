__author__ = 'Steve'

import pandas as pd
import numpy as np
from matplotlib.pyplot import pie, axis, show
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Pie_Distr(QtWidgets.QWidget):
    def __init__(self):
        super(Pie_Distr, self).__init__()
        self.UI()

    def UI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Pie Chart')
        #self.setWindowIcon(QtWidgets.QIcon('Normal Distribution Histogram-48.png'))
        grid = QtWidgets.QGridLayout()
        self.label = QtWidgets.QLabel('Choose Attribute')
        grid.addWidget(self.label, 0, 0, 1, 1)
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(['Gender', 'Malaria'])
        grid.addWidget(self.combo, 1, 0, 1, 1)
        self.plot = QtWidgets.QPushButton('Pie Chart')
        self.plot.resize(self.plot.sizeHint())
        self.plot.clicked.connect(self.Pie_Chart)
        grid.addWidget(self.plot, 2, 0, 1, 1)

        self.setLayout(grid)
        self.show()

    def Pie_Chart(self):
        try:
            df = pd.read_csv('data/2015 data.csv')
            item = self.combo.currentText()
            sum = pd.DataFrame(df.groupby(pd.Grouper(key='Malaria'))[item].value_counts().unstack())
            print(sum)
            label = df['Malaria'].unique()
            plt.pie(sum)
            plt.axis('equal')
            plt.title('Cases of Malaria in Dataset')
            plt.axis('equal')
            plt.legend()

            plt.show()
        except:
            print('Error')


def main3():
    import sys
    app = QApplication(sys.argv)
    ex = Pie_Distr()
    app.exec_()


if __name__ == '__main__':
    main3()
