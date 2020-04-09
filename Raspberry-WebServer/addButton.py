from ircodec.command import CommandSet
import sys

#Add the button by adding the name when starting the program
button = sys.argv[1]
print(button)
controller = CommandSet.load("ir.json")
controller.add(button)
controller.save_as("ir.json")
