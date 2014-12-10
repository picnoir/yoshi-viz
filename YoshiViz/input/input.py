import json
#file name
file_directory = '.\input.txt'
#open file
f=open(file_directory)
#temp(string) txt to string
temp = f.read()
#string to python object
data = json.loads(temp)
#print related object
print (data['DataQuality'][0]['RepoOwner'],data['DataQuality'][0]['monthlyEventsStdDev'])
print (data['DataCommunity'][0]['RepoOwner'],data['DataCommunity'][0]['avgMilestonesPeriod'])

