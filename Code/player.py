import pygame
from animation import *

class Entity(AnimateSprite):

    def __init__(self, name, x, y):
        super().__init__(name)

        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feets = pygame.Rect(0,0, self.rect.width / 2, 12)
        self.old_position = self.position.copy()

    def save_location(self): self.old_position = self.position.copy()


    def move_right(self): 
        self.change_animations("right")
        self.position[0] += self.speed
    def move_left(self): 
        self.change_animations("left")
        self.position[0] -= self.speed
    def move_up(self): 
        self.change_animations("up")
        self.position[1] -= self.speed
    def move_down(self): 
        self.change_animations("down")
        self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feets.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feets.midbottom = self.rect.midbottom

    def move_up_right(self): 
        self.change_animations("up")
        self.position[0] += self.speed
        self.position[1] -= self.speed

    def move_up_left(self): 
        self.change_animations("up")
        self.position[0] -= self.speed
        self.position[1] -= self.speed
    
    def move_down_right(self): 
        self.change_animations("down")
        self.position[0] += self.speed
        self.position[1] += self.speed
    
    def move_down_left(self): 
        self.change_animations("down")
        self.position[0] -= self.speed
        self.position[1] += self.speed


class Player(Entity):

    def __init__(self):
        super().__init__("player", 0, 0)
        

class NPC(Entity):

    def __init__(self, name, nb_points=0, dialog=[], health=150, damage=0, speed=0):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.current_point = 0
        self.zombie_health = health
        self.zombie_damage = damage
        self.zombie_speed = speed
        self.zombie_clock = 0
        self.zombie_old_position = [0, 0]

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_spawn")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)

