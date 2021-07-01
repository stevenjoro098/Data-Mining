__author__ = 'Steve'

import matplotlib.pyplot as plt
#from histogram import Hist_Distr
import sys
#from import_file import *
#from dtc_details import *
#from prediction_window import *
#from pie_chart import *
#from import_file import *
#from time_series_plot import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from decision_tree_classifier import *
#from kmeans import *
from pandas.plotting import table
#from Qtabling import *
from matplotlib.backends.backend_qt4agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg \
    import NavigationToolbar2QT as NavigationToolbar

class PrettyWidget(QWidget):

    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 1300, 600)
        self.setFixedSize(1300, 600)
        self.center()
        self.setWindowTitle('Health Statistics & Analysis')
        #self.setWindowIcon(QIcon('hospital-2.png'))
        grid = QGridLayout()
        self.setLayout(grid)

        bar = QMenuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        save = QAction('Save', self)
        file.addAction(save)
        edit = bar.addMenu('Edit')
        edit.addAction('Copy')
        edit.addAction('paste')
        quit = bar.addMenu('Quit')
        exit = QAction('Exit', self)
        quit.addAction(exit)
        grid.addWidget(bar, 0,0,1,2)

        pic = QLabel()
        #pic.setPixmap(QPixmap('electrocardiogram.png'))
        pic.resize(pic.sizeHint())
        label1 = QLabel('Data Manipulation')
        #label1.setFont(QFont('Calibri', 11, QFont.Bold))
        file_import = QPushButton('Import File')
        file_import.resize(file_import.sizeHint())
        #self.connect(file_import, SIGNAL('clicked()'), self.file_dialog)
        #self.connect(self, SIGNAL('main2closed()'), self.file_clear)
        button2 = QPushButton('Display DataFrame')
        button2.resize(button2.sizeHint())
        #self.connect(button2, SIGNAL('clicked()'), self.disp_df)
        #self.connect(self, SIGNAL('main2closed()'), self.df_clear)

        describ = QPushButton('Description')
        describ.clicked.connect(self.description)


        sublayout1 = QGridLayout()
        sublayout1.addWidget(pic, 0,0)
        sublayout1.addWidget(label1, 1,0)
        sublayout1.addWidget(file_import,2,0)
        sublayout1.addWidget(button2,2,1)

        sublayout1.addWidget(describ,3 ,0)
        grid.addLayout(sublayout1,1 ,0)

        label2 = QLabel('Statistical Visualization')
        #label2.setFont(QFont('Calibri', 11,QFont.Bold))
        button4 = QPushButton('Distribution(Histogram)')
        button4.resize(button4.sizeHint())
        #self.connect(button4, SIGNAL('clicked()'), self.Hist)
        #self.connect(self, SIGNAL('main2closed()'), self.hist_clear)
        button5 = QPushButton('Time Chart Series')
        button5.resize(button5.sizeHint())
        button5.clicked.connect(self.plot_series)
        button6 = QPushButton('Pie Chart')
        button6.clicked.connect(self.Pie)
        button7 = QPushButton('Clear Canvas')
        button7.clicked.connect(self.clear_canvas)
        sublayout2 = QGridLayout()
        sublayout2.addWidget(label2,0,0)
        sublayout2.addWidget(button4,1,0)
        sublayout2.addWidget(button5,1,1)
        sublayout2.addWidget(button6,2,0)
        sublayout2.addWidget(button7,2,1)
        grid.addLayout(sublayout2,2 ,0 ,1 ,1)

        label3 = QLabel('Supervised / UnSupervised Learning')
        #label3.setFont(QFont('Calibri', 11, QFont.Bold))
        button7 = QPushButton('Decision Tree Classifier')
        button7.resize(button7.sizeHint())
        button7.clicked.connect(self.classifier)
        #self.connect(button7, SIGNAL('clicked()'), self.dc_tree_info)
        #self.connect(self, SIGNAL('main2closed()'), self.clearDecision)
        self.button8= QPushButton('Clustering(KMean)')
        #self.connect(self.button8, SIGNAL('clicked()'), self.clustering)
        #self.connect(self, SIGNAL('main2closed()'), self.clearCluster)
        button9 = QPushButton('Predictive Learning')
        #self.connect(button9, SIGNAL('clicked()'), self.prediction)
        #self.connect(self, SIGNAL('main2closed()'), self.pred_close)
        sublayout3 = QVBoxLayout()
        sublayout3.addWidget(label3)
        sublayout3.addWidget(button7)
        sublayout3.addWidget(self.button8)
        sublayout3.addWidget(button9)
        grid.addLayout(sublayout3,3 , 0 , 1, 1)

        verticalLine = QFrame()
        verticalLine.setFrameStyle(QFrame.VLine)
        verticalLine.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        grid.addWidget(verticalLine,1 ,1, 6, 1)
        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1, 2, 1, 2)
        grid.addWidget(self.toolbar, 0, 2, 1, 2)

        self.show()
    def disp_df(self):
        self.display_df = Table_Widget()
        #self.connect(self.display_df, SIGNAL('closed()'), self.df_clear)
        self.display_df.show()
    def df_clear(self):
        #self.emit(SIGNAL('main2closed()'))
        pass
    def file_dialog(self):
        self.file_diag = file_dialog()
        #self.connect(self.file_diag, SIGNAL('closed()'), self.hist_close)
        self.file_diag.show()
    def file_clear(self):
        self.emit(SIGNAL('main2closed()'))
    def file_import(self):
        print('file_import')
        deef = file_dialog
        deef.get_csv_filename(self)
        return deef

        #data description mean, std, count, min, max, quartile, median.
    def description(self):
        df = pd.read_csv('2015 data.csv')
        fig , ax= plt.subplots(figsize=(13, 3)) # set size frame
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis
        ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
        #tabla = table(ax, df.describe(), loc='center')  # where df is your data frame
        #tabla.auto_set_font_size(False) # Activate set fontsize manually
        #tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
        #tabla.scale(1.2, 1.2) # change size table
        plt.show()


        #plot time curve series for the trend of Malaria
    def plot_series(self):
        time_plot()

        #plot pie chart to represent the fraction of Gender and Malaria cases from a Whole.
    def Pie(self):
        self.pie_window = Pie_Distr()
        self.connect(self.hist_window, SIGNAL('closed()'), self.pie_close)
        self.pie_window.show()
    def pie_close(self):
        self.emit(SIGNAL('main2closed()'))
    def pie_clear(self):
        del self.pie_window
        self.pie_window = None

    def clear_canvas(self):
        self.canvas.clear()


    def plot1(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**2 for i in x]
        ax.plot(x, y, 'b.-')
        ax.set_title('Quadratic Plot')
        self.canvas.draw()

    def plot2(self):
        self.canvas.clearFocus()
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**0.5 for i in x]
        ax.plot(x, y, 'r.-')
        ax.set_title('Square Root Plot')
        self.canvas.draw()
    def plot3(self):
        return 0

        '''To plot the distribution of health from data gathered;
        Histogram will determine Age, Height & Weight Distribution'''
    def Hist(self):
        self.hist_window = Hist_Distr()
        self.connect(self.hist_window, SIGNAL('closed()'), self.hist_close)
        self.hist_window.show()
    def hist_close(self):
        self.emit(SIGNAL('main2closed()'))
    def hist_clear(self):
        del self.hist_window
        self.hist_window = None
    def classifier(self):

        print("\n-- get data:")
        df = get_iris_data()

        print("\n-- df.head():")
        #print(df.head(), end="\n\n")

        features = ["Age","Height","Weight","BMI"]
        df, targets = encode_target(df, "Malaria")
        #Learning of the algorithm

        y = df["Target"]
        X = df[features]

        #dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
        #dt.fit(X, y)

        print("\n-- get_code:")
        get_code(dt, features, targets)

        print("\n-- Target Class")
        #print(df[df['Weight'] <= 50]['Malaria'].unique(), end="\n\n")

        #visualize_tree(dt, features)
    def dc_tree_info(self):
        self.decision_details = d_tree_info()
        self.connect(self.decision_details, SIGNAL('closed()'), self.decision_close)
        self.decision_details.show()
    def decision_close(self):
        self.emit(SIGNAL('main2closed()'))
    def clearDecision(self):
        del self.decision_details
        self.decision_details = None
        #Unspervised learning where the algorithm trys to group the data from the dataset, based on the
    def clustering(self):
        self.other_window = clustered_layout()
        self.connect(self.other_window, SIGNAL('closed()'), self.clustering_close)
        self.other_window.show()
    def clustering_close(self):
        self.emit(SIGNAL('main2closed()'))
    def clearCluster(self):
        del self.other_window
        self.other_window = None

        #To carry out the prediction of target class representing Malaria and its Types based on
        # the characteristics they potray from the data collected.
    def prediction(self):
        self.pred_window = prediction()
        self.connect(self.pred_window, SIGNAL('closed()'), self.pred_close)
        self.pred_window.show()
    def pred_close(self):
        self.emit(SIGNAL('main2closed'))
    def clearPred(self):
        del self.pred_window
        self.pred_window = None

        #position the main window in the center position of the screen layout.
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()

if __name__=="__main__":
    main()

