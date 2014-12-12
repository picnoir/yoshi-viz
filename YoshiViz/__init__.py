import json

#read the data in txt and write it into string
def txtToString(fileDirectory):

    #open file
    f=open(fileDirectory)
    #temp(string) txt to string
    temp = f.read()   
    return temp

#transfer string into python object (json form)
def StringToObj(temp):
    data = json.loads(temp)
    return data

#test
#print (inputData())
#print (StringToObj(txtToString()))
