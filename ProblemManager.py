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

#Denna klass hanterar matte problemen.
#Endast enkla problem finns pga. att mållgruppen var barn som inte har
#börjat skolan ännu. Tanken är att spelaren ska lära sig känna igen siffror.

import pygame
from EasyProblem import EasyProblem

class ProblemManager(object):
    def __init__(self, settings):
        super().__init__()
        self.__settings = settings
        self.__font = self.__settings.problem_font
        self.__problem_pos = self.__settings.problem_position
        self.__problems = list()
        self.__problems.append(self.__easy_problem())
        self.__problems.append(self.__easy_problem())
        self.__problems.append(self.__easy_problem())
        self.__problems.append(self.__easy_problem())
        self.__problems.append(self.__easy_problem())
        self.__problems[0].current_problem = True
        self.__fails = -1
        self.__solved = -1
        self.__cp_index()
        self.__all_solved = False

    def update(self, number):
        self.__all_solved = self.__check_win()
        if number != None:
            self.__check_number(number)
                
        
    def __check_win(self):
        for problem in self.__problems:
            if problem.solved == False:
                return False

        return True
        
    def __easy_problem(self):
        return EasyProblem(self.__problem_pos, self.__settings.problem_names[0],
                           self.__settings.problem_layer, self.__font,
                           self.__settings.problem_size)

    def __check_number(self, number):
        if self.problem != None:
            if number == self.problem.number:
                self.__solved += 1
                self.problem.solved = True
                if self.__cp_index() < len(self.__problems) - 1:
                    self.__problems[self.__cp_index() + 1].current_problem = True
                self.__problems[self.__cp_index()].current_problem = False
                
            elif number != self.problem.number:
                self.__fails += 1

    def __cp_index(self):
        for problem in self.__problems:
            if problem.current_problem:
                return self.__problems.index(problem)

    @property
    def fails(self):
        return self.__fails

    @property
    def solved(self):
        return self.__solved

    @property
    def problem(self):
        for problem in self.__problems:
            if problem.current_problem:
                return problem

        return None
