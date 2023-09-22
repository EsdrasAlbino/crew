import pygame
import sys
from entities.item_entity import Item
from entities.inventory_entity import Inventory


class Crew(object):
    def __init__(self):
        self.screen = None
        self.clock = None

    def init(self, screen_size=(800, 600)):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Crew')

        inventory = Inventory()

        # Add items to the inventory with custom positions
        item1 = Item("Item 1", (50, 50))
        item2 = Item("Item 2", (50, 350))
        # Add another "Item 1" to test quantity stacking
        item3 = Item("Item 3", (50, 500))
        item4 = Item("Item 4", (700, 450))
        item5 = Item("Item 5", (700, 50))
        inventory.add_item(item1)
        inventory.add_item(item2)
        inventory.add_item(item3)
        inventory.add_item(item4)
        inventory.add_item(item5)

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
