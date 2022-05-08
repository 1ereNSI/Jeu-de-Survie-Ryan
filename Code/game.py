import pygame
import pytmx
import pyscroll 
from player import Player

class Game:

    def __init__(self):

        #Demarrage
        self.running = True
        self.map = "world"

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

        # Défininir les rect pour entrer dans la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)


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

    def switch_house(self):
        self.map = "house"

        # Charger la Carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('house.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Définitions des zones de collisions

        self.collisions = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 5)
        self.group.add(self.player)

        # Défininir les rect pour entrer dans la maison
        enter_house = tmx_data.get_object_by_name("exit_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # recuperer le point de spawn dans la maison 
        spawn_house_point = tmx_data.get_object_by_name("spawn_house")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        self.map = "world"

        # Charger la Carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Définitions des zones de collisions

        self.collisions = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 5)
        self.group.add(self.player)

        # Défininir les rect pour sortir de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # recuperer le point de spawn devant la maison 
        spawn_house_point = tmx_data.get_object_by_name("enter_house_exit")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y

    def update(self):   
        self.group.update()

        # Verification entree dans la maison
        if self.map == "world" and self.player.feets.colliderect(self.enter_house_rect):
            self.switch_house()

        # Verification sortie de la maison
        if self.map == "house" and self.player.feets.colliderect(self.enter_house_rect):
            self.switch_world()
        

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