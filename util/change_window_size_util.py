import pygame

def update_window(screen):
    return screen.get_size()

def change_window_size(
    screen, track_coords, player_coords, propellant_coords, bullet_coords, comet_coords
):
    window_dimensions = update_window(screen)
    track_coords_before = track_coords

    if window_dimensions[1] * 2 < window_dimensions[0]:
        track_left_coord = window_dimensions[0] // 2 - window_dimensions[1] // 2
        track_right_coord = track_left_coord + window_dimensions[1]
        track_bottom_coord = window_dimensions[1]
    else:
        track_left_coord = window_dimensions[0] // 4
        track_right_coord = 3 * window_dimensions[0] // 4
        track_bottom_coord = window_dimensions[0] // 2

    track_coords = (
        track_left_coord,
        None,
        track_right_coord,
        track_bottom_coord,
    )  # left, top, right, bottom

    displacement_track = track_coords[0] - track_coords_before[0]
    proportion_height = (track_coords[3]) / (track_coords_before[3])

    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, window_dimensions)

    asteroid = pygame.image.load("assets/asteroid.png")
    asteroid_dimensions = (
        (track_coords[2] - track_coords[0]) / 10,
        (track_coords[2] - track_coords[0]) / 10,
    )
    asteroid_left_coord = track_coords[0] - asteroid_dimensions[0]
    asteroid = pygame.transform.scale(asteroid, asteroid_dimensions)

    player_dimensions = (
        (track_coords[2] - track_coords[0]) / 10,
        31 * ((track_coords[2] - track_coords[0]) / 10) // 45,
    )
    player_new_coords = (
        player_coords[0] + displacement_track,
        player_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    propellant_dimensions = (320 * (track_coords[3] / 12) // 580, track_coords[3] / 12)
    propellant_new_coords = (
        propellant_coords[0] + displacement_track,
        propellant_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    bullet_dimensions = (14 * (track_coords[3] / 24) // 26, track_coords[3] / 24)
    bullet_new_coords = (
        bullet_coords[0] + displacement_track,
        bullet_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    comet_dimensions = (track_coords[3] // 14, (track_coords[3] // 7))
    comet_new_coords = (
        comet_coords[0] + displacement_track,
        comet_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    return (
        window_dimensions,
        track_coords,
        background,
        asteroid,
        asteroid_dimensions,
        asteroid_left_coord,
        player_dimensions,
        player_new_coords,
        propellant_dimensions,
        propellant_new_coords,
        bullet_dimensions,
        bullet_new_coords,
        comet_dimensions,
        comet_new_coords,
        proportion_height,
    )
