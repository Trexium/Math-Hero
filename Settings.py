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

#Denna klass innehåller endast inställningar som position, storlek osv.
#Dessa delas med genom "properties" pga att spelet inte ska kunna ändra på dessa.

import pygame
class Settings(object):

    def __init__(self):
        #Screen settings
        self.__screen_size = width, height = 800, 600
        self.__title       = "Mattehjälten"
        self.__fps         = 60
        self.__trans_color = (255, 0, 255)

        #Game states
        self.__state_starting       = "STARTING"
        self.__state_running        = "RUNNING"
        self.__state_pause          = "PAUSE"
        self.__state_gameover       = "GAME_OVER"
        self.__state_menu           = "MAIN_MENU"
        self.__state_instructions   = "INSTRUCTIONS"
        

        #Backgrounds
        self.__loading_screen     = "loading_screen.bmp"
        self.__loading_screen_pos = (0, 0)

        #Layers
        self.__layers = (0, 1, 2, 3, 4, 5, 6)
        self.__platform_layer = 0
        self.__sideboard_layer = 0
        self.__lights_layer = 1
        self.__enemy_layer = 1
        self.__spawn_layer = 2
        self.__finish_layer = 2
        self.__ground_layer = 3
        self.__player_layer = 4
        self.__life_layer = 4
        self.__ps_layer = 4
        self.__problem_layer = 5
        self.__projectile_layer = 6

        
        
        

        #Level settings
        self.__ground_name = "GROUND"
        self.__ground_size = width, height = 800, 100
        self.__ground_pos = x, y = 0, (self.__screen_size[1] -
                                       self.__ground_size[1])

        self.__inviswall_name = "INVISIBLE_WALL"
        self.__platform_size = width, height = 450, 10
        self.__inviswall_size = width, height = 100, 400
        self.__inviswall_pos1 = x, y = 0, 0
        self.__inviswall_pos2 = x, y = (self.__screen_size[0] -
                                        self.__inviswall_size[0]), 0
        
        self.__platform_name = "PLATFORM"
        self.__platform1_pos = x, y = ((self.__screen_size[0]) -
                                       (self.__inviswall_size[0]) -
                                       (self.__platform_size[0])), 150
        self.__platform2_pos = x, y = self.__inviswall_size[0], 250
        self.__platform3_pos = x, y = (self.__screen_size[0] -
                                       self.__inviswall_size[0] -
                                       self.__platform_size[0]), 350
        self.__platform_layer = 1
        

        self.__spawn_name1, self.__spawn_name2, self.__spawn_name3 = "SPAWN_POINT_1", "SPAWN_POINT_2", "SPAWN_POINT_3"
        self.__middle_area = width, height = ((self.__screen_size[0] - (self.__inviswall_size[0] * 2)), (self.__screen_size[1] - self.__ground_size[1]))
        self.__spawn_size = width, height = 40, 40    
        
        self.__spawn_pos2 = x, y = (self.__screen_size[0] / 2 - (self.__spawn_size[0] / 2), 0)
        self.__spawn_pos1 = x, y = (self.__spawn_pos2[0] / 2, 0)
        self.__spawn_pos3 = x, y = (self.__spawn_pos2[0] * 1.5, 0)
        self.__spawn_pos = [self.__spawn_pos1, self.__spawn_pos2, self.__spawn_pos3]

        self.__finish_name = "FINISH_POINT"
        self.__finish_size = width, height = 70, 100
        self.__finish_pos = x, y = (self.__platform3_pos[0] - self.__finish_size[0] + 15, self.__screen_size[1] - self.__ground_size[1] - self.__finish_size[1])

        self.__sideboard_name = ("SIDEBOARD_LEFT", "SIDEBOARD_RIGHT")
        

        self.__sideboard_size = width, height = 113, 172
        self.__sideboard_y = 0
        self.__lsideboard_pos = (0, self.__sideboard_y)
        self.__rsideboard_pos = (self.__screen_size[0] - self.__sideboard_size[0], self.__sideboard_y)

        self.__score_name = "SCORE_"
        self.__score_pos = list()
        self.__score_pos.append((10, -4))
        self.__score_pos.append((10, 58))
        self.__score_pos.append((10, 117))
        self.__score_pos.append((61, 28))
        self.__score_pos.append((61, 89))


        self.__fail_name = "FAIL_"
        self.__fail_pos = list()
        self.__fail_pos.append((self.__screen_size[0] - 65, -3))
        self.__fail_pos.append((self.__screen_size[0] - 65, 59))
        self.__fail_pos.append((self.__screen_size[0] - 65, 118))
        self.__fail_pos.append((self.__screen_size[0] - 115, 29))
        self.__fail_pos.append((self.__screen_size[0] - 115, 90))

        self.__ps_name = "PROBLEM_SCREEN"
        self.__ps_size = width, height = (330, 60)
        self.__ps_pos = x, y = ((self.__screen_size[0] / 2) - (self.__ps_size[0] / 2), self.screen_size[1] - self.__ps_size[1] - 10)

        #Enemy settings
        self.__enemy_name = "ENEMY"
        self.__enemy_pos1 = self.__spawn_pos1
        self.__enemy_pos2 = self.__spawn_pos2
        self.__enemy_pos3 = self.__spawn_pos3
        self.__spawn_time = 5000
        self.__enemy_speed = (1, 5)
        self.__enemy_life = 1

        #Player settings
        self.__player_name = "PLAYER"
        self.__player_pos = (((self.__screen_size[0] / 2) - 10), (self.__ground_pos[1] - 100))
        self.__player_speed = (4, 5)
        self.__player_life = 3

        #Problem settings
        self.__problem_names = ("EASY_PROBLEM", "MEDIUM_PROBLEM", "HARD_PROBLEM")
        self.__problem_font = pygame.font.SysFont("Arial Black", 30)
        self.__problem_pos = (self.__ps_pos[0] + (self.__ps_size[0] / 2), self.__ps_pos[1] - (self.__ps_size[1] / 2))

        #Projectile settings
        self.__projectile_name = "PROJECTILE"
        self.__projectile_speed = (0, 7)
        self.__projectile_life = 1
        self.__reload_time = 2000

        #Menu settings
        self.__newgame_name = "NEW_GAME"
        self.__newgame_pos = ((self.__screen_size[0] / 2) - 250, 100)

        self.__instructions_name = "INSTRUCTIONS"
        self.__instructions_pos = ((self.__screen_size[0] / 2) - 256, self.__newgame_pos[1] + 150)

        self.__quit_name = "QUIT_GAME"
        self.__quit_pos = ((self.__screen_size[0] / 2) - 158, self.__instructions_pos[1] + 150)

        self.__info_name = "INFORMATION"
        self.__info_pos = ((self.__screen_size[0] / 2) - 258, 75)

        self.__menubutton_name = "MAIN_MENU_BUTTON"
        self.__menubutton_pos = (self.__info_pos[0] - 30, (self.__screen_size[1] - 105))

        

        self.__back_name = "BACK_BUTTON"
        self.__back_pos = ((self.__menubutton_pos[0] + 200), self.__menubutton_pos[1])

        self.__next_name = "NEXT_BUTTON"
        self.__next_pos = ((self.__back_pos[0] + 200), self.__back_pos[1])

        self.__gameover_name = "GAME_OVER"
        self.__gameover_pos = ((self.__screen_size[0] / 2) - 150, self.__info_pos[1])

        self.__gomenu_pos = ((self.__screen_size[0] / 2) - 180, 300)
        self.__restart_name = "RESTART"
        self.__restart_pos = ((self.__screen_size[0] / 2) + 4, 300)

        self.__pause_name = "PAUSE"
        self.__pause_pos = ((self.__screen_size[0] / 2) - 105, 150)

        self.__resume_name = "RESUME"
        self.__resume_pos = ((self.__screen_size[0] / 2) - 92, 320)

    
    #Menu properties
    @property
    def resume_name(self):
        return self.__resume_name

    @property
    def resume_position(self):
        return self.__resume_pos
    
    @property
    def pause_name(self):
        return self.__pause_name

    @property
    def pause_position(self):
        return self.__pause_pos
    
    @property
    def gameover_name(self):
        return self.__gameover_name

    @property
    def gameover_position(self):
        return self.__gameover_pos

    @property
    def gomenu_position(self):
        return self.__gomenu_pos

    @property
    def restart_name(self):
        return self.__restart_name

    @property
    def restart_position(self):
        return self.__restart_pos
    
    @property
    def next_name(self):
        return self.__next_name

    @property
    def next_position(self):
        return self.__next_pos

    @property
    def back_name(self):
        return self.__back_name

    @property
    def back_position(self):
        return self.__back_pos
    
    @property
    def menubutton_name(self):
        return self.__menubutton_name

    @property
    def menubutton_position(self):
        return self.__menubutton_pos
    
    @property
    def info_name(self):
        return self.__info_name

    @property
    def info_position(self):
        return self.__info_pos
    
    @property
    def instructions_name(self):
        return self.__instructions_name

    @property
    def instructions_position(self):
        return self.__instructions_pos

    @property
    def quit_name(self):
        return self.__quit_name

    @property
    def quit_position(self):
        return self.__quit_pos
    
    @property
    def newgame_name(self):
        return self.__newgame_name
    @property
    def newgame_position(self):
        return self.__newgame_pos

    #Projectile properties
    @property
    def projectile_name(self):
        return self.__projectile_name

    @property
    def projectile_speed(self):
        return self.__projectile_speed

    @property
    def projectile_life(self):
        return self.__projectile_life

    @property
    def reload_time(self):
        return self.__reload_time
        
    #Player properties
    @property
    def player_name(self):
        return self.__player_name

    @property
    def player_position(self):
        return self.__player_pos

    @property
    def player_speed(self):
        return self.__player_speed

    @property
    def player_life(self):
        return self.__player_life
    
    #Game states
    @property
    def state_starting(self):
        return self.__state_starting

    @property
    def state_running(self):
        return self.__state_running

    @property
    def state_pause(self):
        return self.__state_pause

    @property
    def state_gameover(self):
        return self.__state_gameover

    @property
    def state_menu(self):
        return self.__state_menu

    @property
    def state_instructions(self):
        return self.__state_instructions
    
    #Problem properties
    @property
    def problem_names(self):
        return self.__problem_names
    
    @property
    def problem_font(self):
        return self.__problem_font

    @property
    def problem_position(self):
        return self.__ps_pos

    @property
    def problem_size(self):
        return self.__ps_size
    
    #Enemy properties
    @property
    def enemy_life(self):
        return self.__enemy_life
    @property
    def enemy_speed(self):
        return self.__enemy_speed
    
    @property
    def spawn_time(self):
        return self.__spawn_time
    
    @property
    def enemy_name(self):
        return self.__enemy_name
        
    @property
    def enemy_position1(self):
        return self.__enemy_pos1

    @property
    def enemy_position2(self):
        return self.__enemy_pos2

    @property
    def enemy_position3(self):
        return self.__enemy_pos3
        
    #Screen properties
    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def screen_title(self):
        return self.__title

    @property
    def fps(self):
        return self.__fps

    @property
    def trans_color(self):
        return self.__trans_color

    #Background properties
    @property
    def loading_screen(self):
        return self.__loading_screen

    @property
    def loadscr_position(self):
        return self.__loading_screen_pos

    #Layers
    @property
    def layers(self):
        return self.__layers
    
    @property
    def platform_layer(self):
        return self.__platform_layer

    @property
    def sideboard_layer(self):
        return self.__sideboard_layer

    @property
    def lights_layer(self):
        return self.__lights_layer

    @property
    def enemy_layer(self):
        return self.__enemy_layer

    @property
    def spawn_layer(self):
        return self.__spawn_layer

    @property
    def finish_layer(self):
        return self.__finish_layer

    @property
    def ground_layer(self):
        return self.__ground_layer

    @property
    def player_layer(self):
        return self.__player_layer

    @property
    def ps_layer(self):
        return self.__ps_layer

    @property
    def life_layer(self):
        return self.__life_layer

    @property
    def problem_layer(self):
        return self.__problem_layer

    @property
    def projectile_layer(self):
        return self.__projectile_layer

 

    #Level properties
    @property
    def ground_position(self):
        return self.__ground_pos

    @property
    def ground_name(self):
        return self.__ground_name
    
    @property
    def inviswall_size(self):
        return self.__inviswall_size

    @property
    def inviswall_position1(self):
        return self.__inviswall_pos1

    @property
    def inviswall_position2(self):
        return self.__inviswall_pos2

    @property
    def inviswall_name(self):
        return self.__inviswall_name

    @property
    def platform_position1(self):
        return self.__platform1_pos

    @property
    def platform_position2(self):
        return self.__platform2_pos

    @property
    def platform_position3(self):
        return self.__platform3_pos

    @property
    def platform_name(self):
        return self.__platform_name

    @property
    def spawn_name1(self):
        return self.__spawn_name1

    @property
    def spawn_name2(self):
        return self.__spawn_name2

    @property
    def spawn_name3(self):
        return self.__spawn_name3

    @property
    def spawn_position1(self):
        return self.__spawn_pos1

    @property
    def spawn_position2(self):
        return self.__spawn_pos2

    @property
    def spawn_position3(self):
        return self.__spawn_pos3

    @property
    def spawn_positions(self):
        return self.__spawn_pos

    @property
    def finish_name(self):
        return self.__finish_name

    @property
    def finish_position(self):
        return self.__finish_pos

    @property
    def sideboard_name(self):
        return self.__sideboard_name

    @property
    def lsideboard_position(self):
        return self.__lsideboard_pos

    @property
    def rsideboard_position(self):
        return self.__rsideboard_pos

    @property
    def score_name(self):
        return self.__score_name

    @property
    def score_position(self):
        return self.__score_pos

    @property
    def fail_name(self):
        return self.__fail_name

    @property
    def fail_position(self):
        return self.__fail_pos

    @property
    def problem_name(self):
        return self.__ps_name

    


