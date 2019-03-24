#Lab 6 implemented in Python, R was being slow

#import nltk
import numpy as np
import csv
#import urllib2
from collections import Counter
import operator
import matplotlib.pyplot as plt
import math as math

def computeYearOccurence(year):
    rang = (52-(2015-year)) * 100




#billboard_lyrics_1964-2015.csv
#URL implementatino from website
# url = 'https://raw.githubusercontent.com/walkerkq/musiclyrics/master/billboard_lyrics_1964-2015.csv'
# response = urllib2.urlopen(url)
# cr = csv.reader(response)

my_data = np.genfromtxt('billboard_lyrics_1964-2015.csv', delimiter=',',dtype = None)
filteredWords = np.genfromtxt('Terms-to-Block.csv', delimiter=',",',dtype = None)
stopWords = open('stop-word-list.txt').read().splitlines()

explicitWords = []
for word in filteredWords:
    explicitWords.append(word[2:len(word)-2])

#############################################################
#############################################################
allLyrics = {}
allLyrics2 = {}
removedKeys = {}
explicitCounts = {}
yearExplicit = {}
missingLyrics = []
count = 0
first = 5001#Use 5001 for all songs of 2015
last = 5101
for i in range(first, last):
    lyrics = my_data[i][4]
    if lyrics != "NA":
        lyrics = lyrics[1:len(lyrics)-1]
        title = my_data[i][1]
        year = my_data[i][3]
        title = title[1:len(title)-1]
        numOcc = Counter(lyrics.split())
        sorted_x = sorted(numOcc.items(), key=operator.itemgetter(1), reverse=True)
        tup = (sorted_x,year)
        allLyrics.update({title:tup})
        allLyrics2.update({title:numOcc})
    else:
        missingLyrics.append(my_data[i][1])
    #sys.exit()
for song in allLyrics.keys():
    d = allLyrics.get(song)
    #print(d[0])
    #print(d[1])#Prints Year
    #print(d)
    for item in d[0]:
        for stopword in stopWords:
            if stopword == item[0]:
                count = count + 1
                #print(allLyrics.get(song)[0])
                #print(type(allLyrics.get(song)[0]))
                #print(item[0])
                #print(type(item[0]))
                #print(item)
                #print(type(item))
                allLyrics.get(song)[0].remove(item)
                #print(allLyrics.get(song)[0])
                if not stopword in removedKeys:
                    removedKeys[stopword] = 1
                else:
                    removedKeys[stopword] += 1
        for explicit in explicitWords:
            if explicit == item[0]:
                if not explicit in explicitCounts:
                    explicitCounts[explicit] = 1
                else:
                    explicitCounts[explicit] += 1
                if not d[1] in yearExplicit:
                    yearExplicit[d[1]] = 1
                else:
                    yearExplicit[d[1]]+=1

sorted_explicit = sorted(explicitCounts.items(), key=operator.itemgetter(1),reverse = True)
sorted_years = sorted(yearExplicit.items(), key=operator.itemgetter(0))

# globalLyricsCount = {}
# for song in allLyrics.keys():
#     d = allLyrics.get(song)
#     for item in d[0]:
#         if not item[0] in globalLyricsCount:
#             #print(item[0])
#             globalLyricsCount[item[0]] = 1
#         else:
#             globalLyricsCount[item[0]] += 1
# print(len(globalLyricsCount))

globalLyricsCount2 = {}
for song in allLyrics2.keys():
    d = allLyrics2.get(song)
    for item in d:
        if not item in globalLyricsCount2:
            #print(item[0])
            globalLyricsCount2[item] = 1
        else:
            globalLyricsCount2[item] += 1

stopwordcountall = 0
for song in allLyrics2.keys():
    d = allLyrics2.get(song)
    for word in d.keys():
        for stopword in stopWords:
            if stopword == word:
                stopwordcountall = stopwordcountall + 1
                del allLyrics2.get(song)[word]
stopwordcount = 0
for word in globalLyricsCount2.keys():
    for stopword in stopWords:
        if stopword == word:
            stopwordcount = stopwordcount + 1
            del globalLyricsCount2[word]

wordStems = {}
for a in globalLyricsCount2.keys():
    for b in globalLyricsCount2.keys():
        if a != b and len(a)>2:
            if a in b:
                if a not in wordStems:
                    wordStems[a]=1
                else:
                    wordStems[a] += 1
sortedstems = sorted(wordStems.items(), key=operator.itemgetter(1),reverse = True)
print('\n\n')
print("top word stems and occurences of them: ")
print(sortedstems)
print('\n\n')

#TF-IDF Calculations
w, h =  last-first, len(globalLyricsCount2)
matrix = np.zeros((w, h))
doc_order = []
word_order = []
word_map = {}
word_pos = 0
print("Size of Matrices used for Tf-IDF calculations")
print(matrix.shape)#166,2
# for song in allLyrics2.keys():
#     doc_order.append(song)
for word in globalLyricsCount2:
    word_order.append(word)
    word_map.update({word:word_pos})
    word_pos = word_pos + 1
#print(word_map)

#have counts of each word in each song
#have total counts of words combined from each song
#If normalizing, I have the sorted counts to first word for each song is the max
#sparsity = count/totalEntries
#I need some way to map the position of each word in the matrix
row = 0
col = 0
pos = 0
for song in allLyrics2.keys():
    for word in allLyrics2.get(song):
        count = allLyrics2.get(song).get(word)
        maptoword = word_map.get(word)
        matrix[row, maptoword] = count
        col = col + 1
    col = 0
    row = row + 1
#print(matrix)

sparseCount = 0
idfCounts = 0
idfCount = [0] * h
#print(idfCount)
pos = 0
for y in matrix:
    for z in y:
        if z<1:
            sparseCount = sparseCount + 1
        else:
            idfCount[pos] = idfCount[pos] + 1
        pos = pos+1
    pos = 0
print("Sparseness of matrix: ")
sparseness = float(sparseCount)/float(w * h)
print(sparseness)



#idf of each word = log10(numDocs/total occurence of that word)
idfMap = {}
for word in globalLyricsCount2:
    maptoword = word_map.get(word)
    idf = round(math.log10((last-first)/float(idfCount[maptoword])),3)
    idfMap.update({word:idf})
sortedIDF = sorted(idfMap.items(), key=operator.itemgetter(1))
print('\n\n')
for j in range(10):
    print(sortedIDF[j])
print('\n\n')
print(" Number of Unique documents each word appeared in:")
for j in range(10):
    print(str(sortedIDF[j][0]) + ": " + str(idfCount[word_map[sortedIDF[j][0]]]))
print('\n\n')

#if a term appears in the document, updatte the entry with the idf associated with that term
    #column of matrix is associated with term
norms = [0] * (w)
IDFmatrix = np.zeros((w, h))
row = 0
col = 0
for song in allLyrics.keys():
    doc_order.append(song)
    for word in allLyrics2.get(song):
        maptoword = word_map.get(word)
        for r in range(last-first):
            if matrix[r,maptoword] > 0:
                IDFmatrix[r,maptoword] = idfMap.get(word)
print('\n\n')
print('IDF matrix: ')
for x in IDFmatrix:
    print(x)
print('\n\n')

norm = 0
row = 0
for y in IDFmatrix:
    for z in y:
        norm = norm + (z * z)
    norms[row] = math.sqrt(norm)
    row = row + 1
    norm = 0
#print(norms)
print("\n\n")
for song in allLyrics.keys():
    d = allLyrics.get(song)
    print(str(song) + ":")
    for x in range(5):
        print(d[0][x])
    print("\n")

#multiply the term frequency(matrix) by the idf matrix
tfIDFmatrix = np.zeros((w, h))
max = 0
for row in range(w):
    for col in range(h):
        tfIDFmatrix[row,col] = round(matrix[row, col] * IDFmatrix[row,col],3)
        if tfIDFmatrix[row,col] > max:
            max = tfIDFmatrix[row,col]

col = 0
print("Song: " + str(doc_order[0]))
tfIDFmap = {}
for word in allLyrics2.get(doc_order[0]):
    maptoword = word_map.get(word)
    print("Word: " + str(word)+ "    tfidfValue: " + str(tfIDFmatrix[0,maptoword]))
    tfIDFmap.update({word:tfIDFmatrix[0,maptoword]})
sortedIDFmap = sorted(tfIDFmap.items(), key=operator.itemgetter(1),reverse = True)
print('TF-IDF values for the song the heart wants what it wants')
for k in sortedIDFmap:
    print(k)










#CHECKS IF WORDS WERE REMOVED CORRECTLY
# sorted_global = sorted(globalLyricsCount.items(), key=operator.itemgetter(1))
# print(globalLyricsCount['a'])
# for thing in removedKeys:
#     if thing in globalLyricsCount:
#         print(thing)

#




#Plotting
#############################################################
#############################################################
# print(sorted_explicit)
# print(sorted_years)
#
# # plt.bar(range(len(yearExplicit)), yearExplicit.values(), align='center')
# # plt.xticks(range(len(yearExplicit)), yearExplicit.keys())
#
# x, y = zip(*sorted_years) # unpack a list of pairs into two tuples
# # flo = y.astype(np.float)
# plt.bar(range(len(x)), y, align='center')
# newx = []
# for year in x:
#     newx.append(year[2:])
# plt.xticks(range(len(x)), newx)
# plt.show()

#############################################################
#############################################################

# #Accesses the count of the word wooly in the song wooly bully
# print(allLyrics['wooly bully']['wooly'])
# #Accesses the highest
# print(max(allLyrics['wooly bully'].iteritems(), key=operator.itemgetter(1))[0])
