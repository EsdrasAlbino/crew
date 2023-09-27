from util.values_global import ITEM_SPACING_INVENTORY_X_Y, ITEM_SPACING_INVENTORY_ADD


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
        screen_width = surface.get_width()
        screen_height = surface.get_height()
        item_spacing = ITEM_SPACING_INVENTORY_X_Y
        position = [item_spacing, item_spacing]

        # Calculate the position for the top-right item
        top_right_x = screen_width - item_spacing - ITEM_SPACING_INVENTORY_ADD
        top_right_y = screen_height - item_spacing - ITEM_SPACING_INVENTORY_ADD

        for item in self.items:
            # if item == self.items[0]:  # First item goes to top-right
            #    item.draw(surface, (top_right_x, top_right_y))
            # elif item == self.items[1]:  # Second item goes to top-left
            #    item.draw(surface, position)
            # else:  # Other items go to the bottom
            item.draw(surface, position)
            position[0] += ITEM_SPACING_INVENTORY_ADD + item_spacing
            position[1] = ITEM_SPACING_INVENTORY_ADD + item_spacing

            if position[0] + ITEM_SPACING_INVENTORY_ADD >= screen_width:
                position[0] += ITEM_SPACING_INVENTORY_ADD + item_spacing
                position[1] += ITEM_SPACING_INVENTORY_ADD + item_spacing
