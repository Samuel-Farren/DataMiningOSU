import csv
import numpy as np
import scipy as sci
import matplotlib as plot
from math import exp
import operator
from matplotlib.mlab import PCA
from sklearn.metrics import confusion_matrix
#from __future__ import print_function

# def getResponse(neighbors):
#     classVotes = {}
#     for x in range(len(neighbors)):
#         response = neighbors[x][-1]
#         if response in classVotes:
#             classVotes[response] += 1
#         else :
#             classVotes[response] = 1
#     sortedVotes = sorted(classVotes.iteritems(), key = operator.itemgetter(1), reverse = True)
# 	return sortedVotes[0][0]


list_data = []# iris = "Iris.csv"
training = "Iris_Test.csv"
income = "income_tr.csv"
matrix = np.empty((0, 5), float)

# fileChoice = input('Enter 1 for iris data or 2 for income data: ')

# matrix = np.loadtxt(iris, delimiter = ",")# print np.matrix(matrix)

with open(training, 'rb') as f:
    reader = csv.DictReader(f)
    data = next(reader)# print data
    for row in reader:
        a = np.array([float(row["sepal_width"]), float(row["sepal_length"]), float(row["petal_length"]), float(row["petal_width"])])
        list_data.append(a)
test_data = np.genfromtxt("Iris.csv", dtype = None, delimiter = ',', names = True, usecols = (0,1,2,3))
iris_classes = np.genfromtxt("Iris_Test.csv", dtype = None, delimiter = ',', names = True, usecols = (4))# Prints ID - > print list_data[0][0]
test_data_classes = np.genfromtxt("Iris.csv", dtype = None, delimiter = ',', names = True, usecols = (4))# Prints ID - > print list_data[0][0]

print iris_classes

training_data = np.vstack(list_data)
print training_data# print arr
k = 5
k = input('Enter how many closest objects you want to display: ')

# firstRow = arr[user_choice]
tuple_array = []
train_id = 0
print "MINKOWSKI PROXIMITY MEASURES ARE BELOW"
print "#######################################"
class_votes = {}
correctCount = 0
data_frames = []
posterior_prob = 0
loopcount = 0
knn_array = []
confusion_predicted = []
confusion_actual = []
wrong_virginicas = []
for i in range(0, len(test_data)):
    actual_class = test_data_classes[i][0]
    firstRow = test_data[i]
	#storing the ids from the training set and how close they are to the curent test data element
    for row in training_data:
        minkowski = pow(pow((firstRow[0] - row[0]), 2),.25) + pow(pow((firstRow[1] - row[1]), 2),.25) + pow(pow((firstRow[2] - row[2]), 2),.25) + pow(pow((firstRow[3] - row[3]), 2), .25)
        tup = train_id, minkowski
        tuple_array.append(tup)
        train_id = train_id + 1
    tuple_array.sort(key = lambda tup: tup[1])

    print "Compared ID: " + str(i) + "  "
	#not comparing correct array value int trainging set
    for j in range(0, k):
        print "id:" + str(tuple_array[j][0]) + "  " + str(j) + "-prox: " + str(tuple_array[j][1])
        classs = iris_classes[tuple_array[j][0]][0]
        print "class is: " + classs
        if (classs in class_votes):
            class_votes[classs] += 1
        else :
            class_votes[classs] = 1
	print class_votes
    guess = max(class_votes.iteritems(), key = operator.itemgetter(1))[0]
    posterior_prob = float(max(class_votes.iteritems(), key = operator.itemgetter(1))[1])/float(k)
    data_frame_tuple = i + 1, test_data_classes[i][0], guess, posterior_prob
    loopcount = loopcount + 1
    print loopcount
    print data_frame_tuple
    data_frames.append(data_frame_tuple)
    if guess == test_data_classes[i][0]:
         correctCount += 1
    if actual_class =='Iris-setosa':
        confusion_actual.append(0)
    elif actual_class=='Iris-versicolor':
        confusion_actual.append(1)
    elif actual_class =='Iris-virginica':
        confusion_actual.append(2)
        if guess != 'Iris-virginica':
            wrong_virginicas.append(guess)
    if guess =='Iris-setosa':
        confusion_predicted.append(0)
    elif guess=='Iris-versicolor':
        confusion_predicted.append(1)
    elif guess =='Iris-virginica':
        confusion_predicted.append(2)
    class_votes.clear()
    print "\n"
    del tuple_array[: ]
    train_id = 0
print "len dataframes is : " + str(len(data_frames))
percentage = float(correctCount) / float(len(test_data))
print "The accuracy obtained from a minkowski classifier is: " + str(percentage * 100) + "%"
print "END OF MINKOWSKI MEASURES"
print '\n\n\n\n\n'

print '\n\n\n\n'
print confusion_matrix(confusion_actual,confusion_predicted)
print '\n\n\n\n'
print wrong_virginicas


print "Transaction ID    Actual   Predicted   Posterior"
f = open('KNNIrisOutput.txt','w')
f.write("Transaction ID    Actual   Predicted   Posterior\n\n")
for t in data_frames:
	#print(str(t[0]) + "   " + str(t[1]) + "   " + str(t[2]) + "   " + str(t[3]), file="KNNIrisOutput.txt")
    f.write(str(t[0]) + "   " + str(t[1]) + "   " + str(t[2]) + "   " + str(t[3]) + '\n')
    print str(t[0]) + "   " + str(t[1]) + "   " + str(t[2]) + "   " + str(t[3])
f.write("=====================================================================================\n")
f.write("END OF FILE")
f.close()



# Cosine Similarity Proximity Measure###(d1.d2 / || d1 || * || d2 || | )##############################################################################
cosine_array = []
counter = 0
correctCount=0
# print "COSINE SIMILARITY PROXIMITY MEASURES ARE BELOW"
# print "#######################################"#
# for i in range(0, len(test_data)):
#     actual_class = test_data_classes[i][0]
#     firstRow = test_data[i]
#     for row in training_data:
#         dot = firstRow[0] * row[0] + firstRow[1] * row[1] + firstRow[2] * row[2] + firstRow[3] * row[3]
#         lens1 = pow(pow(firstRow[0], 2) + pow(firstRow[1], 2) + pow(firstRow[2], 2) + pow(firstRow[3], 2), .5)
#         lens2 = pow(pow(row[0], 2) + pow(row[1], 2) + pow(row[2], 2) + pow(row[3], 2), .5)
#         cosine = dot / (lens1 * lens2)
#         cosine_tup = counter, cosine
#         cosine_array.append(cosine_tup)
#         counter = counter + 1
#     #print "number: " + str(counter) + "dot: " + str(dot) + "lens1: " + str(lens1) + "lens2: " + str(lens2) + "cosine: " + str(cosine)
#     counter = counter + 1
#     cosine_array.sort(key = lambda tup: tup[1], reverse = True)
#     print "Compared ID: " + str(i) + "  "
#     for j in range(0, k):
#         print "id:" + str(cosine_array[j][0]) + "  " + str(j) + "-prox: " + str(cosine_array[j][1])
#         classs = iris_classes[cosine_array[j][0]][0]
#         print "Cosine array [j][0] is: " + str(cosine_array[j][0])
#         print "class is: " + classs
#         if (classs in class_votes):
#             class_votes[classs] += 1
#         else :
#             class_votes[classs] = 1
# 	print class_votes
#     guess = max(class_votes.iteritems(), key = operator.itemgetter(1))[0]
#     data_frame_tuple = i + 1, test_data_classes[i][0], guess, posterior_prob
#     print data_frame_tuple
#     data_frames.append(data_frame_tuple)
#     print "Guess is " + guess
#     print "actual is " + actual_class
#     if guess == actual_class:
#          correctCount += 1
#     class_votes.clear()
#     print "\n"
#     del tuple_array[: ]
#     train_id = 0
#     for j in range(1, k + 1):
#         print "id:" + str(cosine_array[j][0]) + "  " + str(j) + "-prox: " + str(cosine_array[j][1])
#         print "\n"#
#     del cosine_array[: ]
#     counter = 0
# print "END OF COSINE MEASURES"
#
# print "Cosine Guess percentage is: " + str(float(correctCount)/float(len(test_data))*100)

#
#print cosine_array


# results = PCA(arr)# print results.fracs# print arr

############################################################################## Income Data Set## with open('income_tr.csv', 'rb') as f: #reader = csv.DictReader(f)# data = next(reader)# print data#
# for row in reader: #list_data.append(row)### for r in list_data: #print r#############################################################################
