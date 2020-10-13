#found from https://github.com/tflearn/tflearn/issues/121

#loss: 739 at epoch 100
#source ~/tensorflow/bin/activate
from __future__ import division, print_function, absolute_import

import tflearn
import numpy as np
import math
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf
import getSamples as gs
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

#subtract by mean and divide by std (mean and std of all response times)
def normalize(response_times, data):
    std = np.std(response_times)
    mean = np.mean(response_times)
    for i in range(0,data.shape[0]):
        for j in range(0,data.shape[1]):
            data[i,j] = (data[i,j]-mean)/std
    return data

#multiply by std and add the mean (mean and std of all response times)
def denormalize(response_times, data):
    std = np.std(response_times)
    mean = np.mean(response_times)
    for i in range(0,data.shape[0]):
            for j in range(0,data.shape[1]):
                data[i,j] = ((std*data[i,j])+mean)
    return data

#step_radians = 0.001
x_length = 50
y_length = 7
iterations = 10
learning_rate = 0.01

def myRNN(activator, optimizer, X_train, Y_train, X_test, Y_test, response_times):
    tf.reset_default_graph()
    # Network building
    net = tflearn.input_data(shape=[None, x_length, 1])
    net = tflearn.lstm(net, 32, dropout=0.8,bias=True)
    net = tflearn.fully_connected(net, y_length, activation=activator)
    net = tflearn.regression(net, optimizer=optimizer, loss='mean_square', learning_rate=learning_rate)

    last_sample_x_test = X_test[-1,:]
    last_sample_truth = np.concatenate((X_test[-1,:],Y_test[-1,:]))

    X_train = X_train.reshape([X_train.shape[0],X_train.shape[1],1])
    X_test = X_test.reshape([X_test.shape[0],X_test.shape[1],1])


    # Training
    model = tflearn.DNN(net, tensorboard_verbose=0)
    model.fit(X_train, Y_train, n_epoch=25, validation_set=0.1, batch_size=32)

    # Predict the future values
    predict = model.predict(X_test)

    last_sample_prediction = predict[-1,:]

    expected = np.array(Y_test).flatten()
    predicted = np.array(predict).flatten()

    #plot the last sample
    """forecast = np.concatenate((last_sample_x_test,last_sample_prediction))
    days = [x for x in range(0,last_sample_truth.size)]
    plt.plot(days, last_sample_truth)
    plt.plot(days, forecast)
    plt.xlabel('Day')
    plt.ylabel('Response Times (in hours)')
    plt.title('Median Response Time per Day for DOT')
    plt.show()"""

    # predicted = denormalize(response_times, predicted)
    mae = mean_absolute_error(predicted, expected)
    mse = mean_squared_error(predicted, expected)
    return mse, mae
    
def main():

    activator = 'relu'
    optimizer = 'adam'
    agencies = ['DEP','DOB','DOHMH','DOT','DPR','DSNY','HPD','NYPD']
    #agencies = ['DOT']

    fh = open("rnn_results.txt","w")

    for chosen_agency in agencies:
        fh.write("\n"+chosen_agency)
        mses = []
        maes = []
        response_times, X_train, Y_train, X_test, Y_test = gs.getSamples(chosen_agency, x_length, y_length)

        #X_train = normalize(response_times, X_train)
        #Y_train = normalize(response_times, Y_train)
        #X_test = normalize(response_times, X_test)

        for i in range(0,iterations):
            mse, mae = myRNN(activator, optimizer, X_train, Y_train, X_test, Y_test, response_times)
            mses.append(mse)
            maes.append(mae)

        avg_mse = sum(mses)/len(mses)
        avg_mae = sum(maes)/len(maes)
        
        fh.write("\nMSE: "+str(avg_mse))
        fh.write("\nMAE: "+str(avg_mae))

    fh.close()

main()