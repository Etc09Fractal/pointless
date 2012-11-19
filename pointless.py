#POINTLESS BUTTON#
#COPYRIGHT 2012#
#DONOVAN ROUDABUSH#



#Imports#
import random
from Tkinter import *

#Functions#
def start():
	text = random.randint(1,13)
	if text == 1:
		label1text.set("Hi.")
	elif text == 2:
		label1text.set("Hola. Si, yo hablo en Espanol.")
	elif text == 3:
		label1text.set("Why did you click me?")
	elif text == 4:
		label1text.set("That was pointless.")
	elif text == 5:
		label1text.set("No Comment")
	elif text == 6:
		label1text.set("Wat up?")
	elif text == 7:
		label1text.set("I'm pumped.")
	elif text == 8:
		label1text.set("Can not compute.")
	elif text == 9:
		label1text.set("WARNING: Pointless.")
	elif text == 10:
		label1text.set("Bonjour, comment t'appelle tu? Est-ce que tu veux aller chez moi?")
	elif text == 11:
		label1text.set("Washington DC.")
	elif text == 12:
		label1text.set("Your computer have been infected by pointless.")
	elif text == 13:
		label1text.set("Dat Pointless.")
#GUI#
app = Tk()
app.title("Pointless Button")
app.geometry("450x300+200+200")
label1text = StringVar()
label1text.set("Pointless Button")
label1=Label(app, textvariable = label1text)
label1.pack(side='top')
button1=Button(app, text="Click Here", height=4, command = start)
button1.pack(side='bottom')
app.mainloop()
