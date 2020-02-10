import pyttsx3
import datetime
import wikipedia
import tkinter.filedialog as filedialog
import os 
import pygame 
from pygame.locals import *
import time
import random
import pygame.mixer
from pygame import mixer

import speech_recognition as jr


#setting voice for jrvis
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

#jarvis audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishing
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour<=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak('good Evning')
    
    speak('I am jarvis. Tell me how may I help you')

#speech input
def takecommand():
    s = jr.Recognizer()
    with jr.Microphone() as source:
        print('Listning.........')
        s.pause_threshold = 1
        audio = s.listen(source)

        try:
            print('Recogniging......')
            query = s.recognize_google(audio,language = 'en-in')
            print(f"User said : {query}\n")

        except Exception as e:
            #print(e)
            speak('say that again')
            return "None"
        
        return query

def nextsong():
    pygame.mixer.music.stop()

def stop_playing():
    pygame.mixer.music.pause()

def continue_music():
    pygame.mixer.music.unpause()
    
            
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        #logic for exicuting task
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia'," ")
            results = wikipedia.summary(query, sentences = 10)
            speak('according to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            os.spawnl(os.P_NOWAIT, r'C:\Program Files\Mozilla Firefox\Firefox.exe',r'FireFox', '-new-tab', 'https://www.youtube.com/')
        
        elif 'open google' in query:
            speak('opening google')
            os.spawnl(os.P_NOWAIT, r'C:\Program Files\Mozilla Firefox\Firefox.exe',r'FireFox', '-new-tab', 'https://www.google.com/')

        
        elif 'play music' in query:

            speak('playing music')
            music_dir = r'D:\Music'
            playlist = []
            for files in os.listdir(music_dir):
                if files.endswith(".mp3"):
                    playlist.append(os.path.join(music_dir,files))
            
            songs = len(playlist)
            
            pygame.mixer.init()
            for songs in playlist:
                pygame.mixer.music.load(songs)
                pygame.mixer.music.play()
                now_playing = songs.split('\\')
                l = len(now_playing) - 1
                song_name = now_playing[l]
                song_name2 = song_name.replace(".mp3"," ")
                print('Now playing : ',song_name2)
                
                speak('Now playing')
                speak(song_name2)
                stop_query = takecommand().lower()
                
                
                if 'next song' in stop_query:
                    nextsong()
    
                elif 'stop playing' in stop_query:
                    
                    stop_playing()
                    break
                elif 'continue' in stop_query:
                    pygame.mixer.music.unpause()
                
                
                while pygame.mixer.music.get_busy():
                    
                    pygame.time.Clock().tick(5)
            
        
                    
                    
                    

                    

                    

         

               

        
            
                
            
            
                        
                        