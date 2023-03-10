from Body.AiBrain import ReplyBrain
from Body.Listen import MicExecution
from Body.Qna import QuestionsAnswer
print(">> Starting The Jarvis : Wait For Some Seconds. ")
from Body.speak import Speak
def MainExe():
    Speak("Hello Sir")
    Speak("I am Jarvis , I'm Ready to assist you sir")
    while True:
        Data = MicExecution()
        Data = str(Data)
        if len(Data)<3:
            pass
        elif "what is" in Data or "where is" in Data or "Question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
MainExe()
