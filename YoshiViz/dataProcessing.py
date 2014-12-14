'''
this file is the function of processing the data
F1:(TxtToString)from txt raw data to string
F2:(StringToObj)from tring to Json form data
'''
import json

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
