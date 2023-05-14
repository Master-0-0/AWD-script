import os

ip_list = []

for i in range(0,255):
    ip = "192.168.1."+str(i)
    #ip = "192-168-1-{0}.pvp2169.bugku.cn".format(str(i))
    #print(ip)
    shell = "ping {0} -n 1".format(ip.rstrip())
  
    body = os.popen(shell,'r',1)    
    if "TTL=" in body.read():
        print("+++++++++++【目标存活】++++++++++++++++")
        print("ip: "+ip)        
        ip_list.append(ip)
        body.close()
    else:
        print("ip: "+ip.rstrip()+" 无法连接")
        body.close()
print(ip_list)        