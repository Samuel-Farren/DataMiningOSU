README

Project 2: KNN classifier on income and iris data sets: Sam Farren

These python scripts utilize :csv, numpy, scipy, matplotlib, operator, and sklearn. All command line output can be ignored as most of it was used for debugging purposes.

            import csv
            import numpy as np
            #import scipy as sci
            import matplotlib as plot
            from math import exp,sqrt,log10,log1p
            #from matplotlib.mlab import PCA
            import matplotlib.pyplot as plt
            from numpy import recfromcsv
            import operator
            from sklearn.metrics import confusion_matrix
            from sklearn.metrics import roc_curve, auc

There are two scripts in this folder for project 2. The first one is iris.py.This uses the file from lab 1 called Iris.csv and the one from lab 2 called Iris_Test.csv so make sure
these are in the same directory as the script. When you run it with the command input stated below, it will prompt you for how many neighbors you want the algorithm to run against. Input any number less than
the input size, I recommend between 4 and 8 for the iris dataset. The output for iris.py is written to a file called KNNIrisOutput.txt where the actual, predicted, and posterior probabilities
are stored.
        How to run:
            _> python iris.py

For the income dataset, it is almost the same. This is the file called IncomeDataset.py. The two files required for this are income_te.csv and income_tr.csv so make sure
these are in the directory when you run the python script. It will also prompt you for the number of neighbors for the algorithm to run against.
I recommend a higher number for this dataset around 20 or 30 for better success rate in predicting classes. The output will be written to a file called KNNIncomeOutput.txt
        How to run:
            _> python IncomeDataset.py


In Summary:
    Iris Dataset:
        _> python iris.py
        Output File: KNNIrisOutput.txt

    Income Dataset:
        _> python IncomeDataset.py
        OutputFile: KNNIncomeOutput.txt
