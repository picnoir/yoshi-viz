'''
this file is the algorithm part
F1:(DecisionTreeAlgorithm)input the metrics to define(return) the community type
'''
import json
#from thresholds_functions import Engagement,Informality,Situatedness,NetworkOfPractice

'''
this file is the preparation of decision tree
F1:(Engagement)judge if is high eneagement, return boolean value, True if engagement is high
F2:(Informality)judge if is informal or not, return boolean value, True if it is informal
F3:(Situatedness)judge if is situated, return boolean vaule, True if situatedness is nearby, Flase is for far alway remoteness 
F4:(NetworkOfPractice)judge if is NoP, True if it is NoP
'''
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

#judge if is high eneagement, return boolean value, True if engagement is high
def Engagement(
        uniqueComments, avgSubscriptions, avgeUserCommits,
        avgUserCollaborationFiles, avgeFileContributors):
    if (uniqueComments and
        avgSubscriptions >= AVERAGE_SUBSCRIPTION and
        avgeUserCommits >= AVERAGE_USER_COMMITS and
        avgUserCollaborationFiles >= AVERAGE_USER_COLLABORATION_FILES and
        avgeFileContributors >= AVERAGE_FILE_CONTRIBUTOR):
        return True
    else:
        return False

#judge if is informal or not, return boolean value, True if it is informal
def Informality(
    avgMilestonesPeriod, hierarchyDegree, hasWiki):
    if (avgMilestonesPeriod <= AVERAGE_MILESTONES and
        hierarchyDegree <= HIERARCHICAL_DEGREE and
        hasWiki):
        return True
    else:
        return False


#judge if is situated, return boolean vaule, True if situatedness is nearby, Flase is for far alway remoteness 
def Situatedness(
    avgDistance, avgCulturalDistance):
    if (avgDistance <= GEOGRAPHICAL_DISTANCE and
        avgCulturalDistance <= CULTURAL_DISTANCE):
        return True
    else:
        return False

#judge if is NoP, True if it is NoP
def NetworkOfPractice(selfSimilarity):
    if selfSimilarity >= SELF_SIMILARITY :
        return True
    else:
        return False
'''
above is the thresholds functions
'''

#one repoitory name to one result
def CommunityType(fileDirectory,repositoryName):
    #open file
    f=open(fileDirectory)
    #temp(string) txt to string
    temp = f.read()  
    data = json.loads(temp)
    for i in range(len(data['DataCommunity'])):
        if data['DataCommunity'][i]['RepoName'] ==repositoryName:
            tempCommunityType = DecisionTreeAlgorithm(
                    data['DataCommunity'][i]['uniqueCommenterExists'],
                    data['DataQuality'][i]['avgSubscriptions'],
                    data['DataQuality'][i]['avgeUserCommits'],
                    data['DataQuality'][i]['avgUserCollaborationFiles'],
                    data['DataQuality'][i]['avgeFileContributors'],
                    data['DataCommunity'][i]['avgMilestonesPeriod'],
                    data['DataCommunity'][i]['hierarchyDegree'],
                    data['DataQuality'][i]['hasWiki'],
                    data['DataCommunity'][i]['avgDistance'],
                    data['DataCommunity'][i]['avgCulturalDistance'],
                    data['DataCommunity'][i]['selfSimilarity'])
            return tempCommunityType
            break
        if i == len(data['DataCommunity'])-1:
            return 'no such repository name'

#already defined algorithm 
def DecisionTreeAlgorithm(
    uniqueComments, avgSubscriptions, avgeUserCommits,
    avgUserCollaborationFiles, avgeFileContributors,
    avgMilestonesPeriod, hierarchyDegree, hasWiki,
    avgDistance, avgCulturalDistance, selfSimilarity):

    CommunityType = []
    #Situatedness
    if Situatedness(avgDistance, avgCulturalDistance):
        CommunityType.append('Community of Proctice')
    #Informality
    if Informality(avgMilestonesPeriod, hierarchyDegree, hasWiki):
        CommunityType.append('Informal Network')
        #Engagement
        if Engagement(uniqueComments, avgSubscriptions, avgeUserCommits, avgUserCollaborationFiles, avgeFileContributors):
            CommunityType.append('Informal Community')
            return CommunityType
        #judge if is NoP
        elif NetworkOfPractice(selfSimilarity) and \
            not Situatedness(avgDistance, avgCulturalDistance):
            CommunityType.append('Network of Practice')
            return CommunityType
        #neither IC and NoP
        else:
            return CommunityType
            
    else:
        CommunityType.append('Formal Network')
        if Engagement(uniqueComments, avgSubscriptions, avgeUserCommits, avgUserCollaborationFiles, avgeFileContributors):
            CommunityType.append('Informal Community')
            return CommunityType
        elif NetworkOfPractice(selfSimilarity) and \
            not Situatedness(avgDistance, avgCulturalDistance):
            CommunityType.append('Network of Practice')
            return CommunityType
        else:
            return CommunityType


'''
#file director        
fileDirectory = r'.\input.txt'
#test decision tree
#repositoryName = input("Please input repository name:\n")
repositoryName = 'bootstrap'
print(CommunityType(fileDirectory,repositoryName))
'''



#test for all repository for one time
#file director        
#fileDirectory = r'.\input.txt'
#read from txt
#temp = TxtToString(fileDirectory)
#string to python object
#data = StringToObj(temp)
'''
for i in range(len(data['DataCommunity'])):

        tempCommunityType = DecisionTreeAlgorithm(
                    data['DataCommunity'][i]['uniqueCommenterExists'],
                    data['DataQuality'][i]['avgSubscriptions'],
                    data['DataQuality'][i]['avgeUserCommits'],
                    data['DataQuality'][i]['avgUserCollaborationFiles'],
                    data['DataQuality'][i]['avgeFileContributors'],
                    data['DataCommunity'][i]['avgMilestonesPeriod'],
                    data['DataCommunity'][i]['hierarchyDegree'],
                    data['DataQuality'][i]['hasWiki'],
                    data['DataCommunity'][i]['avgDistance'],
                    data['DataCommunity'][i]['avgCulturalDistance'],
                    data['DataCommunity'][i]['selfSimilarity'])
        print(data['DataCommunity'][i]['RepoOwner'],data['DataCommunity'][i]['RepoName'],tempCommunityType)
'''



        
#test
#print related object
#print (data['DataQuality'][0]['RepoOwner'],data['DataQuality'][0]['monthlyEventsStdDev'])
#print (data['DataCommunity'][0]['RepoOwner'],data['DataCommunity'][0]['avgMilestonesPeriod'])


#test high engagement(true is high engagement)
'''
for i in range(len(data['DataCommunity'])):
    highEngagement = Engagement(data['DataCommunity'][i]['uniqueCommenterExists'],data['DataQuality'][i]['avgSubscriptions'],data['DataQuality'][i]['avgeUserCommits'],data['DataQuality'][i]['avgUserCollaborationFiles'],data['DataQuality'][i]['avgeFileContributors'])
    print (highEngagement)
'''

#test informality(true is informal) of all
'''
for i in range(len(data['DataCommunity'])):
    informal = Informality(data['DataCommunity'][i]['avgMilestonesPeriod'],data['DataCommunity'][i]['hierarchyDegree'],data['DataQuality'][i]['hasWiki'])
    print (informal)
'''

#test situated distance (true is near situatedness) of all
'''
for i in range(len(data['DataCommunity'])):
    situated = Situatedness(data['DataCommunity'][i]['avgDistance'], data['DataCommunity'][i]['avgCulturalDistance'])
    print (situated)
'''
#test self similarity (trur is high self-similartity) of all
'''
for i in range(len(data['DataCommunity'])):
    selfSimi = NetworkOfPractice(data['DataCommunity'][i]['selfSimilarity'])
    print (selfSimi)

'''

    

