import pygame
import pytmx
import pyscroll
from dialogue import *
from map import MapManager 
from player import Player

class Game:

    def __init__(self):

        #Demarrage
        self.running = True
        self.map = "world"

        # Création de la Fenêtre de jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Survival Game")

        # Generation du Joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        self.health = MapManager.attack_zombie

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:

            if pressed[pygame.K_RIGHT]:
                self.player.move_up_right()
            elif pressed[pygame.K_LEFT]:
                self.player.move_up_left()
            else:
                self.player.move_up()

        elif pressed[pygame.K_DOWN]:

            if pressed[pygame.K_RIGHT]:
                self.player.move_down_right()
            elif pressed[pygame.K_LEFT]:
                self.player.move_down_left()
            else:
                self.player.move_down()

        elif pressed[pygame.K_RIGHT]:

            if pressed[pygame.K_UP]:
                self.player.move_up_right()
            elif pressed[pygame.K_DOWN]:
                self.player.move_down_right()
            else:
                self.player.move_right()

        elif pressed[pygame.K_LEFT]:
            if pressed[pygame.K_UP]:
                self.player.move_up_left()
            elif pressed[pygame.K_DOWN]:
                self.player.move_down_left()
            else:
                self.player.move_left()

    def update(self):   
        self.map_manager.update()    

    def run(self):
        # Boucle du jeu
        fps = pygame.time.Clock()

        while self.running:
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.map_manager.all_monster.draw(self.screen)
            self.dialog_box.render(self.screen)
            self.dialog_box.afficher_stats(self.screen, self.map_manager.player_health, self.map_manager.player_health_max, self.map_manager.points_player, self.map_manager.score, self.map_manager.score_max, self.map_manager.player_damage)
            self.map_manager.check_zombie_damage()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
                    if event.key == pygame.K_a:
                        self.map_manager.up_health()
                    if event.key == pygame.K_b:
                        self.map_manager.up_damage()

            fps.tick(60)

        pygame.quit()