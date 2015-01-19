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

#Denna klass hanterar inläsning av musik, ljudeffekter och bilder.

import pygame
from Content import Content
from Images import Images
from Sounds import Sounds
from Music import Music
import os
import Settings
from ErrorWindow import ErrorWindow

def load_menucontent(screen, settings):
    __image_files = list()
    __sound_files = list()
    __music_files = list()
    __play_sounds = True

    try:
        for file in os.listdir("Images/Menu"):
            if file.endswith(".bmp") or file.endswith(".png"):
                __image_files.append(file)
    except FileNotFoundError:
        message = "    Bild mappen kunde inte hittas!\nTips: Installera om spelet."
        error = ErrorWindow("Error!", message)
        error.show()
        raise SystemExit

    try:
        for file in os.listdir("Sounds/"):
            if file.endswith(".wav"):
                __sound_files.append(file)
    except FileNotFoundError:
        message = "    Ljud mappen kunde inte hittas!\nTips: Installera om spelet.\n\nVill du spela utan ljud?"
        error = ErrorWindow("Error!", message, True)
        __play_sounds = error.show()
    if __play_sounds:
        try:
            for file in os.listdir("Music/"):
                if file.endswith(".wav") or file.endswith(".mp3") or file.endswith(".ogg"):
                    __music_files.append(file)
        except FileNotFoundError:
            message = "    Musik mappen kunde inte hittas!\nTips: Installera om spelet.\n\nVill du spela utan musik?"
            error = ErrorWindow("Error!", message, True)
            __play_sounds = error.show()
            
    __images = __load_images("Images/Menu/", __image_files, screen, settings)
    __sounds = __load_sounds(__sound_files)
    __music  = __load_music(__music_files)
    return Content(__images, __sounds, __music, __play_sounds)
    
def load_content(screen, settings, play_sounds):
    __image_files = list()
    __sound_files = list()
    __music_files = list()
    try:
        for file in os.listdir("Images/"):
            if file.endswith(".bmp") or file.endswith(".png"):
                __image_files.append(file)
    except FileNotFoundError:
        message = "    Bild mappen kunde inte hittas!\nTips: Installera om spelet."
        error = ErrorWindow("Error!", message)
        error.show()
    if play_sounds:
        try:
            for file in os.listdir("Sounds/"):
                if file.endswith(".wav"):
                    __sound_files.append(file)
        except FileNotFoundError:
            message = "Inga ljudfiler hittades!\nTips: Installera om spelet.\n\nVill du spela utan ljud?"
            error = ErrorWindow("Error!", message, True)
            play_sounds = error.show()

    if play_sounds:
        try:
            for file in os.listdir("Music/"):
                if file.endswith(".wav") or file.endswith(".mp3") or file.endswith(".ogg"):
                    __music_files.append(file)
        except FileNotFoundError:
            message = "Inga musikfiler hittades!\nTips: Installera om spelet.\n\nVill du spela utan ljud?"
            error = ErrorWindow("Error!", message, True)
            play_sounds = error.show()

    
    __images = __load_images("Images/", __image_files, screen, settings)
    if play_sounds:
        __sounds = __load_sounds(__sound_files)
        __music  = __load_music(__music_files)
    return Content(__images, __sounds, __music, play_sounds)

def __load_images(filepath, image_files, screen, settings):
    __images = list()
    for file in image_files:
        item = (file[:-4], load_image(filepath, file, settings))
        __images.append(item)

    return Images(__images)

def __load_sounds(sound_files):
    __sounds = list()
    for file in sound_files:
        item = (file[:-4], pygame.mixer.Sound(os.path.join("Sounds/", file)))
        __sounds.append(item)

    return Sounds(__sounds)

def __load_music(music_files):
    __music = list()
    for file in music_files:
        item = (file[:-4], os.path.join("Music/", file))
        __music.append(item)

    return Music(__music)
    
    
def load_image(filepath, filename, settings):
    try:
        image = pygame.image.load(os.path.join(filepath, filename)).convert_alpha()
        return image
    except:
        message = "En eller flera bilder kunde inte hittas\nTips: Installera om spelet."
        error = ErrorWindow("Error!", message)
        pygame.quit()
        raise SystemExit(0)
    


def load_sound(filename):
    sound = pygame.mixer.Sound(os.path.join("Sounds", filename))
    return sound
