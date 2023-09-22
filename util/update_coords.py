def update_coords(old_coords, new_coords):
    return (
        new_coords[0] if new_coords[0] != None else old_coords[0],
        new_coords[1] if new_coords[1] != None else old_coords[1],
        new_coords[2] if new_coords[2] != None else old_coords[2],
        new_coords[3] if new_coords[3] != None else old_coords[3],
    )
