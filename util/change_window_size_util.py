import pygame

def change_window_size(screen, track_coord, player_left_coord, player_top_coord, propellant_left_coord, propellant_top_coord, bullet_left_coord, bullet_top_coord, comet_left_coord, comet_top_coord):
    window_dimensions = screen.get_size()
    track_coord_before = track_coord

    if window_dimensions[1] * 2 < window_dimensions[0]:
        track_left_coord = window_dimensions[0] // 2 - window_dimensions[1] // 2
        track_right_coord = track_left_coord + window_dimensions[1]
        track_bottom_coord = window_dimensions[1]
    else:
        track_left_coord = window_dimensions[0] // 4
        track_right_coord = 3 * window_dimensions[0] // 4
        track_bottom_coord = window_dimensions[0] // 2
    track_coord = (track_left_coord, 0, track_right_coord, track_bottom_coord)
    displacement_track = track_coord[0] - track_coord_before[0]
    proportion_height = (track_bottom_coord)/(track_coord_before[3])


    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, window_dimensions)

    asteroid = pygame.image.load("assets/asteroid.png")
    asteroid_dimensions = ((track_coord[2] - track_coord[0]) / 10, (track_coord[2] - track_coord[0]) / 10)
    asteroid_left_coord = track_coord[0] - asteroid_dimensions[0]
    asteroid = pygame.transform.scale(asteroid, asteroid_dimensions)

    player = pygame.image.load("assets/player.png")
    player_dimensions = ((track_coord[2] - track_coord[0]) / 5, 31 * ((track_coord[2] - track_coord[0]) / 5) // 45)
    player = pygame.transform.scale(player, player_dimensions)
    player_left_coord = player_left_coord + displacement_track
    player_top_coord = player_top_coord* proportion_height

    propellant = pygame.image.load("assets/propellant.png")
    propellant_dimensions = (320 * (track_coord[3] / 10) // 580, track_coord[3] / 10)
    propellant = pygame.transform.scale(propellant, propellant_dimensions)
    propellant_left_coord = propellant_left_coord +displacement_track
    propellant_top_coord = propellant_top_coord * proportion_height

    bullet = pygame.image.load("assets/bullet.png")
    bullet_dimensions = (14 * (track_coord[3] / 20) // 26, track_coord[3] / 20)
    bullet = pygame.transform.scale(bullet, bullet_dimensions)
    bullet_left_coord = bullet_left_coord + displacement_track
    bullet_top_coord = bullet_top_coord * proportion_height

    comet = pygame.image.load("assets/comet.png")
    comet_dimensions = (track_coord[3] // 10, (track_coord[3] // 10))
    comet = pygame.transform.scale(comet, comet_dimensions)
    comet = pygame.transform.rotozoom(comet, 45, 1)
    comet_left_coord = comet_left_coord + displacement_track
    comet_top_coord = comet_top_coord * proportion_height

    return track_coord, background, asteroid, asteroid_dimensions, asteroid_left_coord, player, player_dimensions, player_left_coord, player_top_coord, propellant, propellant_dimensions, propellant_left_coord, propellant_top_coord, bullet, bullet_dimensions, bullet_left_coord, bullet_top_coord, comet, comet_dimensions, comet_left_coord, comet_top_coord
