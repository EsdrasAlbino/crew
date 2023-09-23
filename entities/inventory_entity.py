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
        item_spacing = 20
        x, y = item_spacing, item_spacing

        # Calculate the position for the top-right item
        top_right_x = screen_width - item_spacing - 70
        top_right_y = item_spacing

        for item in self.items:
            if item == self.items[0]:  # First item goes to top-right
                item.draw(surface, top_right_x, top_right_y)
            elif item == self.items[1]:  # Second item goes to top-left
                item.draw(surface, item_spacing, item_spacing)
            else:  # Other items go to the bottom
                item.draw(surface, x, y)
                x += 70 + item_spacing
                if x + 70 >= screen_width:
                    x = item_spacing
                    y += 70 + item_spacing
