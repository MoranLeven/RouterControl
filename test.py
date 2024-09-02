from router import Router 
from operations import * 
from constants import IGNORE_MAC
from utils import *



def removeAll(router):
    if router.is_loggedIn:
        currentConnections = getCurrentConnections(router)
        staticIPs = getCurrentStaticIPConnections(router)
        trafficControlledIPs = getTrafficControlledConnections(router)

        #remove all staticIPs
        for conn in staticIPs:
            print(conn)
            ip = conn["IP_Address"]
            mac = conn["MAC_Address"]
            select = conn["Select_Value"]
            status = deleteStaticIPUser(select,ip,mac,router)
            print(status,"\n") 

        #remove all trafficControlledIPs
        for conn in trafficControlledIPs:
            print(conn)
            removeQ = conn['removeQ']
            status = deleteTrafficControlledUser(router,removeQ)
            print(status,end="\n")

def controlAll(router):
    if router.is_loggedIn:
        currentConnections = getCurrentConnections(router)
        staticIPs = getCurrentStaticIPConnections(router)
        trafficControlledIPs = getTrafficControlledConnections(router)
        #lets make them static
        for conn in currentConnections:
            print(conn)
            ip = conn["IP_Address"]
            mac = conn["MAC_Address"]
            if mac.lower() not in get_mac_list(staticIPs):
                status = addStaticIPUser(router,ip,mac)
                print(status,end="\n") 
            else:
                print("IP already static")
        
        staticIPs = getCurrentStaticIPConnections(router)
        for conn in staticIPs:
            print(conn)
            ip = conn['IP_Address']
            mac = conn["MAC_Address"]
            if mac.lower() in IGNORE_MAC:
                print(f"{mac}<-> {ip} it is a part of protected list.",end="\n\n")  # type: ignore
            elif ( ip in get_ip_list(trafficControlledIPs) ):
                print(f"IP {ip} is already controlled.")
            else:
                status = addTrafficControlledUser(router,ip,up_rate_ceiling=50, down_rate_ceiling=100, up_rate_floor=10,down_rate_floor=10)
                print(status,end="\n\n")


router = Router()
router.login()
# removeAll(router)
controlAll(router)
