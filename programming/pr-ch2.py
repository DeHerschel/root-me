#! /usr/bin/env python
#-*-coding:utf-8-*-

import socket
import time
import base64
HOST = "irc.root-me.org"
PORT = 6667
NICK = "fast"
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
while 1:
	buffer = irc.recv(1024)
	print(buffer)
	if buffer.find('PING') != -1:
		irc.send('PONG ' + buffer.split()[1] + '\r\n')
		irc.send("PRIVMSG " + "Candy" + " :!ep2 \r\n")
	if buffer.find('PRIVMSG fast') != -1:
		coded = buffer.split()[3].split(":")[1]
		decoded = coded.decode('ascii');
		base64_bytes = coded.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		message = message_bytes.decode('ascii')
	 	irc.send("PRIVMSG " + "Candy" + " :!ep2 -rep " + message + "\r\n")
	 	print(irc.recv(1024))
	 	break
