
# Import all the required modules
import os
import pyttsx3
import speech_recognition as sr 


# Creating Class
class codemonk1307:

    # function to take the user's choice commands as input
    def takeCommands(self):
        # using recognizer and microphone method for input voice commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            # number of seconds of non-speaking audio before a phrase is considered complete
            r.pause_threshold = 0.8
            audio = r.listen(source)

            # input Voice is identified
            try:
                # listening voice commands in indian english
                print("Recognizing")
                Query = r.recognize_google(audio, language = "en-in")

                # displaying the voice command
                print("the query is =", Query, "'")
            
            except Exception as e:
                # display the exception errors
                print(e)
                # handling Exception
                print("Say that again sir")
                return "None"
        return Query


    # method/funcion for generating Voice output
    def Speak(self, audio):
        # constructor call for pyttsx3.init()
        engine = pyttsx3.init("sapi5")
        # setting voice type and its id
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    
    # method to self shut down system
    def quitSelf(self):
        self.Speak("sir do u want the system to shut down")
        # input voice command
        take = self.takeCommands()
        choice = take
        if "yes" in choice:
            # shutting down
            print("shutting down the PC")
            self.Speak("Shutting your Computer")
            os.system("shutdown /s /t 30")

        if "no" in choice:
            # IDLE
            print("thank you sir")
            self.Speak("thank you sir")


# Driver's Code
if __name__ == "__main__":
    fool = codemonk1307()
    fool.quitSelf()

