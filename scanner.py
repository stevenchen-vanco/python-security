import nmap

portscan = nmap.PortScanner()

target=input("Enter the IP to scan: ")
target_port=input("Enter the port range: ")

if not target:
    target='127.0.0.1'

if not target_port:
    target_port='1-1024'

print("Initializing Scan Against {}".format(target))
portscan.scan(hosts='{}'.format(target), arguments='-p {}'.format(target_port))

for host in portscan.all_hosts():
     print('\nHost : {}'.format(host))
     print('Status : {}\n'.format(portscan[host].state()))


     for x in portscan[host].all_protocols():
         print("Port Type: {}".format(x))
         port_num = portscan[host][x].keys()

         for num in port_num:
             print("Port: {}\tStatus: {}".format(num,portscan[host][x][num]['state']))

     


