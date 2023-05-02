import csv
import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer()
engine = pyttsx3.init()
with sr.Microphone() as source:
    print("Speak the name of the person you want to search for:")
    audio = r.listen(source)
search=r.recognize_google(audio)
if search=="Faculty":
    name_to_search = r.recognize_google(audio)
elif search=="RoomNo":
    floor_to_search=r.recognize_google(audio)
with open('NWC Name board1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Faculty Name'] == name_to_search:
            engine.say(row)
            engine.runAndWait()
        elif row['ROOM NO']==floor_to_search:
            engine.say(row)
            engine.runAndWait()