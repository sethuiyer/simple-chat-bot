import aiml
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("question",help="Go ahead with your question!")
args = parser.parse_args()
kernel = aiml.Kernel()
kernel.verbose(False)
kernel.setBotPredicate("name", "Rebecca")
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "startup.xml", commands = "'LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
print kernel.respond(args.question)
kernel.saveBrain("bot_brain.brn")