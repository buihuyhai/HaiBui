import speech_recognition
import pyttsx3
from datetime import date, datetime
robot_ear = speech_recognition.Recognizer()
while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you == ""

	print("You: " + you)

	if you == "":	
		robot_brain = "I can't hear you,try again"
	elif "good" in you:
		robot_brain = "Nice to meet you"
	elif "going" in you:
		robot_brain = "I'm fine, what about you?"
	elif "I" in you:
		robot_brain = "what do you want to know?"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "tomorrow" in you:
		robot_brain = "Duyen birthday"
	elif "happy" in you:
		robot_brain = 'Happy birthday Duyen'
		print("Chúc Duyên sinh nhật vui vẻ!!! Tuổi mới xinh đẹp hơn, học giỏi hơn, “duyên” hơn…etc❤ Chúc mừng ngày thiên thần ra đời!")
	elif "thank" in you:
		robot_brain = "You well come!"
	elif "bye" in you:
		robot_brain = "goodbye, see you again!"
		print("Robot:"  + robot_brain)
		engine = pyttsx3.init()
		engine.say(robot_brain)
		engine.runAndWait()
		break
	else:
		robot_brain = "sorry, Can you say again?"

	print("Robot:" +robot_brain)
	engine = pyttsx3.init()
	engine.say(robot_brain)
	engine.runAndWait()
