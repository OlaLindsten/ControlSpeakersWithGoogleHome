from flask import Flask, request
import remoteHandler
import serial
app = Flask(__name__)

#Url for send button
@app.route('/send-button')
def sendButton():
	ser = serial.Serial('/dev/ttyACM0', 9600)		#Port for serial connection to arduino via usb
	b = str(request.data)
	c = b.split("'")

	if(c[1] == "2424"):								#Simple body check

		button = request.args.get('button')			#Get button name
		amount = request.args.get('amount')			#Get amount

		amount = convert(amount)

		if (amount == None):						#If no amount is specified default 1
			amount = 1

		amount = int(amount)						#Convert to int so we can loop it
		remoteHandler.sendButton(button, amount)
		button = reformatButton(button)				
		ser.write(str.encode(button))				#Write to Arduino
		print(button)
	return "OK"

#Remove button
@app.route('/remove-button')
def removeButton():
	b = str(request.data)
	c = b.split("'")

	if(c[1] == "2424"):

		button = request.args.get('button')
		remoteHandler.removeButton(button)

	return "OK"

#Initiate json
@app.route('/initiate')
def initiate():
	remoteHandler.initiate()
	return "OK"

#Google home sometimes six instead off 6 so a simple if statement for three common sets
def convert(amount):
	if(amount == " for"):
		amount = 4
	elif(amount == " six"):
		amount = 6
	elif(amount == " five"):
		amount = 5
	return amount

#Converts what should be outputed on LCD
def reformatButton(button):

	if(button == "volume_up_speaker"):
		button = "volume up"
	elif(button == "volume_down_speaker"):
		button = "volume down"
	elif(button == "mute_speaker"):
		button = "speakers muted / unmuted"
	elif(button == "on_off_speaker"):
		button = "on or off speakers"
	return button

if __name__ == '__main__':
	app.run(debug=True, host='192.168.1.91', port=5000)
