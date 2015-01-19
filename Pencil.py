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

#Denna klass används för att rita ut allt på skärmen.

import pygame

class Pencil:

    @staticmethod
    def draw(background, level_objects, sprites, projectiles, problem, settings, pause_menu = None):
        bg = background
        for layer in settings.layers:
            for obj in level_objects:
                if obj.layer == layer:
                    bg.blit(obj.image, obj.position)

            for sprite in sprites:
                if sprite.layer == layer:
                    bg.blit(sprite.image, sprite.position)

            for projectile in projectiles:
                if projectile.layer == layer:
                    bg.blit(projectile.image, projectile.position)

            if problem != None:
                if problem.layer == layer:
                   bg.blit(problem.image, problem.position)

            if pause_menu != None:
                for obj in pause_menu:
                    if obj.layer == layer:
                        bg.blit(obj.image, obj.position)

        return bg

    def draw_gameover(background, level_objects, sprites, settings, menu_objects):
        bg = background
        for layer in settings.layers:
            for obj in level_objects:
                if obj.layer == layer:
                    bg.blit(obj.image, obj.position)

            for sprite in sprites:
                if sprite.layer == layer:
                    bg.blit(sprite.image, sprite.position)

            for obj in menu_objects:
                if obj.layer == layer:
                    bg.blit(obj.image, obj.position)

        return bg
