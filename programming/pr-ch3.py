#! /usr/bin/env python
#-*-coding:utf-8-*-

import socket
import time
HOST = "irc.root-me.org"
PORT = 6667
NICK = "fastbot"
CHAN = "#root-me_challenge"
PASSWD = "passwd"
buffer = ""
irc = socket.socket()
result = irc.connect((HOST, PORT))
irc.send("PASS %s\n" % (PASSWD))
irc.send("USER " + NICK + " " + NICK + " " + NICK + " :fast\n")
irc.send("NICK " + NICK + "\n")
irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (NICK, PASSWD))
time.sleep(3)
irc.send("JOIN " + CHAN + "\n")
decoded = "";
while 1:
	buffer = irc.recv(1024)
	print(buffer)
	if buffer.find('PING') != -1:
		irc.send('PONG ' + buffer.split()[1] + '\r\n')
		irc.send("PRIVMSG " + "Candy" + " :!ep3 \r\n")
	if buffer.find('PRIVMSG fast') != -1:
		coded = buffer.split()[3].split(":")[1]
		print(coded)
		coded = list(coded)
		letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		for letter in coded:
			if letter.isupper():
				index = letters.index(letter.lower())
				if index < 13:			
					decodeletter = letters[index+13];
					decoded = decoded + decodeletter.upper();
				else: 
					decodeletter = letters[index-13];
					decoded = decoded + decodeletter.upper();
			elif letter.islower():
				index = letters.index(letter)
				if index < 13:			
					decodeletter = letters[index+13];
					decoded = decoded + decodeletter
				else: 
					decodeletter = letters[index-13];
					decoded = decoded + decodeletter
			else:
				decoded = decoded + letter
		print(decoded);
	 	irc.send("PRIVMSG " + "Candy" + " :!ep3 -rep " + decoded + "\r\n")
	 	print(irc.recv(1024))
	 	break
