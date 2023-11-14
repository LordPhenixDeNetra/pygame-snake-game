import pygame
import time
import random

pygame.init()

# Paramètres du jeu
width, height = 800, 600
snake_size = 20
speed = 9

# Couleurs
black = (0, 0, 0)
white = (0, 0, 255)
red = (255, 0, 0)

# Initialisation de la fenêtre
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Police pour l'affichage du score
font = pygame.font.SysFont(None, 35)


# Fonction principale du jeu
def game_loop():
    game_over = False
    game_close = False

    # Initialisation du serpent
    snake_list = []
    length_of_snake = 1

    # Position initiale du serpent
    snake_head = [width / 2, height / 2]
    snake_list.append(snake_head)

    # Direction initiale du serpent
    direction = 'RIGHT'
    change_to = direction

    # Position initiale de la pomme
    apple_pos = [random.randrange(1, (width // snake_size)) * snake_size,
                 random.randrange(1, (height // snake_size)) * snake_size]

    while not game_over:

        while game_close:
            game_display.fill(black)
            # Affichage du score
            score = length_of_snake - 1
            score_text = font.render(f'Score: {score}', True, white)
            game_display.blit(score_text, [width / 3, height / 3])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'

        # Met à jour la direction du serpent
        direction = change_to

        # Met à jour la position de la tête du serpent en fonction de la direction
        if direction == 'RIGHT':
            snake_head[0] += snake_size
        elif direction == 'LEFT':
            snake_head[0] -= snake_size
        elif direction == 'UP':
            snake_head[1] -= snake_size
        elif direction == 'DOWN':
            snake_head[1] += snake_size

        # Vérifie les collisions avec les bords de l'écran
        if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
            game_close = True

        # Vérifie les collisions avec le corps du serpent
        for segment in snake_list[1:]:
            if segment == snake_head:
                game_close = True

        # Ajoute la nouvelle tête du serpent à la liste du serpent
        snake_list.append(list(snake_head))

        # Supprime la queue du serpent si la longueur dépasse
        while len(snake_list) > length_of_snake:
            del snake_list[0]

        # Dessine le fond de l'écran
        game_display.fill(black)

        # Dessine le serpent
        for segment in snake_list:
            pygame.draw.rect(game_display, white, [segment[0], segment[1], snake_size, snake_size])

        # Dessine la pomme
        pygame.draw.rect(game_display, red, [apple_pos[0], apple_pos[1], snake_size, snake_size])

        # Met à jour l'écran
        pygame.display.flip()

        # Vérifie si la tête du serpent atteint la position de la pomme
        if snake_head == apple_pos:
            # Génère une nouvelle position pour la pomme
            apple_pos = [random.randrange(1, (width // snake_size)) * snake_size,
                         random.randrange(1, (height // snake_size)) * snake_size]
            # Augmente la longueur du serpent
            length_of_snake += 1

        # Règle la vitesse du jeu
        clock.tick(speed)

    pygame.quit()
    quit()


# Lance le jeu
game_loop()
