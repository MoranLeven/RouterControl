def process_mac(mac):
    if mac.find(":")>-1:
        mac = mac.replace(":","")
    return mac 

def get_mac(ip):
    pass

def get_traffic_controlled_user_data(ip):
    pass

def get_mac_list(data):
    return list(map(lambda x: x["MAC_Address"].lower(),data))

def get_ip_list(data):
    return list(map(lambda x:x['IP_Address'][:-3],data))