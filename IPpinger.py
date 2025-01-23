import requests
import os
import json

x = requests.get('https://api.myip.com').json()

actualIp = x['ip']
print(actualIp)

ZONE_ID = "1712619de68310bd0cce6de304d89230"
readDnsRecord = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"

headersRead = {
    "Authorization": "Bearer f7dRbu-u_1OFdCDGzOD-Wk7hx6oeNQmOx_quCXy1",
    "Accept": "application/json"
    }

z = requests.get(readDnsRecord, headers=headersRead).json()

dnsIP = (z["result"][0]['content'])
#if actualIp == dnsIP:
#rewriteIP = open("IP.csv", "w+")
#rewriteIP.write(actualIp)
#rewriteIP.seek(0)
#print(rewriteIP.read())

DNS_RECORD_ID1 ="5958d2296df999229491a1e495a93516"
DNS_RECORD_ID2 ="1743e62b527cef0cc79f8662c2a86dd0"
DNS_RECORD_ID3 ="1c90254a64c3c378ea0a8618c23dcf36"

patchDnsRecord1 = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID1}"
patchDnsRecord2 = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID2}"
patchDnsRecord3 = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID3}"

headersPatch= {
    "Authorization": "Bearer fqgNK0xMUIZnfvsjdn2ilSfSxO2Yq_72bl8A8mvn",
    "Accept": "application/json"

}
data1 = {
    'content': f'{actualIp}',
    'name': '*.tobilab.org',
    "proxied": True,
    "type": "A",
    "comment": "",
    "tags": [],
    "ttl": 1    
}
data2 = {
    'content': f'{actualIp}',
    'name': 'tobilab.org',
    "proxied": True,
    "type": "A",
    "comment": "",
    "tags": [],
    "ttl": 1    
}
data3 = {
    'content': f'{actualIp}',
    'name': 'www.tobilab.org',
    "proxied": True,
    "type": "A",
    "comment": "",
    "tags": [],
    "ttl": 1    
}

y1 = requests.patch(patchDnsRecord1, headers=headersPatch,json=data1).json()
y2 = requests.patch(patchDnsRecord2, headers=headersPatch,json=data2).json()
y3 = requests.patch(patchDnsRecord3, headers=headersPatch,json=data3).json()

#if actualIp == dnsIP:
#    print("dns is still correct")
#else:
print(y1,y2,y3)

