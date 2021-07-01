import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

def time_plot():
    try:
        df = pd.read_csv('2015 data.csv')
        ps = DataFrame(df.groupby(pd.Grouper(key='Date_Time'))['Malaria'].value_counts().unstack())
        #drop the NaN values in the columns
        ps1 = ps.dropna()
        print(ps.head())
        #split the window based on the Malaria.unique values
        ps1.plot(subplots = True)
        #define x label
        plt.xlabel('Date')
        #define ylabel
        plt.ylabel('No. of Patients')
        #ensure the window displays
        plt.show()
    except:
        print('Error')
if __name__=="__main__":
    time_plot()