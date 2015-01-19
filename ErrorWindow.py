#Emil Gilljam, emgi8934, emil@gilljam.org
#Windows 7 Ultimate, 64-bit
#Python 3.3.2 32-bit
#Pygame 1.9.2a0
#Datum: 2013-08-15

#Spelet går ut på att lösa ett matteproblem genom att låta
#"rätt" siffra passera längst banen ner i ett rör
#och förstöra de siffror som är "fel" genom att skjuta projektiler på dem.
#Rätt siffra är den som löser matteproblemet.
#Du använder höger och vänster pilarna för att flytta på spelaren
#och skjuter projektiler med mellanslag.

#Detta objekt representerar ett fönster som visar fel vid inläsning av
#musik, ljudeffekter eller bilder.

from tkinter import *
import os

class ErrorWindow(object):
    def __init__(self, title, message, run_anyway = False):
        self.__play_sounds = True
        self.__container = Tk()
        self.__container.geometry("200x150")
        self.__container.title(title)
        self.__frame = Frame(self.__container)
        self.__frame.pack(fill=BOTH, expand=True)

        self.__lbl_message = Label(self.__frame, text = message)
        self.__lbl_message.place(x = ((self.__frame['width'] / 2) - (self.__lbl_message['width'] / 2)), y = 20)

        if run_anyway:
            self.__btn_yes = Button(self.__frame, text = "Ja", width = 5, command = self.run_game)
            self.__btn_yes.place(x = 30, y = 110)

            self.__btn_no = Button(self.__frame, text = "Nej", width = 5, command = self.quit_game)
            self.__btn_no.place(x = 110, y = 110)

        else:
            self.__btn_ok = Button(self.__frame, text = "OK", command = self.__container.destroy)
            self.__btn_ok.place(x = 90, y = 110)
        
        
        

    def show(self):
        self.__container.mainloop()
        return self.__play_sounds

    def quit_game(self):
        raise SystemExit

    def run_game(self):
        self.__play_sounds = False
        self.__container.destroy()
