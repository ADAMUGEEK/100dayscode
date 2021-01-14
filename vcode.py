import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()  # object creation no need in pycharm
    welcome = "\t\t\t welcome to geek innovative technology"
    my_name = "CEO"

    def speak(text):
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    speak(welcome)
    
    user = ""
    print(welcome)
    user = str(input(speak("what is your name please")))
    if user == "adamu" or user == "ADAMU":
        speak("welcome back my dear may Allah bostowed orpan you door's of success and grant you his mercy ameen ameen ameen" )
        if user == "adamu":
            speak(f"yea let do it {my_name} we are all set")
        elif user == "ADAMU":
            speak(f"sorry to interrupt but the keyboard is in cap")
    else:
        speak(f"hello {user} how may i help you")

    




