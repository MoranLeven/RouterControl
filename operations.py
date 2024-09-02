from router import Router
from url import getData, getHeaders, getUrl
import requests
from logger import saveCurrentUserList, saveStaticIPUserList, saveTrafficControlledUserList
from dataProcessing import getCurrentConnectedIPs, getSubmitValueForAddUserAndDeleteUser, getSubmitValueForUserTrafficControlAddAndDelete, getCurrentStaticIPs,getCurrentTrafficControlledIPs
import json
from utils import process_mac, get_mac



def getCurrentConnections(router, logData=True):
    currentConnectedUserList = []
    cookies = router.cookies
    data = getData('getActiveConnections')
    headers = getHeaders()
    url = getUrl('getActiveConnections')
    #lets make the call to router 
    response = requests.get(url,headers=headers,data=data,cookies=cookies,verify=False)
    if response.status_code == 200:
        #time to process it and get the IP addresses and other stuffs
        currentConnectedUserList = getCurrentConnectedIPs(response,currentConnectedUserList)
        #time to save them
        if logData:
            saveCurrentUserList(json.dumps(currentConnectedUserList))
    return currentConnectedUserList

def getCurrentStaticIPConnections(router, logData=True):
    cookies = router.cookies
    headers = getHeaders("http://192.168.0.1/lan.htm")
    url = getUrl('getStaticIPUsersConnectionList')
    response = requests.get(url,headers=headers,cookies=cookies,verify=False)
    #time to process it
    currentStaticIPConnectionList = getCurrentStaticIPs(response)
    #lets log them
    if logData:
        saveStaticIPUserList(currentStaticIPConnectionList)
    return currentStaticIPConnectionList

def getSubmitValue(router, action):
    cookies = router.cookies 
    headers = getHeaders()
    if action == "getValueForStaticIP":
        url = getUrl(action)
        response = requests.get(url,headers=headers,cookies=cookies)
        value = getSubmitValueForAddUserAndDeleteUser(response)
        return value
    
    elif action == "getValueForTrafficControl":
        url = getUrl(action)
        response = requests.get(url,headers=headers,cookies=cookies)
        value = getSubmitValueForUserTrafficControlAddAndDelete(response)
        return value


def addStaticIPUser(router,ip,mac,logData=True):
    cookies = router.cookies
    headers = getHeaders("http://192.168.0.1/lan.htm")
    submit_value = getSubmitValue(router,"getValueForStaticIP")
    data = getData('addStaticIPUser')

    #lets prepare Data
    data['ipaddr'] = ip
    data['macaddr'] = process_mac(mac)
    data['submit.htm?lan.htm'] = submit_value
    
    url = getUrl('addStaticIPUser')
    
    response = requests.post(url,headers=headers,cookies=cookies,data=data,verify=False)
    if response.status_code == 200:
        if response.text.find(mac.upper()) > -1:
            #lets log it 
            if logData:
                data = getCurrentStaticIPs(response)
                saveStaticIPUserList(data)
            return "[+] IP added successfully"
    return f"[!] Not able to add {ip}"
    

def deleteStaticIPUser(select,ip,mac,router,logData=True):
    cookies = router.cookies
    headers = getHeaders("http://192.168.0.1/lan.htm")
    submit_value = getSubmitValue(router,"getValueForStaticIP")
    data = getData('deleteStaticIPUser')

    #lets prepare Data
    data['select'] = select 
    data['ipaddr'] = ip
    data['macaddr'] = process_mac(mac)
    data['submit.htm?lan.htm'] = submit_value
    
    url = getUrl('deleteStaticIPUser')
    
    response = requests.post(url,headers=headers,cookies=cookies,data=data,verify=False)
    if response.status_code == 200:
        if response.text.find(mac.upper()) == -1:
            #lets log it 
            if logData:
                data = getCurrentStaticIPs(response)
                saveStaticIPUserList(data)
            return "[+] IP deleted successfully"
    return f"[!] Not able to delete {ip}"


def getTrafficControlledConnections(router, logData=True):
    trafficControlledConnectionList = []
    cookies = router.cookies 
    headers = getHeaders("http://192.168.0.1/ipqostc_gen_ap.htm")
    url = getUrl('getTrafficControlledConnections')
    #lets make the call to router 
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)
    trafficControlledConnectionList = getCurrentTrafficControlledIPs(response)
    
    if logData:
        saveTrafficControlledUserList(trafficControlledConnectionList)
    
    return trafficControlledConnectionList 



def addTrafficControlledUser(router,ip,up_rate_floor=10,up_rate_ceiling=100,down_rate_floor=10,down_rate_ceiling=100,logData=True):
    cookies = router.cookies 
    url = getUrl("addUserToTrafficControl")
    headers = getHeaders("http://192.168.0.1/lan.htm")
    # #first whether it is added to static ip list if not add it
    submit_value = getSubmitValue(router,"getValueForTrafficControl")
    data = getData("addUserToTrafficControl")
    data['srcip'] = ip 
    data['uprateFloor'] = up_rate_floor
    data['downrateFloor'] = down_rate_floor
    data['uprateCeiling'] = up_rate_ceiling
    data['downrateCeiling'] = down_rate_ceiling
    data['submit.htm?ipqostc_gen_ap.htm'] = submit_value

    #time to add it
    response = requests.post(url,headers=headers,cookies=cookies,data=data,verify=False)
    if response.status_code == 200:
        if logData:
            data = getCurrentTrafficControlledIPs(response)
            saveTrafficControlledUserList(data)

        if response.text.find(ip)> -1:
            return f"[+] IP {ip} Speed Controlled successfully"

    return f"[!] Unsuccessful to limit IP {ip}"



def deleteTrafficControlledUser(router,remove_q,logData=True):
    cookies = router.cookies
    headers = getHeaders("http://192.168.0.1/ipqostc_gen_ap.htm")
    url = getUrl("deleteTrafficControlledIP")
    submit_value = getSubmitValue(router,"getValueForTrafficControl")
    data = getData("deleteTrafficControlledIP")
    data['removeQ'] = remove_q 
    data['removeRuleList'] = f"{remove_q},"
    data['submit.htm?ipqostc_gen_ap.htm'] = submit_value
    response = requests.post(url,headers=headers,cookies=cookies,data=data,verify=False)
    if response.status_code == 200:
        if logData:
            data = getCurrentTrafficControlledIPs(response)
            saveTrafficControlledUserList(data)
        return f"[+] Successfully removed"
    return "[!] Not able to remove."




    









