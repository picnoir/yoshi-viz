import json

#global constant variable for thresholds
#geographical distance
GEOGRAPHICAL_DISTANCE = 4000
#culture distance(The data is already in percentage)
CULTURAL_DISTANCE = 15.0
#average milestones
AVERAGE_MILESTONES = 0.1
#hierarchical degree
HIERARCHICAL_DEGREE = 0.8
#self similarity
SELF_SIMILARITY = 0.9
#average subscription
AVERAGE_SUBSCRIPTION = 9.794
#average user commits 
AVERAGE_USER_COMMITS = 14.22
#average user collaboration files
AVERAGE_USER_COLLABORATION_FILES = 0.200
#average file contributor
AVERAGE_FILE_CONTRIBUTOR = 1.220

#read the data in txt and write it into string
def TxtToString(fileDirectory):

    #open file
    f=open(fileDirectory)
    #temp(string) txt to string
    temp = f.read()   
    return temp

#transfer string into python object (json form)
def StringToObj(temp):
    data = json.loads(temp)
    return data

#judge if is high eneagement, return boolean value, True if engagement is high
def Engagement(uniqueComments, avgSubscriptions, avgeUserCommits, avgUserCollaborationFiles, avgeFileContributors):
    if (uniqueComments == True and avgSubscriptions >= AVERAGE_SUBSCRIPTION and avgeUserCommits >= AVERAGE_USER_COMMITS
        and avgUserCollaborationFiles >= AVERAGE_USER_COLLABORATION_FILES and avgeFileContributors >= AVERAGE_FILE_CONTRIBUTOR):
        return True
    else:
        return False

#judge if is informal or not, return boolean value, True if it is informal
def Informality(avgMilestonesPeriod, hierarchyDegree, hasWiki):
    if (avgMilestonesPeriod <= AVERAGE_MILESTONES and hierarchyDegree <= HIERARCHICAL_DEGREE and hasWiki == True):
        return True
    else:
        return False


#judge if is situated, return boolean vaule, True if situatedness is nearby, Flase is for far alway remoteness 
def Situatedness(avgDistance, avgCulturalDistance):
    if (avgDistance <= GEOGRAPHICAL_DISTANCE and avgCulturalDistance <= CULTURAL_DISTANCE):
        return True
    else:
        return False

#judge if is NoP, True if it is NoP
def NetworkOfPractice(selfSimilarity):
    if selfSimilarity >= SELF_SIMILARITY :
        return True
    else:
        return False

    
