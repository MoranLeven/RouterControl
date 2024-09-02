# import requests 
from bs4 import BeautifulSoup as bs

# def login():
#     cookies = {
#         'SessionID': '',
#     }

#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         # 'Cookie': 'SessionID=',
#         'Origin': 'http://192.168.0.1',
#         'Referer': 'http://192.168.0.1/login.htm',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     }
#     data = {
#         'username': 'Admin',
#         'password': 'd41d8cd98f00b204e9800998ecf8427e',
#         'submit.htm?login.htm': 'Login',
#     }

#     response = requests.post('http://192.168.0.1/login.cgi', cookies=cookies, headers=headers, data=data, verify=False)
#     sessionData = response.cookies._cookies.get('192.168.0.1').get('/').get('SessionID')
#     return {sessionData.name:sessionData.value}


# def getAddValue():

#     cookies = {'SessionID':'48'}
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Connection': 'keep-alive',
#         # 'Cookie': 'SessionID=22',
#         'Referer': 'http://192.168.0.1/lan.htm',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     }

#     response = requests.get('http://192.168.0.1/lan.htm', cookies=cookies, headers=headers, verify=False)
#     soup = bs(response.content,features='html.parser')
#     #lets get the input 
#     input = soup.select("form[name='dhcpip'] input[name='submit.htm?lan.htm']")[0]
#     return int(input.attrs.get('value'))



import requests

cookies = {
    'SessionID': '37',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'SessionID=37',
    # 'Referer': 'http://192.168.0.1/ipqostc_gen_ap.htm',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

response = requests.get('http://192.168.0.1/ipqostc_gen_ap.htm', cookies=cookies, headers=headers, verify=False)
soup = bs(response.content,features='html.parser')
# connectionTable = soup.select(".formlisting tr")
# #time to get the data
# connection_data = []
# for connection in connectionTable:
#     if connection.attrs.get('class',None) == None:
#         conn_data = connection.text.split()
#         data= {"username":conn_data[0],"IP_Address":conn_data[1],"MAC_Address":conn_data[2]}
#         connection_data.append(data)

# for i in connection_data:
#     print(i)
# soup = bs(response.content,features="html.parser")
# for i in getCurrentStaticIPs(response):
#     print(i)

