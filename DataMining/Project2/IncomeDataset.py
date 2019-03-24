import csv
import numpy as np
#import scipy as sci
import matplotlib as plot
from math import exp,sqrt,log10,log1p
#from matplotlib.mlab import PCA
import matplotlib.pyplot as plt
from numpy import recfromcsv
#import pylab as P
import operator
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc



k = input('Enter how many objects you want to test against: ')
income = "income_tr.csv"
income_training = "income_te.csv"

# matrix = np.loadtxt(iris, delimiter=",")
# print np.matrix(matrix)
                                    #4                                                              8                           11                              13                          15
#"ID","age","workclass","fnlwgt","education","education_cat","marital_status","occupation","relationship","race","gender","capital_gain","capital_loss","hour_per_week","native_country","class"
#"9364",38," Private",197077," HS-grad",9," Married-civ-spouse"," Other-service"," Husband"," White"," Male",0,0,40," United-States"," <=50K"

#age computed as is (Distribution was nomal enough to continue)
#workclass -> Almost all were private so not taken into account
# fnlwgt -> Ambiguous and doesn't mean anything so not taken into account
# education -> Not use since education_cat is already numerical and represents the same data

#education_cat -> Used in computation, No Transformation needed
    #Up until high school -> 1, some college/associates -> 2, bachelors -> 3, post bachelors -> 4
#marital_status -> Married -> 2, Divorced -> 1, everything else -> 0
#occupation -> Almost All Different so not used in Proximity function
#relationship -> Does not provide meaningful information
#race -> White -> 1 black -> 2 asian-pac-islander -> 3 Amer-Indian-Eskimo ->4 other->5
#gender -> Male -> 1 Female ->2
#capital_loss -> 0->1, <=2000 -> 2, else -> 3
#capital_gain -> 0->1, <= 10000 -> 2, <=50000 -> 3, else -> 4
#native_country: United States -> 0 and International -> 1
#class -> Not computed for Proximity Function

#list_data = recfromcsv(income)
# list_data = np.recfromcsv(income, delimiter=',', filling_values=np.nan, case_sensitive=True, deletechars='', replace_space=' ')
prox_data = np.genfromtxt(income, dtype=None, delimiter=',', names=True, usecols=(0,1,5,6,8,9,10,11,12,13,14,15)) #Prints ID-> print list_data[0][0]
all_data = np.genfromtxt(income, dtype=None, delimiter=',', names=True)
#income_classes = np.genfromtxt("Iris_Test.csv", dtype = None, delimiter = ',', names = True, usecols = (4))# Prints ID - > print list_data[0][0]
training_income_data = np.genfromtxt(income_training, dtype=None, delimiter=',', names=True, usecols=(0,1,5,6,8,9,10,11,12,13,14,15))



#Calculations for the difference in income for those with at least a bachelors degree and those without
##############################################################################################################################
##############################################################################################################################
income = ""
education_cat = 0
bachelorsCount = 0
greaterThan50 = 0
nonBachGreaterThan50 = 0
missingData = 0

workclassCount = 0
missingWorkclass = 0
occupationArray=[]
relationshipArray=[]

greaterThan50ClassCount = 0
for row in all_data:
    if not np.isnan(row['education_cat']) and not row['class'] == None:
        education_cat = row['education_cat']
        income = row['class']
        if education_cat >= 13:
            bachelorsCount = bachelorsCount + 1
            if income == '" >50K"':
                greaterThan50 = greaterThan50+1
        else:
            if income == '" >50K"':
                nonBachGreaterThan50 = nonBachGreaterThan50+1
    else:
        missingData = missingData + 1

    if row['workclass']=='" Private"':
        workclassCount = workclassCount + 1
    elif row['workclass'] == '" ?"':
        missingWorkclass = missingWorkclass + 1

    occupationArray.append(row['occupation'])
    relationshipArray.append(row['relationship'])
    if row["class"] == '" >50K"':
        greaterThan50ClassCount +=1

occCounts = dict()
for i in occupationArray:
  occCounts[i] = occCounts.get(i, 0) + 1
print occCounts

#Uncomment to see graph of occupation counts
# plt.bar(range(len(occCounts)), occCounts.values(), align='center')
# plt.xticks(range(len(occCounts)), occCounts.keys())
# plt.rcParams.update({'font.size': 7})
#
# plt.show()

relCounts = dict()
for i in relationshipArray:
    relCounts[i] = relCounts.get(i,0) + 1
print relCounts

#Uncomment to see graph of occupation counts
plt.bar(range(len(relCounts)), relCounts.values(), align='center')
plt.xticks(range(len(relCounts)), relCounts.keys())
plt.rcParams.update({'font.size': 10})

#plt.show()

print "The percentage of people that have a workclass of Private is: " + str(float(workclassCount)/float(len(all_data))*100) + "%" + "and " + str(float(missingWorkclass)/len(all_data)*100) + "%" + "of the workclass data is missing"
print "The percentage of people with bachelors degrees that make above 50K is: \n" + str((float(greaterThan50)/bachelorsCount)*100) + "%"
print "The percentage of people without bachelors degrees that make above 50K is: \n" + str((float(nonBachGreaterThan50)/(len(all_data)-missingData-bachelorsCount)*100))+ "%"
##############################################################################################################################
##############################################################################################################################
print "\n\n"
print "Preprocessing done"
print "##################\n###################\n##################\n\n"
#user_choice = input('What id do you want to compare against? ')
#k = input('How many closest points do you want displayed? ')

#Transform Test Data
for row in prox_data:
    ################Transform education_cat to similar groups####################
    if row['education_cat'] <=9:
        row['education_cat'] = 1
    elif row['education_cat'] <= 12:
        row['education_cat'] = 2
    elif row['education_cat'] <= 13:
        row['education_cat'] = 3
    elif row['education_cat'] <= 14:
        row['education_cat'] = 4
    else:
        row['education_cat'] = 5
    ####################################################


    ################Transform Martial status for proximity####################
    if row['marital_status'] == " Married-civ-spouse":
        row['marital_status'] = 3
    elif row['marital_status'] == " Divorced":
        row['marital_status'] = 2
    else:
        row['marital_status'] = 1
    ####################################################

    ################Transform Race for proximity####################
    if row['race'] == " White":
        row['race'] = 1
    elif row['race'] == " Black":
        row['race'] = 2
    elif row['race'] == " Asian-Pac-Islander":
        row['race'] = 3
    elif row['race'] == " Amer-Indian-Eskimo":
        row['race'] = 4
    else:
        row['race'] = 5
    ####################################################


    ##############Transform gender data to Binary########################
    if row['gender'] == " Male":
        row['gender'] = 0
    else:
        row['gender'] = 1
    #############Tranform native country data##############################
    if row['native_country'] == " United-States":
        row['native_country'] = 1
    else:
        row['native_country'] = 2
    ####################################################

    if row['capital_gain'] == 0:
        row['capital_gain'] = 1
    elif row['capital_gain'] <= 10000:
        row['capital_gain'] = 2
    elif row['capital_gain'] <= 50000:
        row['capital_gain'] = 3
    else:
        row['capital_gain'] = 4

    if row['capital_loss'] == 0:
        row['capital_loss'] = 1
    elif row['capital_loss'] <= 2000:
        row['capital_loss'] = 2
    elif row['capital_loss'] <= 4000:
        row['capital_loss'] = 3
    else:
        row['capital_loss'] = 4

    if row['hour_per_week'] <= 30:
        row['hour_per_week'] = 1
    elif row['hour_per_week'] <= 40:
        row['hour_per_week'] = 2
    elif row['hour_per_week'] <= 50:
        row['hour_per_week'] = 3
    else:
        row['hour_per_week'] = 4


#Tansform Training Data
for row in training_income_data:
    ################Transform education_cat to similar groups####################
    if row['education_cat'] <=9:
        row['education_cat'] = 1
    elif row['education_cat'] <= 12:
        row['education_cat'] = 2
    elif row['education_cat'] <= 13:
        row['education_cat'] = 3
    elif row['education_cat'] <= 14:
        row['education_cat'] = 4
    else:
        row['education_cat'] = 5
    ####################################################


    ################Transform Martial status for proximity####################
    if row['marital_status'] == " Married-civ-spouse":
        row['marital_status'] = 3
    elif row['marital_status'] == " Divorced":
        row['marital_status'] = 2
    else:
        row['marital_status'] = 1
    ####################################################

    ################Transform Race for proximity####################
    if row['race'] == " White":
        row['race'] = 1
    elif row['race'] == " Black":
        row['race'] = 2
    elif row['race'] == " Asian-Pac-Islander":
        row['race'] = 3
    elif row['race'] == " Amer-Indian-Eskimo":
        row['race'] = 4
    else:
        row['race'] = 5
    ####################################################


    ##############Transform gender data to Binary########################
    if row['gender'] == " Male":
        row['gender'] = 0
    else:
        row['gender'] = 1
    #############Tranform native country data##############################
    if row['native_country'] == " United-States":
        row['native_country'] = 1
    else:
        row['native_country'] = 2
    ####################################################

    if row['capital_gain'] == 0:
        row['capital_gain'] = 1
    elif row['capital_gain'] <= 10000:
        row['capital_gain'] = 2
    elif row['capital_gain'] <= 50000:
        row['capital_gain'] = 3
    else:
        row['capital_gain'] = 4

    if row['capital_loss'] == 0:
        row['capital_loss'] = 1
    elif row['capital_loss'] <= 2000:
        row['capital_loss'] = 2
    elif row['capital_loss'] <= 4000:
        row['capital_loss'] = 3
    else:
        row['capital_loss'] = 4

    if row['hour_per_week'] <= 30:
        row['hour_per_week'] = 1
    elif row['hour_per_week'] <= 40:
        row['hour_per_week'] = 2
    elif row['hour_per_week'] <= 50:
        row['hour_per_week'] = 3
    else:
        row['hour_per_week'] = 4


    #print row

proximity_array = []
testRow = 0
age = 0
#|p-q|/(n-1) for ordinal data
#"ID","age","education_cat","marital_status","race","gender","capital_gain","capital_loss","hour_per_week","native_country"
# 0 1 5 6 9-14
age_array = []
# b=[]
gender = 0
country = 0
race = 0
marital = 0
relationship = 0
similarityArray = []
cosineArray = []
count = 0

class_votes = {}
correctCount = 0
data_frames = []
posterior_prob = 0
loopcount = 0
knn_array = []
confusion_predicted = []
confusion_actual = []
for i in range(0, len(prox_data)):
    comparatorRow = prox_data[i]
    actual_class = comparatorRow[11]
    for row in training_income_data:
        age_array.append(row['age'])
        age = abs(float(prox_data[testRow]['age'])-float(row['age']))
        education_cat = abs((float(prox_data[testRow]['education_cat'])-float(row['education_cat']))/4)
        # marital = abs((float(prox_data[testRow]['marital_status'])-float(row['marital_status']))/2)
        # race = abs((float(prox_data[testRow]['race'])-float(row['race']))/4)
        if comparatorRow['marital_status'] == row['marital_status']:
            marital = 1
        else:
            marital = 0
        if comparatorRow['relationship'] == row['relationship']:
            relationship = 1
        else:
            relationship = 0
        if comparatorRow['race'] == row['race']:
            gender = 1
        else:
            gender = 0
        if comparatorRow['gender'] == row['gender']:
            gender = 1
        else:
            gender = 0
        if comparatorRow['native_country'] == row['native_country']:
            country = 1
        else:
            country = 0
        capital_gain = abs((float(comparatorRow['capital_gain'])-float(row['capital_gain']))/4)
        capital_loss= abs((float(comparatorRow['capital_loss'])-float(row['capital_loss']))/4)
        hours = abs((float(comparatorRow['hour_per_week'])-float(row['hour_per_week']))/4)

        similarity = (gender) + (relationship) + (country)  + (race) + (education_cat) + (marital) + (capital_gain) + (capital_loss) + (hours) + (float(age)/100)

        #cosine_tuple = row[0],(gender) , (relationship) , (country)  , (race) , (education_cat) , (marital) , (capital_gain) , (capital_loss) , (hours) , (float(age)/100)
        simTup = row[0],similarity,row[11]
        similarityArray.append(simTup)

        #cosineArray.append(cosine_tuple)
    similarityArray.sort(key=lambda tup: tup[1],reverse=True)
    #
    # for j in range(0, k):
    #     print "id:" + str(tuple_array[j][0]) + "  " + str(j) + "-prox: " + str(tuple_array[j][1])
    #     classs = iris_classes[tuple_array[j][0]][0]
    #     print "class is: " + classs

    for m in range(0,k):
        if similarityArray[m][2] in class_votes:
            class_votes[similarityArray[m][2]]+=1
        else:
            class_votes[similarityArray[m][2]] = 1
    print class_votes

    guess = max(class_votes.iteritems(), key = operator.itemgetter(1))[0]
    posterior_prob = float(max(class_votes.iteritems(), key = operator.itemgetter(1))[1])/float(k)

    #Calculate Posterior Here:
    #==========================================================================

    #==========================================================================
    data_frame_tuple = i + 1, actual_class, guess, posterior_prob
    #loopcount = loopcount + 1
    #print loopcount
    #print data_frame_tuple
    data_frames.append(data_frame_tuple)
    if guess == actual_class:
         correctCount += 1
    if actual_class =='" <=50K"':
        confusion_actual.append(0)
    elif actual_class=='" >50K"':
        confusion_actual.append(1)
    if guess =='" <=50K"':
        confusion_predicted.append(0)
    elif guess=='" >50K"':
        confusion_predicted.append(1)
    class_votes.clear()
    print "\n"
    #del tuple_array[: ]
    #train_id = 0



    print "Record " + str(i)
    print "Compared ID: " + comparatorRow[0] + "  "
    for j in range(1,k+1):
        print "id:" + str(similarityArray[j][0]) + "  " + str(j) + "-prox: " + str(similarityArray[j][1])
    print "\n"
    del similarityArray[:]
    count = 0
print "END OF SIMILARITY MEASURES"
print '\n\n\n\n\n'
print str((float(correctCount)/float(len(prox_data)))*100) + "%"

print '\n\n\n\n'
print confusion_matrix(confusion_actual,confusion_predicted)
print '\n\n\n\n'


f = open('KNNIncomeOutput.txt','w')
f.write("Transaction ID    Actual   Predicted   Posterior\n\n")
for t in data_frames:
	#print(str(t[0]) + "   " + str(t[1]) + "   " + str(t[2]) + "   " + str(t[3]), file="KNNIrisOutput.txt")
    f.write(str(t[0]) + "   " + str(t[1]) + "   " + str(t[2]) + "   " + str(t[3]) + '\n')
    print str(t[0]) + "   " + str(t[1]) + "   " + str(t[2]) + "   " + str(t[3])
f.write("=====================================================================================\n")
f.write("END OF FILE")
f.close()

print "the number of classes greater than 50k is:  " + str(float(greaterThan50ClassCount/float(len(all_data))))

#P(class is above 50K) = P(Y) = 19.23%
#the number of classes greater than 50k is:  0.192307692308



#print similarityArray

# cosineVals = []
# for i in range(1, len(prox_data)):
#     firstRow = cosineArray[i]
#     for row in cosineArray:
#         dot = firstRow[1]*row[1] + firstRow[2]*row[2] + firstRow[3]*row[3] + firstRow[4] * row[4] + firstRow[5] * row[5] + firstRow[6] * row[6] + firstRow[7] * row[7] + float(firstRow[8] * row[8]) + float(firstRow[9] * row[9])
#         lens1 = pow(pow(firstRow[1],2) + pow(firstRow[2],2) + pow(firstRow[3],2) + pow(firstRow[4],2) + pow(firstRow[5],2) + pow(firstRow[6],2) + pow(firstRow[7],2) + pow(firstRow[8],2)
#         + pow(firstRow[9],2),.5)
#         lens2 = pow(pow(row[1],2) + pow(row[2],2) + pow(row[3],2) + pow(row[4],2) + pow(row[5],2) + pow(row[6],2) + pow(row[7],2) + pow(row[8],2)
#         + pow(row[9],2),.5)
#         cosine = dot/(lens1 * lens2)
#         cosine_tup = row[0],cosine
#         cosineVals.append(cosine_tup)
#         count = count + 1
#     cosineVals.sort(key=lambda tup: tup[1],reverse=True)
#     print "Compared ID: " + firstRow[0] + "  "
#     for j in range(1,k+1):
#         print "id:" + str(cosineVals[j][0]) + "  " + str(j) + "-prox: " + str(cosineVals[j][1])
#     print "\n"
#     del cosineVals[:]
#     count = 0
# print "END OF COSINE MEASURES"


#print "\n*******\n******\n\n****\n\n"


############################################################################
# with open(income, 'rb') as f:
#     reader = csv.DictReader(f)
#     data = next(reader)
#     # print data
#     for row in reader:
#         a = np.array([int(row["ID"]),int(row["age"]),row["workclass"],row["education"],int(row["education_cat"])])
#         list_data.append(a)
# #print str(list_data)
# arr = np.vstack(list_data)
# arr2 = np.vstack(list_data)
############################################################################
