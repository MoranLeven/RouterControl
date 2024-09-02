from constants import *
from bs4 import BeautifulSoup as bs
def getSessionID(response):
    if response.status_code == 200:
        sessionData = response.cookies._cookies.get(ROUTER_IP).get('/').get('SessionID')
        return {sessionData.name:sessionData.value}
    else:
        return {}

def getCurrentConnectedIPs(response,currentConnectedUserList):
    if response.status_code == 200:
        soup = bs(response.content,features="html.parser")
        #lets get the stuff and save them in dictionary
        connection_table = soup.select(".formlisting tr")
        for connection in connection_table:
            if connection.attrs.get('class',None) == None:
                conn_data = connection.text.split()
                data= {"username":conn_data[0],"IP_Address":conn_data[1],"MAC_Address":conn_data[2]}
                currentConnectedUserList.append(data)
        return currentConnectedUserList
    
def getSubmitValueForAddUserAndDeleteUser(response):
    soup = bs(response.content,features='html.parser')
    data = soup.select('form[name="dhcpip"] input[name="submit.htm?lan.htm"]')[0]
    return int(data.attrs.get('value'))


def getSubmitValueForUserTrafficControlAddAndDelete(response):
    soup = bs(response.content,features='html.parser')
    data = soup.select('form[name="qostcrule"] input[name="submit.htm?ipqostc_gen_ap.htm"]')[0]
    return int(data.attrs.get('value'))

#DHCP IP Operations processing 
def getCurrentStaticIPs(response):
    static_ip_list = []
    soup = bs(response.content,features="html.parser")
    static_ip_table = soup.select("table.formlisting tr:not(.form_label_row)")
    for conn in static_ip_table:
        #get the select value for static IP
        value = conn.select_one('input[name="select"]').attrs.get("value")
        conn_data = conn.text.split()
        data = {"Select_Value":value,"IP_Address":conn_data[0],"MAC_Address":conn_data[1]}
        static_ip_list.append(data)
    return static_ip_list

def getCurrentTrafficControlledIPs(response):
    traffic_controlled_ips = []
    soup = bs(response.content, features="html.parser")
    traffic_controlled_ip_table = soup.select("table#qosTable tr")[2:]
    for controlled_conn in traffic_controlled_ip_table:
        remove_q = controlled_conn.select_one("input[name='removeQ']").attrs.get("value")
        conn_data = controlled_conn.text.split()
        data = {"removeQ":remove_q,"IP_Address":conn_data[1],"UP_Floor":conn_data[2],"DOWN_Floor":conn_data[3],
                "UP_Ceiling":conn_data[4],"DOWN_Ceiling":conn_data[5]}
        traffic_controlled_ips.append(data) 
    return traffic_controlled_ips
