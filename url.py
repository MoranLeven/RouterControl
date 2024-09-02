from constants import REQUIRED
data = {
    "login":{
            'username': 'Admin',
            'password': 'd41d8cd98f00b204e9800998ecf8427e',
            'submit.htm?login.htm': 'Login'
    },
    "addStaticIPUser":{
        'lan_dhcpRangeStart': '192.168.0.2',
        'lan_dhcpRangeEnd': '192.168.0.254',
        'ipaddr': REQUIRED,
        'macaddr': REQUIRED,
        'submit.htm?lan.htm': REQUIRED
    },
    "deleteStaticIPUser":{
        'lan_dhcpRangeStart': '192.168.0.2',
        'lan_dhcpRangeEnd': '192.168.0.254',
        'ipaddr': REQUIRED,
        'macaddr': REQUIRED,
        'delete': 'Delete Selected',
        'select': REQUIRED,
        'submit.htm?lan.htm': REQUIRED

    },
    "addUserToTrafficControl":{
        'removeRuleList': '',
        'proto': '0',
        'srcip': REQUIRED,
        'srcnetmask': '',
        'dstip': '',
        'dstnetmask': '',
        'uprateFloor': REQUIRED,
        'uprateCeiling': REQUIRED,
        'downrateFloor': REQUIRED,
        'downrateCeiling': REQUIRED,
        'addRule': 'Add',
        'submit.htm?ipqostc_gen_ap.htm': REQUIRED
    },
    "deleteTrafficControlledIP":{
        'removeQ': REQUIRED,
        'removeRuleList': REQUIRED,
        'save': 'Delete',
        'proto': '0',
        'srcip': '',
        'srcnetmask': '',
        'dstip': '',
        'dstnetmask': '',
        'sport': '',
        'dport': '',
        'uprateFloor': '',
        'uprateCeiling': '',
        'downrateFloor': '',
        'downrateCeiling': '',
        'submit.htm?ipqostc_gen_ap.htm': REQUIRED,
    }
}

url = {
    "login":"http://192.168.0.1/login.cgi",
    "getActiveConnections":"http://192.168.0.1/dhcptbl.htm",
    "getValueForStaticIP":"http://192.168.0.1/lan.htm",
    "getStaticIPUsersConnectionList":"http://192.168.0.1/lan.htm",
    "addStaticIPUser":"http://192.168.0.1/form2Dhcpip.cgi",
    "deleteStaticIPUser":"http://192.168.0.1/form2Dhcpip.cgi",
    "getTrafficControlledConnections":"http://192.168.0.1/ipqostc_gen_ap.htm",
    "getValueForTrafficControl":"http://192.168.0.1/ipqostc_gen_ap.htm",
    "addUserToTrafficControl":"http://192.168.0.1/form2IPQoSTc.cgi",
    "deleteTrafficControlledIP":"http://192.168.0.1/form2IPQoSTc.cgi"
}

def getData(action):
    return data.get(action,None)

def getUrl(action):
    return url.get(action,None)

def getHeaders(referer=None):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://192.168.0.1',
            'Referer': 'http://192.168.0.1/login.htm' if referer == None else referer,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }
        return headers

