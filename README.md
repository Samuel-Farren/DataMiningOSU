# DataMiningOSU
This is a list Repo of various projects done at Ohio State for a Data Mining Class

# DataMiningOSU
This is a list Repo of various projects done at Ohio State for a Data Mining Class.

There are a total of 6 projects. All code was writte without the aid of any pre-existing libraries. Descriptions of each can be seen below:

==============================================================================================
==============================================================================================

## Lab1: 
    My program is written in Python. It uses two external libraries: numpy and matplotlib so make sure these are installed if it is ran
    on a local machine and not on the CSE Environment. I ran mine on a Mac and tested on the CSE environmen
    and both worked fine.

There are two separate python files in the folder. One is iris.py and the other is IncomeDataset.py. both are run by just typing in the terminal:

python iris.py
python IncomeDataset.py

Make sure both datasets are in the directory when you run the programs as I couldn't find a way in python
to load the data from a url and thought it would run faster anyways if it was already on the local machine.
With both files in the directory, you can run the above comamands depending on which dataset you want to see first.
MAKE SURE THE FILES ARE NAMED HOW THEY ARE LISTED ON CARMEN.(Iris.csv and income_tr.csv)
When iris.py is ran, you will be prompted to enter how many closest objects you want to be displayed.
So if you want 5 just type in the number five and hit enter, then
All of the proximity data will be displayed in the terminal. The first list of data that is displayed is based off
a Minkowski difference solution for proximity. The second set of data used a cosine similarity calculation to compute the
proximity similarities.

IncomeDataset.py is similar in that it will prompt you to enter how many closest objects you want to see. All of the proximities
are output at the end of the terminal. What comes before will be a bunch of statistics that were used in the report. The first similarity
process will run and rapidly write the top k similarities to each id in the terminal. The second one will run which is a cosine similarity,
however it runs very slowly and doesn't work all the way. I couldn't figure out how to make it run faster since the load of computation
for the cosine was much much greater.

==============================================================================================
==============================================================================================

## Lab2: 

KNN classifier on income and iris data sets: Sam Farren

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

==============================================================================================
==============================================================================================

## Lab3: Textbook Homework


==============================================================================================
==============================================================================================

## Lab4: Textbook Homework

==============================================================================================
==============================================================================================

## Lab5: K-Nearest_Neighbors Analysis Lab Writeup and R Script

==============================================================================================
==============================================================================================

## Lab6: An Analysis of the billboard top 100 songs and their lyrics from 1964-2015. Did analysis of explicit words by year as well which can be seen in Figures folder.

This lab just consisted of one file called lab6.py and a couple other files for the dataset and the
stop-word-list and explicit terms file. The dataset used is called billboard_lyrics_1964-2015.csv. It
is rather large so I don't recommend opening it since it caused atom to crash a couple times when i did. The
stop-word-list.txt is a file of the meaningless words I filtered out of the Term frequency calculations.
Terms-to-Block.csv is the list of explicit words I used for explicit lyric analysis over time for the
songs in the dataset.

All of the code I used for graphs and visualization purposes
is commented out to allow the program to run completely through. All of the output is
in the command line and meaningful graphs and text analysis are described in the report.

The packages used in the program were:
import numpy as np
import csv
from collections import Counter
import operator
import matplotlib.pyplot as plt
import math as math

I didn't end up using nltk so I just commented it out.

You can simply run the file after making sure the dataset, stop-word-list, and Terms-to-Block
are in the same directory as lab6.py. just do:

python lab6.py and the file will run all the way through and output into the terminal.


==============================================================================================
==============================================================================================

