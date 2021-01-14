import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()  # object creation

    def speak(text):
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    speak("welcome")    
    




