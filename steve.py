# Created on October 3, 2016

import speech_recognition as sr
import pyttsx
import time
import os
import pygame.mixer
import random

engine = pyttsx.init()
r = sr.Recognizer()
pygame.mixer.init()

def listen():
    with sr.Microphone() as source:
        print("*listening")
        return r.listen(source)

options = open("options.txt")
name = options.readline()[5:-1].lower()
transcribe = options.readline()[11:-1].lower()
img_name = options.readline()[11:-1]
options.close()

functions = ["no",
             "print file",
             "your functions",
             "play music",
             "make text file",
             "change my name option",
             "change my transcribe option",
             "change my image name option",
             "get random number",
             "run command",
             "get milestones",
             "take picture"]

trans = False
if transcribe == "yes":
    trans = True

if trans:
    trans_file = open("transcription.txt", 'a')
    trans_file.write("-*-*-*-*-*-*-*-*-*-\n")

try:
    print("<steve> Hello. I am Steve, your digital assistant. Is there anything I can do for you?")
    engine.say("Hello. I am Steve, your digital assistant. Is there anything I can do for you?")
    engine.runAndWait()

    if trans:
        trans_file.write("<steve> Hello. I am Steve, your digital assistant. Is there anything I can do for you?\n")

    anyelse = True

    while True:
        audio = listen()

        try:
            words = r.recognize_google(audio)
            print("<%s> "%name + words)
            if trans: trans_file.write("<%s> "%name+words+"\n")
    
            if words.lower() == "no":
                print("<steve> Goodbye.")
                engine.say("Goodbye.")
                engine.runAndWait()
                print("*quitting")
                if trans:
                    trans_file.write("<steve> Goodbye.\n*quitting\n")
                    trans_file.close()
                break
                
            elif words.lower() == "get milestones":
                for stone in milestones:
                    print("> %s"%stone + " : " + "%s"%milestones[stone])
                    if trans:
                        trans_file.write("> %s\n"%stone)
                    time.sleep(1)
                
            elif words.lower() == "run command":
                engine.say("what command?")
                engine.runAndWait()
                x = str(raw_input("<steve> What command? "))
                if trans: trans_file.write("<steve> What command? %s"%x)
                os.system(x)
        
            elif words.lower() == "your functions":
                print("<steve> Here are my functions:")
                engine.say("here are my functions")
                engine.runAndWait()
                for func in functions:
                    print("> %s"%func)
                    engine.say(func)
                    engine.runAndWait()
                    if trans:
                        trans_file.write("> %s\n"%func)
                    time.sleep(1)
            
            elif words.lower() == "get random number":
                num = random.random()
                print("<steve> The number: %.2f"%num)
                engine.say("the number: %.2f"%num)
                engine.runAndWait()
                if trans:
                    trans_file.write("<steve> The number: %.2f\n"%num)
                del num
                
            elif words.lower() == "print file":
                engine.say("Type the filename here:")
                engine.runAndWait()
                x = str(raw_input("<steve> Type the filename here: "))
                if trans:
                    trans_file.write("<steve> Type the filename here: "+x+"\n")
                try:
                    File = open(x, 'r')
                    readfile = File.read()
                    File.close()
                    print("<steve> Here is your file:")
                    engine.say("Here is your file:")
                    print(readfile)
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Here is your file:\n"+readfile+"\n")
                except IOError:
                    print("<steve> There was an error reading this file.")
                    engine.say("There was an error reading this file.")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> There was an error reading this file.\n")
            
            elif words.lower() == "play music":
                engine.say("Type the filename here:")
                engine.runAndWait()
                x = str(raw_input("<steve> Type the filename here: "))
                if trans:
                    trans_file.write("<steve> Type the filename here: "+x+"\n")
                try:
                    print("<steve> Here is your music:")
                    engine.say("Here is your music:")
                    engine.runAndWait()
                    print("*playing")
                    if trans:
                        trans_file.write("<steve> Here is your music:\n*playing\n")
                    try:
                        sound = pygame.mixer.Sound(x)
                        sound.play()
                        while pygame.mixer.get_busy(): time.sleep(0.1)
                    except KeyboardInterrupt:
                        sound.stop()
                        del sound
                except:
                    print("<steve> There was an error playing this music.")
                    engine.say("There was an error playing this music.")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> There was an error playing this music.\n")
            
            elif words.lower() == "make text file":
                engine.say("Where should I save this file?")
                engine.runAndWait()
                x = str(raw_input("<steve> Where should I save this file? "))
                if trans:
                    trans_file.write("<steve> Where should I save this file? "+x)
                engine.say("Start talking now.")
                engine.runAndWait()
                print("<steve> Start talking now.")
                if trans:
                    trans_file.write("<steve> Start talking now.\n*listening\n")
                while True:
                    try:
                        audio2 = listen()
                        words2 = r.recognize_google(audio2)
                        break
                    except sr.UnknownValueError:
                        print("<steve> What did you say?")
                        engine.say("What did you say?")
                        engine.runAndWait()
                        if trans:
                            trans_file.write("<steve> What did you say?\n")
                    except sr.RequestError:
                        print("<steve> There is no Internet connection. Goodbye.\n*quitting")
                        engine.say("There is no Internet connection. Goodbye.")
                        engine.runAndWait()
                        if trans:
                            trans_file.write("<steve> There is no Internet connection. Goodbye.\n*quitting\n")
                try:
                    fileobj = open(x,'w')
                    fileobj.write(words2)
                    fileobj.close()
                    del audio2, words2
                    print("<steve> File has been saved successfully.")
                    engine.say("File has been saved sucessfully.")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> File has been saved successfully.\n")
                except:
                    try: fileobj.close()
                    except: pass
                    print("<steve> There was an error saving this file.")
                    engine.say("There was an error saving this file.")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> There was an error saving this file.\n")
            
            elif words.lower() == "take picture":
                if img_name == "$TIME":
                    img_name = str(time.clock())
                print("<steve> Picture will be saved to \"~Pictures/steve/%s.bmp\" using CommandCam."%img_name)
                engine.say("Picture will be saved to the steve folder in Pictures as %s dot b m p using commandcam"%img_name)
                engine.runAndWait()
                time.sleep(2)
                if trans:
                    trans_file.write("<steve> Picture will be saved to \"~Pictures/steve/%s.bmp\" using CommandCam.\n"%img_name)
                print("*shooting image %s.bmp"%img_name)
                if trans:
                    trans_file.write("*shooting image %s.bmp\n"%img_name)
                os.system("C:/Users/belew/Documents/steve/webcam.exe /filename C:/Users/belew/Pictures/steve/%s.bmp"%img_name)
                print("<steve> Saved!")
                if trans:
                    trans_file.write("<steve> Saved!\n")
                engine.say("Saved!")
                engine.runAndWait()
            
            elif words.lower() == "change my name option":
                try:options = open("C:/Users/belew/Documents/steve/options.txt", "w")
                except IOError:
                    print("<steve> Cannot change file.")
                    engine.say("Cannot change file")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Cannot change file.\n")
                else:
                    engine.say("What should I change your name to?")
                    engine.runAndWait()
                    new = str(raw_input("<steve> What should I change your name to? "))
                    if trans:
                        trans_file.write("<steve> What should I change your name to? %s"%new)
                    options.write("NAME %s\nTRANSCRIBE %s\nIMAGE_NAME %s\nEND"%(new,transcribe,img_name))
                    name = new.lower()
                    del new
                    options.close()
                    print("<steve> Changed!")
                    engine.say("changed")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Changed!\n")
                
            elif words.lower() == "change my transcribe option":
                try:options = open("C:/Users/belew/Documents/steve/options.txt", "w")
                except IOError:
                    print("<steve> Cannot change file.")
                    engine.say("Cannot change file")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Cannot change file.\n")
                else:
                    engine.say("What should I change the transcribe to?")
                    engine.runAndWait()
                    new = str(raw_input("<steve> What should I change the transcribe to? (YES/NO) "))
                    if trans:
                        trans_file.write("<steve> What should I change the transcribe to? (YES/NO) %s"%new)
                    options.write("NAME %s\nTRANSCRIBE %s\nIMAGE_NAME %s\nEND"%(name,new,img_name))
                    del new
                    options.close()
                    print("<steve> Changed!")
                    engine.say("changed")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Changed!\n")
    
            elif words.lower() == "change my image name option":
                try:options = open("C:/Users/belew/Documents/steve/options.txt", "w")
                except IOError:
                    print("<steve> Cannot change file.")
                    engine.say("Cannot change file")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Cannot change file.\n")
                else:
                    engine.say("What should I change the image name to? ")
                    engine.runAndWait()
                    new = str(raw_input("<steve> What should I change the image name to? "))
                    if trans:
                        trans_file.write("<steve> What should I change the image name to? %s"%new)
                    options.write("NAME %s\nTRANSCRIBE %s\nIMAGE_NAME %s\nEND"%(name,transcribe,new))
                    del new
                    options.close()
                    print("<steve> Changed!")
                    engine.say("changed")
                    engine.runAndWait()
                    if trans:
                        trans_file.write("<steve> Changed!\n")
            
            else:
                print("<steve> I do not know this command, \""+words+"\".")
                engine.say("I do not know this command, \""+words+"\".")
                engine.runAndWait()
                if trans:
                    trans_file.write("<steve> I do not know this command, \""+words+"\".\n")
            
        except sr.UnknownValueError:
            if random.random() > 0.5:
                print("<steve> What did you say?")
                engine.say("What did you say?")
                engine.runAndWait()
                anyelse = False
                if trans:
                    trans_file.write("<steve> What did you say?\n")
            else:
                print("<steve> Goodbye.")
                engine.say("Goodbye.")
                engine.runAndWait()
                print("*quitting")
                if trans:
                    trans_file.write("<steve> Goodbye.\n*quitting\n")
                    trans_file.close()
                break
                
        except sr.RequestError as e:
            print("<steve> There is no Internet connection. I cannot understand you. Goodbye.")
            engine.say("There is no Internet connection. I cannot understand you. Goodbye.")
            engine.runAndWait()
            print("*quitting")
            if trans:
                trans_file.write("<steve> There is no Internet connection. Goodbye.\n*quitting\n")
                trans_file.close()
            break
        
        if anyelse:
            print("<steve> Anything else?")
            engine.say("Anything else?")
            engine.runAndWait()
            if trans:
                trans_file.write("<steve> Anything else?\n")
    
    if trans:
        if not trans_file.closed:
            trans_file.close()
    
    pygame.mixer.quit()

except KeyboardInterrupt:
    if trans:
        trans_file.close()
    pygame.mixer.quit()
