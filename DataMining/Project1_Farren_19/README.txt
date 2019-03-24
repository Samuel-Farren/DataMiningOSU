README:

Name: Sam Farren
Class: Data Mining
Instructor: Jason Van Hulse

My program is written in Python. It uses two external libraries: numpy and matplotlib so make sure these are installed if it is ran
on a local machine and not on the CSE Environment. I ran mine on a Mac and tested on the CSE environment and both worked fine.

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
