import json
from __init__ import *

fileDirectory = r'.\input.txt'
#read from txt
temp = txtToString(fileDirectory)
#string to python object
data = StringToObj(temp)

#test
#print related object
print (data['DataQuality'][0]['RepoOwner'],data['DataQuality'][0]['monthlyEventsStdDev'])
print (data['DataCommunity'][0]['RepoOwner'],data['DataCommunity'][0]['avgMilestonesPeriod'])


