import aiml
import os

kernel = aiml.Kernel()

kernel.learn('startup.xml')
kernel.respond("load aiml b")

while True:
    print kernel.respond(raw_input("Enter your message >> "))
