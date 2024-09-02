from router import Router 
from operations import * 
from constants import IGNORE_MAC

def removeAll(router):
    if router.is_loggedIn:
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

router = Router()
router.login()
removeAll(router)

