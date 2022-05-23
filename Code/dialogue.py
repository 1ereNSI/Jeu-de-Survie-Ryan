from re import T
from tkinter import E
import pygame
from map import *
from map import MapManager

class DialogBox:

    x_POSITION = 60
    y_POSITION = 470

    def __init__(self):
        self.box = pygame.image.load("dialog_box.png")
        self.box = pygame.transform.scale(self.box, (700, 100))
        self.texts = []
        self.text_index = 0
        self.letter_index = 1
        self.font = pygame.font.Font("dialog_font.ttf", 18)
        self.reading = False

    def execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog

    def render(self, screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box, (self.x_POSITION, self.y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0,0,0))
            screen.blit(text, (self.x_POSITION + 60, self.y_POSITION + 30))

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            #fermer le dialogue
            self.reading = False

    def afficher_stats(self, screen, hp, hp_max, points, score, score_max, damage):
        text_hp = self.font.render("Points de vie : " + str(hp) + " / " + str(hp_max), False, (250,0,0))
        screen.blit(text_hp, (10, 10))
        text_hp2 = self.font.render("(a pour améliorer et régénérer ses pv)", False, (250,0,0))
        screen.blit(text_hp2, (10, 30))
        text_damage = self.font.render("Damage : " + str(damage) + " (b pour améliorer ses dégâts)", False, (0,250,0))
        screen.blit(text_damage, (10, 70))
        text_points = self.font.render("Points de compétence : " + str(points), False, (0,0,250))
        screen.blit(text_points, (10, 110))
        text_score = self.font.render("Score : " + str(score), False, (0,0,0))
        screen.blit(text_score, (640, 10))
        text_score_max = self.font.render("Score max : " + str(score_max), False, (0,0,0))
        screen.blit(text_score_max, (591, 30))
