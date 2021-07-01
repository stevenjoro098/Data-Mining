__author__ = 'Steve'

from PyQt5 import QtWidgets


class d_tree_info(QtWidgets.QWidget):
    def __init__(self):
        super(d_tree_info, self).__init__()
        self.UI()

    def UI(self):
        self.setGeometry(100, 100, 150, 150)
        self.setWindowTitle('Decision Tree Navigation Information')
        grid = QtWidgets.QGridLayout()
        #self.setWindowIcon(QIcon('flag.png'))
        self.label0 = QtWidgets.QLabel('DECISION TREE CLASSIFIER')
        #self.label0.setFont(QtGui.QFont('Calibri', 12, QtGui.QFont.Bold))
        self.label = QtWidgets.QLabel('1) (MIN_SAMPLES_SPLIT = 20)- requires 20 SAMPLES in a node \n for it to be split\n')
        #self.label.setFont(QtGui.QFont('Calibri', 10))
        self.label1 = QtWidgets.QLabel('2) (RANDOM_STATE = 99) - is to SEED the random NUMBER generator\n')
        #self.label.setFont(QtGui.QFont('Calibri', 10))
        self.label2 = QtWidgets.QLabel(
            '3) VALUE = [50.0. 0.] - if a cond is TRUE, take the left/right branch to get to the 50 SAMPLES. \n\n'
            'This means there are 50 EXAMPLES of TARGET 0 in this case P.FALCIPARUM etc \n\n'
            'The splitting continues till it creates a bin with only one class which cannot be split again \n\n'
            'If the resulting bin has less than 20 SAMPLES - this is as a result of MIN_SAMPLE_SPLIT being 20 \n\n')
        #self.label2.setFont(QtGui.QFont('Calibri', 10))
        self.label3 = QtWidgets.QLabel('INDICES:\n\t'
                                   '        P.FALCIPARUM -> [0]\n\t'
                                   '        P. VIVAX -> [1]\n\t'
                                   '        P.MALARAE -> [2]\n\t'
                                   '        P.OVALE -> [3]\n\t')
        #self.label3.setFont(QtWidgets.QFont('Calibri', 10))
        grid.addWidget(self.label0, 0, 0, 1, 1)
        grid.addWidget(self.label, 1, 0, 1, 1)
        grid.addWidget(self.label1, 2, 0, 1, 1)
        grid.addWidget(self.label2, 3, 0, 1, 1)
        grid.addWidget(self.label3, 4, 0, 1, 1)

        self.setLayout(grid)
        self.show()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = d_tree_info()
    app.exec_()


if __name__ == '__main__':
    main()
