import os
import only_emotion as vt
import task_assistant as ta
import random
import time
import webbrowser


if __name__ == '__main__':

	ta.wishMe()
	emo = "abc"
	ta.speak("Checking your mood")

	while emo != "none":
		emo = vt.emotion_()
		break


	emo = "happy"
	print(emo)

	if emo == 'happy':
		ta.speak("You look so happy")
		time.sleep(1)
		ta.speak("Stay happy")
		time.sleep(1)
		ta.speak("any work is remain tell me ")
		time.sleep(1)
		ta.task()

	elif emo == "neutral":
		ta.speak("You look neutral")
		time.sleep(1)
		ta.speak("can i tell you a joke")

		answer = ta.take_command()
		if answer == "yes":
			time.sleep(1)
			ta.speak("why was the stadium so cool ???")
			time.sleep(1)
			ta.speak("it was fil with fans")
		else:
			ta.task()

	elif emo == 'sad':
		ta.speak("you look so sad")
		ta.speak("stay happy don't be a sad")
		ta.speak("do you want to listen music???")
		answer = ta.take_command()
		if answer == "yes":
			
			music_path = "give your music path"
			songs = os.listdir(music_path)
			play_song = music_path + "WhatsApp Audio 2019-09-21 at 2.41.21 PM.mp3"
			os.startfile(play_song)
		else:
			ta.speak("can i play video")
			ans = ta.take_command()
			if ans == "yes":
				webbrowser.open("https://www.youtube.com/watch?v=ZebSXPUCPFc")


	elif emo == 'angry':
		ta.speak("you are so angry")
		list_qoute = ["anger is, most dangerous, inner enemy","the greatest, remedy for anger, is delay","control your, anger is your biggest strength"]
		rand_ = random.randint(0, 2)
		ta.speak(list_qoute[rand_])
		ta.speak("can we performe one exercise??")
		answer = ta.take_command()
		if answer == "yes":
			count = 0
			num_list = list(range(1,11))
			ta.speak("I have an acitivity")
			ta.speak("speak with me")
			for i in num_list[::-1]:
				ta.speak(i)
				for j in range(1000000):
					count += 1
				
			ta.speak("I hope you will feel better now")
		else:
			ta.task()


	elif emo == 'fear':
		ta.speak("why are you scary!!!")
		list_qoute = ["Fear is only deep as the mind allows","feAr is pain arising from anticipation of evil","everything you want is on the other side of fear"]
		rand_ = random.randint(0,2)
		ta.speak(list_qoute[rand_])
		ta.speak("sir,can i play video for you ???")
		answer = ta.take_command()
		if answer == "yes":
			webbrowser.open("https://www.youtube.com/watch?v=af9qXLrPadA")
		else:
			ta.task()




	elif emo == 'surprise':
		ta.speak("you look so surprise!!!")
		ta.speak("")

	else:
		try:
			ta.speak('you look so disgust')
		except:
			pass