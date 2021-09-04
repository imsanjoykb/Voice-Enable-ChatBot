#########################################################
# Developed By : Sanjoy Biswas                          #
# Project : Voice Enable ChatBot                        #
# Email : sanjoy.eee32@gmail.com                        #
#########################################################

### Import Necessary Libraries

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
import pyttsx3 as pp
from tkinter import *
import speech_recognition as s
#from espeakng import ESpeakNG
#import espeakng
#import os
#import warnings
from PIL import Image,ImageTk
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there ! Hope you are doing well.',
    'what is your name ?',
    'My name is BigBot , I am created For Mannat Technologies Work Demo',
    'how are you doing ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Doha, Dubai',
    'In which language you talk?',
    'I mostly talk in english',
    'Who is your Idol?',
    'My Idol is Elon Musk',
    'WHat is your favourite food?',
    'My favourite food is Charge'

]

trainer = ListTrainer(bot)

# Training the bot with the help of trainer of data
trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)


main = Tk()
main.geometry("400x550") # Define size
main.configure(bg='black') # Set Background color
main.title("Mannat Bot") # Set Title
img = PhotoImage(file=r"images\boticon.png")

#Resize the Image using resize method
#resized_image= img.resize((162,162), Image.ANTIALIAS)
#new_image= ImageTk.PhotoImage(resized_image)

photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            send_to_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def send_to_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating message text field

textF = Entry(main, font=("Verdana", 15))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Send To Bot", font=("Verdana", 10), command=send_to_bot, bg= '#5C00A3')
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# Bind main window with enter key...
main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


threadstart = threading.Thread(target=repeatL)

threadstart.start()

main.mainloop()
