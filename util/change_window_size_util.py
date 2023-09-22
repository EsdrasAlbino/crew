import pygame


def change_window_size(
    screen, track_coords, player_coords, propellant_coords, bullet_coords, comet_coords
):
    window_dimensions = screen.get_size()
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

    player = pygame.image.load("assets/player.png")
    player_dimensions = (
        (track_coords[2] - track_coords[0]) / 5,
        31 * ((track_coords[2] - track_coords[0]) / 5) // 45,
    )
    player = pygame.transform.scale(player, player_dimensions)
    player_new_coords = (
        player_coords[0] + displacement_track,
        player_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    propellant = pygame.image.load("assets/propellant.png")
    propellant_dimensions = (320 * (track_coords[3] / 10) // 580, track_coords[3] / 10)
    propellant = pygame.transform.scale(propellant, propellant_dimensions)
    propellant_new_coords = (
        propellant_coords[0] + displacement_track,
        propellant_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    bullet = pygame.image.load("assets/bullet.png")
    bullet_dimensions = (14 * (track_coords[3] / 20) // 26, track_coords[3] / 20)
    bullet = pygame.transform.scale(bullet, bullet_dimensions)
    bullet_new_coords = (
        bullet_coords[0] + displacement_track,
        bullet_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    comet = pygame.image.load("assets/comet.png")
    comet_dimensions = (track_coords[3] // 10, (track_coords[3] // 10))
    comet = pygame.transform.scale(comet, comet_dimensions)
    comet = pygame.transform.rotozoom(comet, 45, 1)
    comet_new_coords = (
        comet_coords[0] + displacement_track,
        comet_coords[1] * proportion_height,
        None,
        None,
    )  # left, top, right, bottom

    return (
        track_coords,
        background,
        asteroid,
        asteroid_dimensions,
        asteroid_left_coord,
        player,
        player_dimensions,
        player_new_coords,
        propellant,
        propellant_dimensions,
        propellant_new_coords,
        bullet,
        bullet_dimensions,
        bullet_new_coords,
        comet,
        comet_dimensions,
        comet_new_coords,
    )
