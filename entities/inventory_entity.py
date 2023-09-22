import pygame


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Check if the item is already in the inventory
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += 1
                return
        self.items.append(item)

    def draw(self, surface):
        for item in self.items:
            item.draw(surface)
