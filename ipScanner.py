import os
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-o","--op_sys",required=True,help="operating system (w for Windows || l for linux)")
ap.add_argument("-f","--from",required=True,help="ip range to look from")
ap.add_argument("-t","--to",required=True,help="ip range to look to")
args=vars(ap.parse_args())
op_sys=args["op_sys"]
ip=args["from"]

print('Scanning ips from {} - {}\nOs is {}'.format(args["from"],args["to"],args["op_sys"]))
def Windows():
    lim=int(args["from"].split('.')[3])
    while lim<=int(args["to"]):
    ##    print('ping -n 1 -w 10 {}.{}.{}.{}'.format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim))
        o=os.popen('ping -n 1 -w 10 {}.{}.{}.{}'.format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim)).read()
        if o.split(' ')[9].split('=')[0]=='bytes':
            print("\n****************************************\n***** ip {}.{}.{}.{} got a match *****\n****************************************\n".format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim))
            pass
        else:
            print("ip {}.{}.{}.{} didn't get any match".format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim))
            pass
    ##
        lim+=1
def Linux():
    lim=int(args["from"].split('.')[3])
    while lim<=int(args["to"]):
    ##    print('ping -n 1 -w 10 {}.{}.{}.{}'.format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim))
        o=os.popen('ping -c 1 -W 10 {}.{}.{}.{}'.format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim)).read()
        if o.split(' ')[11].split('=')[0]=='ttl':
            print("\n****************************************\n***** ip {}.{}.{}.{} got a match *****\n****************************************\n".format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim))
            pass
        else:
            print("ip {}.{}.{}.{} didn't get any match".format(args["from"].split('.')[0],args["from"].split('.')[1],args["from"].split('.')[2],lim))
            pass
    ##
        lim+=1

if op_sys=='w':
    Windows()
elif op_sys=='l':
    Linux()
