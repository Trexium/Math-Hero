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

#Denna klass förbereder huvudmenyn genom att ladda in bilder, music och ljudeffekter.





#Importering av klasser och moduler
import pygame
import os
import ContentManager
from Content import Content
from Settings import Settings
from TimeManager import TimeManager



def main():
    try:
        from MainMenu import MainMenu
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        __settings = Settings()
        __time_manager = TimeManager(__settings)
        __screen = __initialize_screen(__settings)
        __loading_screen(__screen, __settings)
        __content = ContentManager.load_menucontent(__screen, __settings)
        __settings.play_sounds = __content.play_sounds
        main_menu = MainMenu(__content, __settings, __screen, __time_manager)

        main_menu.show()
    except SystemExit:
        os._exit(1)
    


def __initialize_screen(settings):
    screen = pygame.display.set_mode(settings.screen_size, 0, 32)
    pygame.display.set_caption(settings.screen_title)
    return screen

#Denna funktion laddar in bild för en "splash-screen" så spelaren har något
#att titta på medans han vänter på att resterande innehåll ska ladda
def __loading_screen(screen, settings):
    splash_screen = ContentManager.load_image("Images/", settings.loading_screen, settings)
    screen.blit(splash_screen, settings.loadscr_position)
    pygame.display.flip()



if __name__ == '__main__':
    main()
