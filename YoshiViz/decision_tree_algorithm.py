import json
from __init__ import *

fileDirectory = r'.\input.txt'
#read from txt
temp = TxtToString(fileDirectory)
#string to python object
data = StringToObj(temp)


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
