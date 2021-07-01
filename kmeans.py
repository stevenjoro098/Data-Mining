import pandas as pd
import sys
from sklearn.cluster import  KMeans
from sklearn.decomposition import  PCA
from PyQt4 import  QtGui
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
class clustered_layout(QtGui.QWidget):
    def __init__(self, parent = globals):
        super(clustered_layout,self).__init__()
        self.center()
        self.UI()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UI(self):
        self.setGeometry(300, 300, 300, 150)
        self.setFixedSize(300, 150)
        self.setWindowTitle('KMeans Clustering Param')
        self.setWindowIcon(QtGui.QIcon('cluster.png'))
        grid = QtGui.QGridLayout(self)
        label1 = QtGui.QLabel('Cluster No.')
        grid.addWidget(label1, 0, 0, 1, 1)
        self.edit1 = QtGui.QLineEdit()
        grid.addWidget(self.edit1,0 ,1 ,1 ,1)

        label2 = QtGui.QLabel('Random State')
        grid.addWidget(label2,1 , 0, 1, 1)
        self.edit2 = QtGui.QLineEdit(self)
        grid.addWidget(self.edit2, 1,1, 1, 1)

        label3 = QtGui.QLabel('PCA')
        grid.addWidget(label3, 2, 0, 1, 1)
        self.edit3 = QtGui.QLineEdit()
        grid.addWidget(self.edit3, 2, 1, 1, 1)

        cluster = QtGui.QPushButton('Cluster')
        cluster.clicked.connect(self.kmean)
        cluster.resize(cluster.sizeHint())
        grid.addWidget(cluster, 3, 0)

        cancel = QtGui.QPushButton('Cancel')
        cancel.clicked.connect(self.close)
        grid.addWidget(cancel,3, 1)
        self.setLayout(grid)
        self.show()

    def kmean(self):
        clst = self.edit1.text()
        rs = self.edit2.text()
        pc = self.edit3.text()
        if clst == '' or rs == '' or pc == '':
            self.info7 = QtGui.QMessageBox()
            self.info7.setIcon(QtGui.QMessageBox.Warning)
            self.info7.setText('Please Check on Your Entries!! \n\n Then Try Again')
            ret = self.info7.exec_()
        if pc > '4' or pc == '1':
            self.info6 = QtGui.QMessageBox()
            self.info6.setIcon(QtGui.QMessageBox.Warning)
            self.info6.setText('Principal Component Analysis cannot exceed 4!! \n Can only work where (1 < n_samples <= 4) for this case')
            ret = self.info6.exec_()
        else:

            dataframe = pd.read_csv('2015 data.csv')
            df = dataframe.head(200)
            #n_clusters = no. of clusters we want
            #Initiliaze the model with 2 parametres -- number of clusters and  random state

            kmeans_model = KMeans(n_clusters=int(clst), random_state=int(rs))
            #Get only the numeric columns from the dataframe
            g_columns = df._get_numeric_data()
            #fit the model using the good columns
            kmeans_model.fit(g_columns)
                         #Get the cluster assignments
            labels = kmeans_model.labels_
            #principal analysis component(PCA)
            #creating a PCA model to compress the columns with
            #similarities into a single column with new figures
            #trying to maintain the info.

            pca_2 = PCA(int(pc))
            #Fit the PCA model on the numeric columns from earlier
            plot_columns = pca_2.fit_transform(g_columns)
            #Make a scatter plot of each game, shaded according to cluster assignment
            plt.scatter(x=plot_columns[:, 0], y = plot_columns[:, 1], c=labels)
            #Show the plot
            plt.show()



def main1():
    app = QtGui.QApplication(sys.argv)
    ex = clustered_layout()
    app.exec_()
if __name__=="__main__":
    main1()
