import datetime
import os
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from AppOpener import run
import time
from tkinter import messagebox
import tkinter as tk

from tkinter import simpledialog


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_cmd():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        cmd1 = ""
        try:

            cmd1 = listener.recognize_google(voice)
            cmd1 = cmd1.lower()
            if 'ultron' in cmd1:
                cmd1 = cmd1.replace('ultron', '', 1)


        except sr.UnknownValueError:
            print("Sorry, I didn't hear, Please repeat again!!")
            talk("Sorry, I didn't hear, Please repeat again!!")

            pass

    return cmd1


def timer():
    root = tk.Tk()

    root.geometry("300x250")

    root.title("Time Counter")

    # Declaration of variables
    hour = tk.StringVar()
    minute = tk.StringVar()
    second = tk.StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # Use of Entry class to take input from the user
    hourEntry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
    hourEntry.place(x=80, y=20)

    minuteEntry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=130, y=20)

    secondEntry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
    secondEntry.place(x=180, y=20)

    def submit():
        global temp

        try:

            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        except:
            print("Please input the right value")
            talk("Please input the right value")
        while temp > -1:

            mins, secs = divmod(temp, 60)

            hours = 0

            if mins > 60:
                hours, mins = divmod(mins, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            root.update()
            time.sleep(1)

            if temp == 0:
                talk("Time's Up!!")
                messagebox.showinfo("Time Countdown", "Time's up ")

            temp -= 1

    btn = tk.Button(root, text='Set Time Countdown', bd='5', command=submit)
    btn.place(x=70, y=120)

    root.mainloop()



def main1():
    talk("Hi , Iam Ultron")
    # while 1:
    talk("How can I help You!")
    cmd = take_cmd()
    # if cmd == 0:
    #     continue
    if "stop" in str(cmd) or "exit" in str(cmd) or "bye" in str(cmd):
        talk("Ok bye and take care")
        # break

    elif 'play' in cmd:
        song = cmd.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)
        # time.sleep(5)
    elif 'screenshot' in cmd:

        ct = datetime.datetime.now()
        ts = ct.timestamp()

        talk('taking, screenshot')
        print("Taking Screenshot")
        myScreenshot = pyautogui.screenshot()
        file_name = str(ts) + ".png"
        myScreenshot.save(file_name)
        # time.sleep(5)
    elif 'what is the time' in cmd or "time please" in cmd or "what is time" in cmd:
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current Time is ' + time1)
        print('Current Time is ' + time1)
    elif 'who is ' in cmd:
        cmd = cmd.replace("ultron", "", 1)
        person = cmd.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'where is' in cmd:
        cmd = cmd.replace("ultron", "", 1)
        s = cmd.replace("where is", "")
        print("searching..")
        talk("searching")
        pywhatkit.search(s)
        # time.sleep(5)
    elif 'tell me about' in cmd:
        cmd = cmd.replace("ultron", "", 1)
        s = cmd.replace("tell me about", "")

        print("searching..")
        talk("searching")
        pywhatkit.search(s)
    elif 'joke' in cmd:
        s = pyjokes.get_joke()
        print(s)
        talk(s)
    elif 'open google' in cmd:
        # webbrowser.open('https://google.com')
        run("google chrome")
        # time.sleep(5)
    elif "good morning" in cmd:

        print('Good morning')
        talk('Good morning')
    elif 'How are you' in cmd or 'how do you do' in cmd:
        print("Iam great, how are you!")
        talk("Iam great, how are you!")
    elif 'Iam good' in cmd or 'iam fine' in cmd:
        print("good to hear")
        talk("good to hear")
    elif 'who created you' in cmd or 'who made you' in cmd:
        print("i was created by Prashanth")
        talk("i was created by Prashanth")
        # time.sleep(5)
    elif 'do you love me' in cmd:
        print("everytime")
        talk("everytime")

    elif "thank you " in cmd or "thanks" in cmd:
        print("welcome, its my honour")
        talk("welcome, its my honour")
    elif "open telegram" in cmd or "open me telegram" in cmd:
        print("opening telegram")
        talk("opening telegram")
        # time.sleep(5)

        # os.system('cmd /c "python" ')
        run("telegram desktop")
    elif "open whatsapp" in cmd or "open me whatsapp" in cmd:
        print("opening whatsapp")
        talk("opening whatsapp")
        # time.sleep(5)

        # os.system('cmd /c "python" ')
        run("whatsapp")
    elif "open whatsapp" in cmd or "open me whatsapp" in cmd:
        print("opening whatsapp")
        talk("opening whatsapp")
        # os.system('cmd /c "python" ')
        run("whatsapp")

    elif 'notepad' in cmd:
        talk('Opening Notepad')
        print('Opening Notepad')
        os.system("Notepad")
    elif 'open camera' in cmd:
        talk('Opening camera')
        print('Opening camera')
        run("camera")
        # time.sleep(5)
    elif "start timer" in cmd:

        timer()
    elif "what is my name" in cmd:
        file1 = open('mydetails.txt', 'r')
        Lines = file1.readlines()
        st=""
        for i in Lines:
            if "name" in i.lower():
                st=i.lower()
                break
        file1.close()
        st=st.replace("name ","")
        talk(st)
    elif "new name" in cmd or "from now call me" in cmd:
        talk("Do you really want to change your name!")
        ROOT = tk.Tk()

        ROOT.withdraw()
        ans = simpledialog.askstring(title="Yes or No", prompt="Yes or No")
        ans=ans.lower()
        if ans=="yes":
            talk("What is your old name?")


        search_text =simpledialog.askstring(title="Old name", prompt="Old name")

        # creating a variable and storing the text
        # that we want to add
        talk("What is your new name")
        replace_text = simpledialog.askstring(title="New name", prompt="New name")
        with open(r'mydetails.txt', 'r') as file:


            data = file.read()

            data = data.replace(search_text, replace_text)
        with open(r'mydetails.txt', 'w') as file:

            file.write(data)
        talk("done")

    elif "send a whatsapp message" or " send whatsapp message" in cmd:
        ROOT = tk.Tk()

        ROOT.withdraw()

        mobie_num = simpledialog.askstring(title="Mobile number", prompt="Enter mobile number with country code")
        mesg = simpledialog.askstring(title="message", prompt="Enter message")

        pywhatkit.sendwhatmsg_instantly(
            phone_no=mobie_num,
            message=mesg
        )
        print("success!")
    else:
        if len(cmd) != 0:
            print("searching..")
            talk("searching")
            cmd = cmd.replace("ultron", "", 1)
            pywhatkit.search(cmd)

if __name__ == '__main__':
    main1()
