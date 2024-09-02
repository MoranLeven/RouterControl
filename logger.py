import json 

def saveCurrentUserList(data):
    file = open('currentUsers.json',"w+")
    file.write(data)
    file.close()

def getCurrentUserList():
    file = open('currentUsers.json',"r+")
    data = json.loads(file.read())
    return data 

def saveStaticIPUserList(data):
    file = open('staticIPUsers.json',"w+")
    file.write(json.dumps(data))
    file.close()

def getStaticIPUserList():
    file = open('staticIPUsers.json',"r+")
    data = json.loads(file.read())
    return data 


def saveTrafficControlledUserList(data):
    file = open('trafficControlledUsers.json',"w+")
    file.write(json.dumps(data))
    file.close()
    

def getTrafficControlledUserList():
    file = open('trafficControlledUsers.json',"r+")
    data = json.loads(file.read())
    return data
