#dependencies 
import os 
import json
import requests
import re
from url import getData, getUrl, getHeaders
from dataProcessing import getSessionID

#The router class
class Router(object):
    cookies={}
    is_loggedIn = False 

    def __init__(self,username="Admin",password="d41d8cd98f00b204e9800998ecf8427e"):
        self.username  = username
        self.password = password

    def login(self):
        headers = getHeaders()
        data = getData('login')
        url = getUrl('login')
        response = requests.post(url,cookies=self.cookies,data=data,headers=headers,verify=False)
        #get the sessionID
        sessionID = getSessionID(response)
        if response.status_code == 200 and sessionID.get('SessionID',None) != None:
            self.is_loggedIn = True 
            self.cookies = sessionID
            return "[+] Logged In Successfully"
        else:
            self.is_loggedIn = False 
            return "[!] Logging Unsuccessful"

    def validateIp(self,IPADDR):
        ip = IPADDR 
        regex_str = ""

    def validateMAC(self,MACADDR):
        pass 

    
    



