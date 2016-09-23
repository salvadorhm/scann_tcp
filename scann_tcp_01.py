#!/usr/bin/env python
from socket import * 
from socket import gethostname
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

if __name__ == '__main__':
    remoteServer = raw_input('Enter host to scan: ')
    minport = input("First port: ")
    maxport = input("Last port: ")

    #remoteServer = '192.168.100.69'
    minport = 0
    maxport = 65535
    
    remoteServerIP = gethostbyname(remoteServer)
    # Print a Banner
    print "-" * 60
    print '# PortScanner Report'
    print "### Please wait, scanning remote host", remoteServerIP
    print '### Host name ', gethostname()
    
    
    # Check what time the scan started
    t1 = datetime.now()
    print "### Init time {}".format(t1)
    print "-" * 60

    #scan reserved ports
    try:
        print 'PORT\tSTATE\n'
        for portTCP in range(minport, maxport):
            sockTCP = socket(AF_INET, SOCK_STREAM)
            sockTCP.settimeout(0.05)
            result = sockTCP.connect_ex((remoteServerIP, portTCP))
            if(result == 0) :
                print ("* {:d}/tcp\topen".format(portTCP))
            sockTCP.close()
    except KeyboardInterrupt:
        print "### You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print '### Hostname could not be resolved. Exiting'
        sys.exit()

    except (socke.timeout, socket.error):
        print "### Couldn't connect to server ", error
        sys.exit()

    t2 = datetime.now()
    print "-" * 60
    totaltime = t2 - t1

    print ('### End time: {}'.format(t2))
    print ('### Scanning Completed in: {}'.format(totaltime))