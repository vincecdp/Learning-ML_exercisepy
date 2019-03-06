# Predicting Prices
"""
Created on Tue Dec 25 17:41:41 2018

@author: WraithDelta
"""
import csv
import numpy as np 
from sklearn.svm import SVR
import matplotlib.pyplot as plt

plt.get_backend()

dates = []
prices = []
#gets data from csv file and parses it
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
            
        #print (dates, prices)
            
    return

#def moving_average(a, n=5):
  #  ret = np.cumsum(a, dtype=float)
  #  ret[n:]=ret[n] - ret[:-n]  
  #  return ret[n-1:] / n  

def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1))
    
    #print (dates, prices)
    
    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    
    svr_rbf.fit(dates, prices) # fitting the data points in the models
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(svr_poly.predict(dates), color='blue', label='Polynomial model')
   
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    
    plt.legend()
    plt.show()
    
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('AAPL.csv')
predicted_price = predict_prices(dates, prices, [[29]])
print (predicted_price)
