# Predicting the data using the Bayesian curve fitting method

import numpy as np
import csv
import pandas as pd


def read_data(fname):

    data = pd.read_csv('Stock Data/' + fname + '.csv')
    x = list(data.iloc[1:, :]['x'])
    t = list(data.iloc[1:, :]['Close'])

    return x, t


def predict_data(x, t):
    # Initialize the parameters
    size = 10
    M = 4
    beta = 12
    alpha = 0.2

    a = np.zeros(shape=(M+1, 1))
    b = np.zeros(shape=(1, M+1))
    lt = np.zeros(shape=(M+1, 1))

    for i in range(0, size):
        for j in range(0, M + 1):
            a[j][0] += [x[i]**j]

    A = a

    for i in range(0, M+1):
        b[0][i] = x[size]**i

    B = b

    s = np.matmul(A, B) * beta

    for i in range(0, M+1):
        for j in range(0, M+1):
            if i == j:
                s[i][j] += alpha

    # Calculate inverse of s
    s = np.linalg.inv(s)

    for i in range(0, size):
        for j in range(0, M+1):
            lt[j][0] += x[i]**j * t[i]

    FT = np.matmul(B, s)

    predicted_price = np.matmul(FT, lt) * beta

    est = predicted_price[0][0]
    mean_error = abs(t[size] - est)
    rel_error = mean_error / t[size]
    result = [est, mean_error, rel_error]

    print("The actual value of the stock is: {:.2f}".format(t[size]))
    return result


def main():
    fname = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'NFLX', 'TRIP', 'TSLA', 'TWTR', 'VAC', 'YELP']
    f = []

    for i in fname:
        x, t = read_data(i)
        print("Predicting the price of stock {}....\n".format(i))

        estimation, mean_error, relative_error = predict_data(x, t)

        print("Estimated value = {:.2f}".format(estimation))
        print("Mean error = {:.2f}".format(mean_error))
        print("Relative error is = {:.2f}\n".format(relative_error))


if __name__ == '__main__':
    main()
