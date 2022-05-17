from dataclasses import dataclass
from tokenize import Name
from player import NPC
from player import *
import pygame, pytmx, pyscroll

@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str


@dataclass
class Map:
    name: str
    collisions: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]

class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.score = 0
        self.screen = screen
        self.player = player
        self.current_map = "carte"
        self.all_monster = pygame.sprite.Group()
        self.player_damage = 5

        self.all_boss = []

        self.boss = NPC("boss", nb_points = 1, damage=0.2, speed = 1)
        self.boss1 = NPC("boss2", nb_points = 1, damage=0.2, speed = 1)
        self.boss2 = NPC("boss2", nb_points = 1, damage=0.2, speed = 1)
        self.boss3 = NPC("boss3", nb_points = 1, damage=0.2, speed = 1)
        self.boss4 = NPC("boss4", nb_points = 1, damage=0.2, speed = 1)
        self.boss5 = NPC("boss5", nb_points = 1, damage=0.2, speed = 1)
        self.boss6 = NPC("boss6", nb_points = 1, damage=0.2, speed = 1)
        self.boss7 = NPC("boss7", nb_points = 1, damage=0.2, speed = 1)
        self.boss8 = NPC("boss8", nb_points = 1, damage=0.2, speed = 1)

        self.all_boss.append(self.boss)
        self.all_boss.append(self.boss1)
        self.all_boss.append(self.boss2)
        self.all_boss.append(self.boss3)
        self.all_boss.append(self.boss4)
        self.all_boss.append(self.boss5)
        self.all_boss.append(self.boss6)
        self.all_boss.append(self.boss7)
        self.all_boss.append(self.boss8)

        self.register_map("carte", portals = [
            Portal(from_world="carte", origin_point="enter_house",target_world = "house",teleport_point = "spawn_house"),   
            Portal(from_world="carte", origin_point="enter_zombie",target_world = "zombie",teleport_point = "spawn_zombie")
        ], npcs = [
            NPC("paul", nb_points = 1, dialog=["Tu vois ce trou ?", "Ne t'y approche pas trop, c'est dangeureux", "Va dans la maison"]),
            NPC("boss", nb_points = 1, dialog = ["Passe par ce chemin pour combattre les zombies", "Tu n'as pas besoin d'arme, les poings suffisent", "Ta vie ne se régénère pas, attention !", "Pour tuer les zombies, appuies sur a à proximité", "dès que tu as 5 points de compétences, appuies", "sur k pour augmenter tes dégâts !", "A chaque fois que vous êtes venu à bout", "d'une vague de zombies, ressortez de la map", "puis rerentrez-y."] )
        ])
        self.register_map("house", portals = [
            Portal(from_world="house", origin_point="exit_house",target_world = "carte",teleport_point = "enter_house_exit")
        ], npcs = [
            NPC("robin", nb_points = 1, dialog=["Nous sommes frappés par une invasion de zombies", "Dirige toi au nord et parle au zombie pacifiste"])
        ])
        self.register_map("zombie", portals = [
            Portal(from_world="zombie", origin_point="enter_carte",target_world = "carte",teleport_point = "spawn_carte")
        ], npcs = [self.boss, self.boss1, self.boss2, self.boss3, self.boss4, self.boss5, self.boss6, self.boss7, self.boss8
       ]
        )

        self.teleport_player("spawn")
        self.teleport_npcs()                
    
    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feets.colliderect(self.player.rect) and type(sprite) is NPC:
                if self.current_map == "carte" or self.current_map == "house":
                    dialog_box.execute(sprite.dialog)
                if self.current_map == "zombie":
                    self.attack_player(sprite.name)

    def attack_player(self, name_zombie=""):
        for boss in self.all_boss:
            if boss.name == name_zombie:
                boss.zombie_health -= self.player_damage
                print(boss.zombie_health)
            else:
                pass

    def check_collisions(self):
        #portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feets.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        #collisions
        for sprite in self.get_group().sprites():
            if sprite.feets.collidelist(self.get_collisions()) > -1:
                sprite.move_back()

            if type(sprite) is NPC:
                if sprite.feets.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 1

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[]):
        # Charger la Carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Définitions des zones de collisions

        collisions = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 4)
        group.add(self.player)

        #recuperer tous les npc et les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        # Creer un objet map
        self.maps[name] = Map(name, collisions, group, tmx_data, portals, npcs)
    
    def get_map(self): return self.maps[self.current_map]
    def get_group(self): return self.get_map().group
    def get_collisions(self): return self.get_map().collisions
    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()