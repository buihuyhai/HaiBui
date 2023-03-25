import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)

def speak(audio):
	print('F.R.I.D.A.Y.:'+ audio)
	friday.say(audio)
	friday.runAndWait()
def time():
	Time= datetime.datetime.datetime.now.strftime("%I:%M:%p")
	speak(time)
def welcome():
	hour=datetime.datetime.now().hour
	if hour >=6 and hour<12:
		speak("Good Morning sir")
	elif hour >=12 and hour <18:
		speak("Good Afternoon sir")
	elif hour >= 18 and hour<24:
		speak("Good Night sir")
	speak("How can i help you")
def command():
	c=sr.Recognizer()
	with sr.Microphone()as source:
		c.pause_threshold=2
		audio=c.listen(source)
	try:
		query=c.recognize_google(audio,language='en')
		print("Hai Bui :" + query)
	except sr.UnknownValueError:
		print("Please repeat or typing the command")
		query=str(input('Your order is:'))

if __name__ =="__main__":
	welcome()
	while True:
		query=command()
		if "google" in query:
				speak("What should I search boss?")
				search=command()
				url=f"https://www.google.com/search?q={search}"
				wb.get().open(url)
				speak(f'Here is your {search} on google')
		if "youtube" in query:
			speak("What should I search boss?")
			search=command() .lower()
			url=f"https://www.youtube.com/search?q={search}"
			wb.get().open(url)
			speak(f'Here is your {search} on youtube')
		elif "open video" in query:
			intro=r"C:\Users\TGDD\Documents\intro\intro.mp4"
			os.startfile(intro)
		elif "time" in query:
			time()
		elif "quit" in query:
			speak("Friday is quitting sir.Goodbye boss")
			quit()