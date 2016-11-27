import aiml
import os
import fbchat
from time import sleep

print 'Enter your username'
username=raw_input()
print ' Enter the password'
password=raw_input()
print 'With which friend u want to check the chatbox?'
fname=raw_input()

client = fbchat.Client(username,password)
friends = client.getUsers(fname)
friend = friends[0]


# Create the kernel and learn AIML files
kernel = aiml.Kernel()
#kernel.learn("std-startup.xml")
#'startup.xml file consist of all the information about AIML files
#aiml file consist information about  input and responce.
kernel.learn('startup.xml')
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
prev_message=[]
messages=client.getThreadInfo(friend.uid,0)
for message in messages:
	prev_message.append(message.body)
while True:
	sleep(3)
	messages=client.getThreadInfo(friend.uid,0)
	recent_message=messages[0]
	if recent_message.body not in prev_message:
		print prev_message
		prev_message.append(recent_message.body)
		client.send(friend.uid,kernel.respond(recent_message.body))

	sleep(2)
