import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shooting Game')

# Set up assets
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (150, 150))  # Increase player size

bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (20, 40))  # Increase bullet size

target_img = pygame.image.load('target.png')
target_img = pygame.transform.scale(target_img, (100, 100))  # Increase target size

# Load sound effects
shoot_sound = pygame.mixer.Sound('shoot.wav')
hit_sound = pygame.mixer.Sound('hit.wav')
lose_life_sound = pygame.mixer.Sound('lose_life.wav')

# Set up game variables
player_x = width // 2
player_y = height - 150  # Adjusted for the new player size
player_speed = 5

bullets = []
bullet_speed = 7
max_bullets = 1

targets = []
target_speed = 2
target_spawn_rate = 30
max_targets = 5

score = 0
lives = 3
game_over = False

# Set up fonts
font = pygame.font.SysFont(None, 55)
game_over_font = pygame.font.SysFont(None, 75)

# Helper functions
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def show_game_over():
    window.fill((0, 0, 0))
    draw_text('GAME OVER', game_over_font, (255, 0, 0), window, width // 3, height // 3)
    draw_text(f'Score: {score}', game_over_font, (255, 255, 255), window, width // 3, height // 2)
    pygame.display.update()
    pygame.time.delay(3000)

# Main game loop
running = True
while running:
    window.fill((211, 211, 211))  # Fill the screen with black
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        show_game_over()
        running = False
        continue

    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < width - 150:
        player_x += player_speed

    # Shoot bullets
    if keys[pygame.K_SPACE] and len(bullets) < max_bullets:
        bullets.append([player_x + 65, player_y - 40])  # Adjusted for new player size
        shoot_sound.play()

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn targets
    if len(targets) < max_targets and random.randint(1, target_spawn_rate) == 1:
        targets.append([random.randint(0, width-100), 0])

    # Move targets
    for target in targets:
        target[1] += target_speed
        if target[1] > height:
            targets.remove(target)
            lives -= 1
            lose_life_sound.play()
            if lives == 0:
                game_over = True

    # Check for collisions
    for bullet in bullets:
        for target in targets:
            if bullet[0] in range(target[0], target[0] + 100) and bullet[1] in range(target[1], target[1] + 100):
                bullets.remove(bullet)
                targets.remove(target)
                hit_sound.play()
                score += 1
                break

    # Draw player
    window.blit(player_img, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        window.blit(bullet_img, pygame.Rect(bullet[0], bullet[1], 20, 40))

    # Draw targets
    for target in targets:
        window.blit(target_img, pygame.Rect(target[0], target[1], 100, 100))

    # Draw score
    draw_text(f'Score: {score}', font, (255, 255, 255), window, 10, 10)
    draw_text(f'Lives: {lives}', font, (255, 255, 255), window, width - 150, 10)

    # Update display
    pygame.display.update()

# Quit the game
pygame.quit()
