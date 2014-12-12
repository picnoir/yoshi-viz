import json
from __init__ import *


def DecisionTreeAlgorithm(uniqueComments, avgSubscriptions, avgeUserCommits, avgUserCollaborationFiles, avgeFileContributors, avgMilestonesPeriod, hierarchyDegree, hasWiki, avgDistance, avgCulturalDistance, selfSimilarity):
    CommunityType = []
    #Situatedness
    if Situatedness(avgDistance, avgCulturalDistance):
        CommunityType.append('CoP')
        return CommunityType
    else:
        #Informality
        if Informality(avgMilestonesPeriod, hierarchyDegree, hasWiki):
            CommunityType.append('IN')
            #Engagement
            if Engagement(uniqueComments, avgSubscriptions, avgeUserCommits, avgUserCollaborationFiles, avgeFileContributors):
                CommunityType.append('IC')
                return CommunityType
            #judge if is NoP
            elif NetworkOfPractice(selfSimilarity):
                CommunityType.append('NoP')
                return CommunityType
            #neither IC and NoP
            else:
                return CommunityType
            
        else:
            CommunityType.append('FN')
            if Engagement(uniqueComments, avgSubscriptions, avgeUserCommits, avgUserCollaborationFiles, avgeFileContributors):
                CommunityType.append('IC')
                return CommunityType
            elif NetworkOfPractice(selfSimilarity):
                CommunityType.append('NoP')
                return CommunityType
            else:
                return CommunityType




#code below will done in report_generator
fileDirectory = r'.\input.txt'
#read from txt
temp = TxtToString(fileDirectory)
#string to python object
data = StringToObj(temp)
#test decision tree
print('RepositoryOwner RepositoryName type')
for i in range(len(data['DataCommunity'])):
    tempCommunityType = DecisionTreeAlgorithm(data['DataCommunity'][i]['uniqueCommenterExists'],data['DataQuality'][i]['avgSubscriptions'],data['DataQuality'][i]['avgeUserCommits'],data['DataQuality'][i]['avgUserCollaborationFiles'],data['DataQuality'][i]['avgeFileContributors'], data['DataCommunity'][i]['avgMilestonesPeriod'],data['DataCommunity'][i]['hierarchyDegree'],data['DataQuality'][i]['hasWiki'], data['DataCommunity'][i]['avgDistance'], data['DataCommunity'][i]['avgCulturalDistance'], data['DataCommunity'][i]['selfSimilarity'])
    print(data['DataCommunity'][i]['RepoOwner'],data['DataCommunity'][i]['RepoName'],tempCommunityType)

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

#test informality(true is informal)
'''
for i in range(len(data['DataCommunity'])):
    informal = Informality(data['DataCommunity'][i]['avgMilestonesPeriod'],data['DataCommunity'][i]['hierarchyDegree'],data['DataQuality'][i]['hasWiki'])
    print (informal)
'''

#test situated distance
'''
for i in range(len(data['DataCommunity'])):
    situated = Situatedness(data['DataCommunity'][i]['avgDistance'], data['DataCommunity'][i]['avgCulturalDistance'])
    print (situated)
'''
