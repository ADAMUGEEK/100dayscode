import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()  # object creation
    welcome = "\t\t\t welcome to geek innovative technology"

    def speak(text):
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    speak("welcome")

    print(welcome)
    user = input(speak("whow are you please"))
    speak(f"hello {user} how may i help you")
    




