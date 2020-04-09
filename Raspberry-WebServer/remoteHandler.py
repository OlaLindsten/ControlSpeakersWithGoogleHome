from ircodec.command import CommandSet
import time

#Run once to initiate the json file
def initiate():
    controller = CommandSet(name="IrInit", emitter_gpio=6,receiver_gpio=16, description="Send ir signal")       #Specifies GPIO
    controller.save_as("ir.json")                                                                               #Save

#Transmit the Ir signal
def sendButton(button, amount):
    controller = CommandSet.load("ir.json")
    print(amount)
    for i in range(amount):
        controller.emit(button)             #Send button
        time.sleep(.1)                      #time is written in seconds, need delay otherwise speakers will not get every transmit
    return

#Remove a button
def removeButton(button):
    controller = CommandSet.load("ir.json")
    controller.remove(button)               #Remove button
    controller.save_as("ir.json")
