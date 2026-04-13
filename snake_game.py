import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enhanced Snake Game")

# Game variables
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
score = 0
clock = pygame.time.Clock()

# Game loop
def game_loop():
    global snake_direction, score, food_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    snake_direction = 'RIGHT'

        # Move the snake
        if snake_direction == 'UP':
            snake_pos[0][1] -= 10
        elif snake_direction == 'DOWN':
            snake_pos[0][1] += 10
        elif snake_direction == 'LEFT':
            snake_pos[0][0] -= 10
        elif snake_direction == 'RIGHT':
            snake_pos[0][0] += 10
        
        # Check for food collision
        if snake_pos[0] == food_pos:
            score += 1
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
            snake_pos.append(snake_pos[-1][:])
        
        # Drawing
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(snake_pos[0][0], snake_pos[0][1], 10, 10))
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        for pos in snake_pos[1:]:
            pygame.draw.rect(win, (0, 200, 0), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.display.flip()
        clock.tick(10)

# Start the game loop
if __name__ == "__main__":
    game_loop()