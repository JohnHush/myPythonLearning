'''
Created on Sep 16, 2010
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
Output:     the most popular class label

@author: pbharrin
'''
from numpy import *
import operator
from os import listdir

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def file2matrix(filename):
    love_dictionary={'largeDoses':3, 'smallDoses':2, 'didntLike':1}
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if(listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm( dataSet ):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile( minVals , ( m , 1 ) )
    normDataSet = normDataSet/tile(ranges , (m,1))
    return normDataSet , ranges , minVals

def datingClassTest():
    hoRatio = 0.1
    datingMat , datingLabel = file2matrix('datingTestSet.txt')
    normMat , ranges , minVals = autoNorm(datingMat)
    m = normMat.shape[0]
    numTestVecs = int( m * hoRatio )
    errorCount = 0.
    for i in range( numTestVecs ):
        classifierResult = classify0( normMat[i , :] , normMat[numTestVecs:m , :] ,\
                                      datingLabel[numTestVecs:m] , 3 )
        print "the classifier came back with: %d , the real answer is : %d"\
        % ( classifierResult , datingLabel[i] )
        if ( classifierResult != datingLabel[i] ) : errorCount += 1.
    print "the total error rate is : %f" % (errorCount/float(numTestVecs))

def classifyPerson():
    resultList = [ 'not at all' , 'in small doses' , 'in large doses']
    percentTats = float(raw_input( "percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequenty flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))

    datingMat , datingLabel = file2matrix('datingTestSet.txt')
    normMat , ranges , minVals = autoNorm(datingMat)
    inArr = array([ffMiles , percentTats , iceCream])
    classifierResult = classify0( (inArr-minVals)/ranges , normMat , datingLabel , 3 )
    print "You will probably like this person: " , resultList[classifierResult-1]


def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros(( m , 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        # fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileNameStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s'  %fileNameStr )
    testFileList = listdir('testDigits')
    errorCount = 0.
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        # fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileNameStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' %fileNameStr)
        classifierResult = classify0( vectorUnderTest , trainingMat , hwLabels , 5 )
        print " the classifier came back with :%d , the real answer is: %d"\
                            %( classifierResult , classNumStr )
        if ( classifierResult != classNumStr ): errorCount += 1.
    print "\n the total number of errors is: %d" % errorCount
    print "\n the total error rate is: %f" % (errorCount/float(mTest))
