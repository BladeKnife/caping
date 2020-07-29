import os,sys,time,requests,re,json,random
from time import sleep
from requests import post
os.system("clear")
print ("""
\033[1;97m        BOT CAPING
       \033[90m __________
\033[1;97mcreator: \033[1;96mfahmiapz
\033[1;97myoutube: \033[1;96mApmzchannel
\033[1;97mgithub : \033[4;92mgithub.com/BangDanz\033[00m
\033[90m_____________________________""")
ff=input("\033[1;97m[\033[1;96m•\033[1;97m]UserAgent: \033[1;92m")
xx=input("\033[1;97m[\033[1;96m•\033[1;97m]Cookie: \033[1;92m")
oo=input("\033[1;97m[\033[1;96m•\033[1;97m]Authorization: \033[1;92m")
pp=input("\033[1;97m[\033[1;96m•\033[1;97m]Ts:\033[1;92m")
ss=input("\033[1;97m[\033[1;96m•\033[1;97m]Index: \033[1;97m")
def login():
    print ("\033[1;97m[\033[1;93m•\033[1;97m]Sedang Login..")
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": ff,
    "cookie": xx,
    "market": "googleplay",
    "appid": "1",
    "content-type": "application/json",
    "accept-encoding": "gzip"
    }
    data={"city":"Jakarta"}
    a=json.dumps(data)
    r = requests.post("https://ai2.caping.co.id/v2/user/login/visitor", data=a, headers=bb)
    h=json.loads(r.text)
    if "OK" in r.text:
        print ("\033[1;97m[\033[1;92m+\033[1;97m]Login Success...\n\033[1;97m[\033[1;92m+\033[1;97m]Yourname:\033[1;92m",h["data"]["user_name"])
    else:
        print ("Login Failed")
    d=requests.get("https://ai2.caping.co.id/v2/user/ccsp/detail", headers=bb)
    g=json.loads(d.text)
    if "OK" in d.text:
        print ("\033[1;97m[\033[1;92m+\033[1;97m]YourId:\033[1,92m",g["data"]["uid"],"\n\033[1;97m[\033[1;92m+\033[1;97m]Yourcoin:\033[1;92m",g["data"]["total_coin"],"\n\033[1;97m[\033[1;92m\033[1;97m]YourMoney:\033[1;92m",g["data"]["total_money"])
    else:
        sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]Login Failed\033[1;91m!")
def daili():
    login()
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": ff,
    "cookie": xx,
    "market": "googleplay",
    "appid": "1",
    "authorization": oo,
    "ts": pp,
    "index": ss,
    "content-type": "application/json",
    "accept-encoding": "gzip"
    }
    for i in range(0,50):
        pg=random.randrange(1,6)
        d=json.dumps({"articleType":1,"page":pg})
        j=requests.post("https://ai2.caping.co.id/v2/news/getNewsList2", data=d, headers=bb).text
        hh=json.loads(j)
        for x in hh["data"]["list"]:
            su=x['ArticleType']
            k=x["NewsId"]
        dat=json.dumps({"reports":[{"action":"browse_news","list":[{"articleType":su,"newsId":k,"status":1,"times":4,"totalms":40},{"articleType":su,"newsId":k,"status":1,"times":3,"totalms":33},{"articleType":su,"newsId":k,"status":1,"times":2,"totalms":31}]}]})
        time.sleep(2)
        r=requests.post("https://ai2.caping.co.id/v2/event/report",data=dat, headers=bb)
        js1=json.loads(r.text)
        if js1["data"] == 0:
           print ("\033[1;97m[\033[1;91m!\033[1;97m]Failed Claim\033[1,91m!")
        else:
           print ("\033[1;97m[\033[1;92m+\033[1;97m]Success Claim:+\033[1;92m20")
daili()
