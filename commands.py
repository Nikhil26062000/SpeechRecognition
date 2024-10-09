import subprocess
import os
import webbrowser as web
from googlesearch import search

global app
global i


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    # def introducer(self):
    #     i=0
    #     self.respond("Hie Buddy")
    #     i+=1


    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("you have not told  me your name yet")
            else:
                self.respond("My name is Speech Recognizer. How can i help you?")

        if "start" in text:
            app = text.split(" ", 1)[-1]
            if "Chrome" in app:
                self.respond("starting " + app)
                os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            elif "sublime" in app:
                self.respond("starting " + app)
                os.startfile("C:\Program Files\Sublime Text 33\sublime_text.exe")
            elif "brackets" in app:
                self.respond("starting " + app)
                os.startfile("C:\Program Files (x86)\Brackets\Brackets.exe")
            elif "Firefox" in app:
                self.respond("starting " + app)
                os.startfile("C:\Program Files\Mozilla Firefox\Firefox.exe")

            else:
                self.respond("Cannot find the app")

        if "open" in text or "Open" in text:
            searchText = text.split(" ", 1)[-1]
            path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            self.respond("Opening " + searchText)
            print(searchText)
            web.get(path).open(searchText)


        if "search" in text or "Search" in text:
            searchText = text.split(" ", 1)[-1]
            self.respond("searching " + searchText)
            for i in search(searchText, tld="co.in", num=10, stop=10, pause=2):
                print(i)

    def respond(self, response):
        print(response)
        subprocess.call(
            "PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + response + "')",
            shell=True)
