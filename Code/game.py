import pygame
import pytmx
import pyscroll 
from player import Player

class Game:

    def __init__(self):
        # Création de la Fenêtre de jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Survival Game")
        
        # Charger la Carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Generation du Joueur
        player_position = tmx_data.get_object_by_name("first_spawn")
        self.player = Player(player_position.x, player_position.y)

        # Dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 3)
        self.group.add(self.player)
    
    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()

        elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
            self.player.move_up_right
        elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
            self.player.move_up_left
        elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
            self.player.move_down_right
        elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
            self.player.move_down_left


    def run(self):
        # Boucle du jeu
        running = True

        while running:

            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()