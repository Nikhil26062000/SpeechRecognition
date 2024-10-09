import pyaudio
import wave
import running as running
import speech_recognition as sr
import subprocess
from commands import Commander

running = True


def echo(text):
    subprocess.call(
        "PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + text + "')",
        shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()
    pa.terminate()


r = sr.Recognizer()
# r.pause_threshold = 0.5
cmd = Commander


def initSpeech():
    print('Listening...')


    with sr.Microphone() as source:
        print('Say something')
        play_audio('Audio/hello.wav')
        audio = r.listen(source)

        command = ''
        try:
            command = r.recognize_google(audio)
        except:
            print("could not understand")
               # print("Couldn't understand, bro.")

        print('Your command:')
        print(command)
        if command in ["quit", "exit"]:
            global running
            print("Thank you for using Speech Recognizer. Have a Great day")
            running = False

        Commander().discover(command)


while running == True:
    initSpeech()
    # r.pause_threshold = 0.5