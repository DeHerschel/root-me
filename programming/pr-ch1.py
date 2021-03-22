#! /usr/bin/env python
#-*-coding:utf-8-*-

import socket
import math
import time
HOST = "irc.root-me.org";
PORT = 6667;
NICK = "fast";
CHAN = "#root-me_challenge";
PASSWD = "passwd";
buffer = "";
irc = socket.socket();
result = irc.connect((HOST, PORT));
irc.send("PASS %s\n" % (PASSWD));
irc.send("USER " + NICK + " " + NICK + " " + NICK + " :fast\n");
irc.send("NICK " + NICK + "\n");
irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (NICK, PASSWD));
time.sleep(3);
irc.send("JOIN " + CHAN + "\n");
while 1:
	buffer = irc.recv(1024);
	print(buffer);
	if buffer.find('PING') != -1: 
		irc.send('PONG ' + buffer.split() [1] + '\r\n');
		irc.send("PRIVMSG " + "Candy" + " :!ep1 \r\n");
	if buffer.find('PRIVMSG fast') != -1:
		n1 = buffer.split()[3].split(":")[1]
		n2 = buffer.split()[5]
		sqr = math.sqrt(float(n1))
		res = round((sqr * int(n2)), 2)
		irc.send("PRIVMSG " + "Candy" + " :!ep1 -rep " + str(res) + "\r\n")
		print(irc.recv(1024))
		break

