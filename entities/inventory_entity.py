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

    def draw(self, surface, track_coord):
        screen_width = surface.get_width()
        screen_height = surface.get_height()
        ITEM_SPACING_INVENTORY_X_Y = (track_coord[2] - track_coord[0])/20
        ITEM_SPACING_INVENTORY_ADD = ITEM_SPACING_INVENTORY_X_Y
        item_spacing = ITEM_SPACING_INVENTORY_X_Y*2
        # position = [item_spacing, item_spacing]

        # Calculate the position for the top-right item
        top_right_x = (track_coord[2]-track_coord[0])//7 + track_coord[2]
        top_right_y = track_coord[3]*8/9
        position = [top_right_x, top_right_y]

        for item in self.items:
            # if item == self.items[0]:  # First item goes to top-right
            #    item.draw(surface, (top_right_x, top_right_y))
            # elif item == self.items[1]:  # Second item goes to top-left
            #    item.draw(surface, position)
            # else:  # Other items go to the bottom
            item.draw(surface, position)
            position[1] -= ITEM_SPACING_INVENTORY_ADD + item_spacing
           # position[1] = ITEM_SPACING_INVENTORY_ADD + item_spacing

            if position[0] + ITEM_SPACING_INVENTORY_ADD >= screen_width:
                position[0] += ITEM_SPACING_INVENTORY_ADD + item_spacing
                position[1] += ITEM_SPACING_INVENTORY_ADD + item_spacing
