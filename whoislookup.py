import sys,time
import whois

host=input("Enter host: ")
if not host:
    sys.exit("Ding Ding Ding...................Enter a host to lookup")

try:
    time.sleep(2)
    print("++++++++++++++++++++++++++++++++++++++  Whois LookUp  ++++++++++++++++++++++++++++++++++++++")
    print(whois.whois(host).text)

except:
    sys.exit("Ping Ping Ping.......................... Enter a valid host")