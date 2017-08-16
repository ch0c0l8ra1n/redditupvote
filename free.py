import requests
import requests.auth
import re
import time
import random

def vote(thing):
    payload={
    'id':thing,
    'dir':1,
    'rank':4
    }
    t=requests.post("https://oauth.reddit.com/api/vote",data=payload,headers=headers)
    print(t)



i=1

session = requests.Session()
client_auth=requests.auth.HTTPBasicAuth(client_id, client_secret)
post_data = {"grant_type": "password", "username": username, "password": password}
usagent="rjpj's web interface for reddit"
headers = {"User-Agent":usagent}
session.headers.update(headers)
response = session.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
parsed=response.json()
token = parsed['access_token']

before_l=""
before_c=""

mentionlist=[]
i=1
while True:
    try:
        headers = {"Authorization": "bearer "+token, "User-Agent":usagent}
        
        url="https://oauth.reddit.com/r/FreeKarma4U/new/.json?limit=25&before=t3_"+before_l
        response = requests.get(url, headers=headers,timeout=5)
        parsed=response.json()
        if(not parsed["data"]["children"]):
            time.sleep(random.randint(300,600))
            continue
        before_l = parsed["data"]["children"][0]["data"]["id"]
        
        
        for item in parsed["data"]["children"]:
            print(item["data"]["title"])
            mentionlist.append(item["data"]["id"])
            vote(item["data"]["name"])
            time.sleep(random.randint(60,120))
            i+=1

        time.sleep(random.randint(300,600))
        url="https://oauth.reddit.com/r/FreeKarma4U/comments/.json?limit=25&before=t1_"+before_c
        response = requests.get(url, headers=headers,timeout=5)
        parsed=response.json()
        if(not parsed["data"]["children"]):
            time.sleep(random.randint(300,600))
            continue

before_c = parsed["data"]["children"][0]["data"]["id"]
    
    
    for item in parsed["data"]["children"]:
        print(item["data"]["body"])
            mentionlist.append(item["data"]["id"])
            vote(item["data"]["name"])
            time.sleep(random.randint(60,120))
            i+=1
        time.sleep(random.randint(300,600))
    except Exception as e:
        print(e)
        time.sleep(10)
        client_auth=requests.auth.HTTPBasicAuth('XmWowKH0kG8zRg', '_2xiEQ51Dw9APs-aEF5oqmJ6Y3Q')
        post_data = {"grant_type": "password", "username": "watguy12_bot", "password": "watguy13_bot"}
        usagent="rjdjdasd the pj"
        headers = {"User-Agent":usagent}
        session.headers.update(headers)
        response = session.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
        parsed=response.json()
        token = parsed['access_token']
        
        before_l=""
        before_c=""
