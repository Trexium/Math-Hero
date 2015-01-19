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

#Denna klass hanterar rörliga speliobjekt såsom siffror, spelare och projektiler.

import pygame
from pygame.locals import *
import Settings
from Enemy import Enemy
from Player import Player
from Projectile import Projectile
import random

class DynamicObjectManager(object):
    def __init__(self, settings, images, sounds):
        super().__init__()
        self.__settings = settings
        self.__sprites = pygame.sprite.Group()
        self.__spawn_pos = list()
        self.__spawn_pos.append(self.__settings.enemy_position1)
        self.__spawn_pos.append(self.__settings.enemy_position2)
        self.__spawn_pos.append(self.__settings.enemy_position3)
        self.__images = images.sprites
        self.__enemy_id = 0
        self.__number_finished = None
        self.__sprite_finished = None
        self.__player = None
        self.__player_image = images.player
        self.__add_player()
        self.__projectile_image = images.projectile
        self.__projectiles = pygame.sprite.Group()
        self.__last_key = None
        self.__correct_count = 5
        self.__hit_sound = sounds.hit
        self.__projectile_sound = sounds.shoot
        self.__hit_sound = sounds.hit
        
        


    def __add_enemy(self, number):
        __rand_pos = random.randint(0, 2)
        __pos = (self.__spawn_pos[__rand_pos][0] + 10, self.__spawn_pos[__rand_pos][1])
        __enemy = Enemy(__pos, self.__settings.enemy_name,
                                 self.__settings.enemy_layer,
                                 self.__images[number],
                                 self.__settings.enemy_speed,
                                 self.__settings.enemy_life,
                                 number,
                                 self.__enemy_id,
                                 None,
                                 (-1, 0))
        if __enemy.spawn_sound != None:
            __enemy.spawn_sound.play()
        self.__sprites.add(__enemy)
        
        self.__enemy_id += 1

    def __add_player(self):
        self.__player = Player(self.__settings.player_position,
                               self.__settings.player_name,
                               self.__settings.player_layer,
                               self.__player_image, self.__settings.player_speed,
                               self.__settings.player_life)
        self.__sprites.add(self.__player)

    def __player_shot(self):
        __projectile = Projectile((self.__player.position[0] + (self.__player_image.get_width() / 2) - (self.__projectile_image.get_width() / 2), self.__player.position[1]),
                                         self.__settings.projectile_name, self.__settings.projectile_layer, self.__projectile_image, self.__settings.projectile_speed,
                                         self.__settings.projectile_life,
                                         self.__projectile_sound)
        if __projectile.spawn_sound != None:
            __projectile.spawn_sound.play()
        self.__projectiles.add(__projectile)

    def __bullet_storm(self):
        for x in range(120):
            __projectile = Projectile((random.randint(0, 800), random.randint(610, 3000)),
                                              self.__settings.projectile_name,
                                              self.__settings.projectile_layer,
                                              self.__projectile_image,
                                              self.__settings.projectile_speed,
                                              self.__settings.projectile_life,
                                              self.__projectile_sound)
            self.__projectiles.add(__projectile)

    def update(self, level_objects, time_manager, input_events, correct_number):
        self.__number_finished = None
        self.__sprites.update(time_manager)
        self.__check_collisions(level_objects)
        if len(self.__sprites) < 6:
            if time_manager.spawn_check:
                if self.__correct_count > 0:
                    e_number = random.randint(0, 9)
                    self.__correct_count -= 1
                else:
                    e_number = correct_number
                    self.__correct_count = 5
                self.__add_enemy(e_number)

        for projectile in self.__projectiles:
            projectile.update(time_manager)
            if projectile.position < (0, 0) or projectile.position > self.__settings.screen_size:
                projectile.kill()

        for event in input_events:
            if event.type == KEYUP:
                if event.key == self.__last_key:
                    self.__player.direction = (0, 0)
                if event.key == K_0:
                    self.__add_enemy(0)
                if event.key == K_1:
                    self.__add_enemy(1)
                if event.key == K_2:
                    self.__add_enemy(2)
                if event.key == K_3:
                    self.__add_enemy(3)
                if event.key == K_4:
                    self.__add_enemy(4)
                if event.key == K_5:
                    self.__add_enemy(5)
                if event.key == K_6:
                    self.__add_enemy(6)
                if event.key == K_7:
                    self.__add_enemy(7)
                if event.key == K_8:
                    self.__add_enemy(8)
                if event.key == K_9:
                    self.__add_enemy(9)
                if event.key == K_F1:
                    self.__bullet_storm()
                
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.__player.direction = (-1, 0)
                    self.__last_key = event.key
                if event.key == K_RIGHT:
                    self.__player.direction = (1, 0)
                    self.__last_key = event.key
                if event.key == K_SPACE:
                    self.__player_shot()

            

    def __check_collisions(self, sprite_group):
        for sprite in self.__sprites:
            self.__object_collision(sprite, pygame.sprite.spritecollide(sprite, sprite_group, False))
            self.__sprite_collisions(sprite, pygame.sprite.spritecollide(sprite, self.__sprites, False))
            self.__sprite_collisions(sprite, pygame.sprite.spritecollide(sprite, self.__projectiles, False))

    def __sprite_collisions(self, sprite, collisions):
        if sprite.name == self.__settings.enemy_name:
            for collision in collisions:
                if collision.name != self.__settings.player_name and collision.name != self.__settings.projectile_name:
                    if sprite.identity != collision.identity:
                        if sprite.falling:
                            collision.kill()
                        elif collision.falling:
                            pass
                        elif sprite.falling == False:
                            sprite.change_direction()
                            
                        if sprite.falling and collision.falling:
                            sprite.direction = (0, 1)
                if collision.name == self.__settings.projectile_name:
                    if self.__hit_sound != None:
                        self.__hit_sound.play()
                        
                    sprite.kill()
                    collision.kill()
            

    def __object_collision(self, sprite, collisions):
        
        if len(collisions) > 0:
            if sprite.name == self.__settings.enemy_name:
                for collision in collisions:
                    if collision.name == self.__settings.platform_name and sprite.falling:
                        sprite.falling = False

                    if collision.name == self.__settings.inviswall_name:
                        sprite.change_direction()

                    if collision.name == self.__settings.ground_name:
                        self.__number_finished = sprite.number
                        sprite.kill()

            if sprite.name == self.__settings.player_name:
                for collision in collisions:
                    if collision.name == self.__settings.ground_name and sprite.falling:
                        sprite.falling = False

                    if collision.name == self.__settings.inviswall_name:
                        if collision.position[0] < 0:
                            sprite.position = (0, sprite.position[1])
                        else:
                            sprite.position = (self.__settings.screen_size[0] - sprite.image.get_width(),
                                               sprite.position[1])
    
        if len(collisions) <= 0:
            sprite.falling = True

        del collisions[:]


    @property
    def sprites(self):
        return self.__sprites

    @property
    def projectiles(self):
        return self.__projectiles

    @property
    def number_finished(self):
        return self.__number_finished
