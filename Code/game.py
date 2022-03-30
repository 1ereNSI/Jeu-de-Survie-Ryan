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

        # Définitions des zones de collisions

        self.collisions = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 5)
        self.group.add(self.player)
    
    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:

            if pressed[pygame.K_RIGHT]:
                self.player.move_up_right()
            elif pressed[pygame.K_LEFT]:
                self.player.move_up_left()
            else:
                self.player.move_up()
            
            self.player.change_animations("up")

        elif pressed[pygame.K_DOWN]:

            if pressed[pygame.K_RIGHT]:
                self.player.move_down_right()
            elif pressed[pygame.K_LEFT]:
                self.player.move_down_left()
            else:
                self.player.move_down()

            self.player.change_animations("down")

        elif pressed[pygame.K_RIGHT]:

            if pressed[pygame.K_UP]:
                self.player.move_up_right()
            elif pressed[pygame.K_DOWN]:
                self.player.move_down_right()
            else:
                self.player.move_right()

            self.player.change_animations("right")

        elif pressed[pygame.K_LEFT]:
            if pressed[pygame.K_UP]:
                self.player.move_up_left()
            elif pressed[pygame.K_DOWN]:
                self.player.move_down_left()
            else:
                self.player.move_left()

            self.player.change_animations("left")

    def update(self):
        self.group.update()

        # Veritications collisions
        for sprite in self.group.sprites():
            if sprite.feets.collidelist(self.collisions) > -1:
                sprite.move_back()

    def run(self):
        # Boucle du jeu
        fps = pygame.time.Clock()
        running = True

        while running:
            
            self.player.save_location()

            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            fps.tick(60)

        pygame.quit()