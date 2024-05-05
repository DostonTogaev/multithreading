import pyttsx3
engine = pyttsx3.init()
engine.say('Asror nima gap, qachon boramiz Tatuga')
engine.setProperty('rate', 125)
rate = engine.getProperty('rate')
print(rate)
engine.save_to_file('Asror nima gap, qachon boramiz Tatuga','Asror.mp3')
engine.runAndWait()
engine.stop()