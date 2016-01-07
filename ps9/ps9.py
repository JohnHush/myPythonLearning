# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subjects = {}
    for line in inputFile:
        tmp = line.strip().split(',')
        subjects[ tmp[0] ] = ( int(tmp[1]) , int(tmp[2]) )
    return subjects

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return subInfo1[0]>subInfo2[0]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return subInfo1[1]<subInfo2[1]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    return (subInfo1[0]/subInfo1[1])>(subInfo2[0]/subInfo2[1])

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    select_subs = {}
    sorted_dict = subjects.items()
    total_work = 0 

    listLength = len(sorted_dict)
    while listLength > 0:
        for i in range( listLength - 1 ):
            if not comparator( sorted_dict[i][1] , sorted_dict[i+1][1] ):
                tmp = sorted_dict[i]
                sorted_dict[i] = sorted_dict[i+1]
                sorted_dict[i+1] = tmp
        listLength -= 1

    for i in range( len(sorted_dict) ):
        total_work += sorted_dict[i][1][1]
        if total_work > maxWork:
            break
        select_subs[sorted_dict[i][0]] = sorted_dict[i][1]

    return select_subs

#
# Problem 3: Subject Selection By Brute Force
#
def workamount( list_subjects ):
    work = 0
    for i in xrange( len(list_subjects) ):
        work += list_subjects[i][1][1]
    return work

def valueamount( list_subjects ):
    value = 0
    for i in xrange( len(list_subjects) ):
        value += list_subjects[i][1][0]
    return value


def selections( list_subjects , n ):
    """
    Returns a list of combinations with n elements 
    in list_subjects, 
    recursion method
    integer n not greater than len(list_subjects)
    """
    if n == 0 :
        yield []
    for i in xrange( len(list_subjects) ):
        for cc in selections( list_subjects[i+1:] , n-1 ):
            yield [list_subjects[i]] + cc

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    listLength = len( subjects.items() )
    value = 0 
    flag = False
    item_selected = []
    dict_selected = {}

    while listLength >0:
        for item in selections( subjects.items() , listLength ):
            if workamount( item ) <= maxWork:
                flag = True
                if valueamount( item ) > value:
                    value = valueamount( item )
                    item_selected = item
        if flag == True:
            break
        listLength -= 1
    for i in xrange( len(item_selected) ):
        dict_selected[ item_selected[i][0] ] = item_selected[i][1]
    return dict_selected

subjects = loadSubjects( SHORT_SUBJECT_FILENAME )
print bruteForceAdvisor( subjects , 3 )
print bruteForceAdvisor( subjects , 4 )
print bruteForceAdvisor( subjects , 5 )
print bruteForceAdvisor( subjects , 6 )
print bruteForceAdvisor( subjects , 7 )

