import csv
import numpy as np
#import scipy as sci
import matplotlib as plot
from math import exp
import operator
#from matplotlib.mlab import PCA

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


list_data = []
#iris = "Iris.csv"
iris="Iris_Test.csv"
income = "income_tr.csv"
matrix = np.empty((0,5), float)

#fileChoice = input('Enter 1 for iris data or 2 for income data: ')

# matrix = np.loadtxt(iris, delimiter=",")
# print np.matrix(matrix)

with open(iris, 'rb') as f:
    reader = csv.DictReader(f)
    data = next(reader)
    # print data
    for row in reader:

        a = np.array([float(row["sepal_width"]),float(row["sepal_length"]),float(row[" petal_length"]),float(row[" petal_width"])])
        list_data.append(a)
iris_classes = np.genfromtxt(iris, dtype=None, delimiter=',', names=True, usecols=(4)) #Prints ID-> print list_data[0][0]
print iris_classes

arr = np.vstack(list_data)
print arr
#print arr
k=5
k=input('Enter how many closest objects you want to display: ')
user_choice = 1
# user_choice = input('What id do you want to compare against? ')
# k = input('How many closest objects do you want displayed? ')

#firstRow = arr[user_choice]
tuple_array = []
count = 0
print "MINKOWSKI PROXIMITY MEASURES ARE BELOW"
print "#######################################"
class_votes = {}
correctCount = 0

for i in range(0, len(arr)):
    firstRow = arr[i]
    for row in arr:
        minkowski = pow(pow((firstRow[0]-row[0]),4) + pow((firstRow[1]-row[1]),4) + pow((firstRow[2]-row[2]),4) + pow((firstRow[3]-row[3]),4),.25)
        tup = count,minkowski
        tuple_array.append(tup)
        count = count+1
    tuple_array.sort(key=lambda tup: tup[1])
    print "Compared ID: " + str(i) + "  "
    for j in range(1,k+1):
        print "id:" + str(tuple_array[j][0]) + "  " + str(j) + "-prox: " + str(tuple_array[j][1])

        if iris_classes[tuple_array[j][0]][0] in class_votes:
            class_votes[iris_classes[tuple_array[j][0]][0]] +=1
        else:
            class_votes[iris_classes[tuple_array[j][0]][0]]=1
    guess = max(class_votes.iteritems(), key=operator.itemgetter(1))[0]
    if guess == iris_classes[i][0]:
        correctCount+=1
    class_votes.clear()
    print "\n"
    del tuple_array[:]
    count = 0
percentage = float(correctCount)/float(len(arr))
print "The accuracy obtained from a minkowski classifier is: " + str(percentage *100) +  "%"
print "END OF MINKOWSKI MEASURES"
print '\n\n\n\n\n'


#Cosine Similarity Proximity Measure
    ###  (d1 . d2 /||d1||*||d2|||)
    ##############################################################################
cosine_array = []
counter = 0
print "COSINE SIMILARITY PROXIMITY MEASURES ARE BELOW"
print "#######################################"
# for i in range(1, len(arr)):
#     firstRow = arr[i]
#     for row in arr:
#         dot = firstRow[0]*row[0] + firstRow[1]*row[1] + firstRow[2]*row[2] + firstRow[3] * row[3]
#         lens1 = pow(pow(firstRow[0],2) + pow(firstRow[1],2) + pow(firstRow[2],2) + pow(firstRow[3],2),.5)
#         lens2 = pow(pow(row[0],2) + pow(row[1],2) + pow(row[2],2) + pow(row[3],2),.5)
#         cosine = dot/(lens1 * lens2)
#         cosine_tup = counter,cosine
#         cosine_array.append(cosine_tup)
#         #print "number: " + str(counter) + "dot: " + str(dot) + "lens1: " + str(lens1) + "lens2: " + str(lens2) + "cosine: " + str(cosine)
#         counter = counter+1
#     cosine_array.sort(key=lambda tup: tup[1],reverse=True)
#     print "Compared ID: " + str(i) + "  "
#     for j in range(1,k+1):
#         print "id:" + str(cosine_array[j][0]) + "  " + str(j) + "-prox: " + str(cosine_array[j][1])
#     print "\n"
#     del cosine_array[:]
#     counter = 0
print "END OF COSINE MEASURES"

#print cosine_array


# results = PCA(arr)
# print results.fracs
# print arr

#############################################################################
#Income Data Set
#
# with open('income_tr.csv', 'rb') as f:
#     reader = csv.DictReader(f)
#     data = next(reader)
#     print data
#     for row in reader:
#         list_data.append(row)
#
#
# for r in list_data:
#     print r
#############################################################################
