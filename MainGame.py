import pygame, os, sys
import contextlib

with contextlib.redirect_stdout(None):
    import pygame
pygame.init()
pygame.font.init()
# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
FPS = 60

# Colors
BLACK = (23, 23, 23)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Fonts
SCORE_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

# Object Parameters
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 100
BALL_WIDTH, BALL_HEIGHT = 10, 10
VEL = 20
BALL_VEL = 4


def draw_window(red, blue, ball, red_score, blue_score):
    WIN.fill(BLACK)
    red_score_text = SCORE_FONT.render("Score: " + str(red_score), 1, WHITE)
    blue_score_text = SCORE_FONT.render("Score: " + str(blue_score), 1, WHITE)
    WIN.blit(red_score_text, (10, 10))
    WIN.blit(blue_score_text, (WIDTH - red_score_text.get_width() - 20, 10))
    pygame.draw.rect(WIN, RED, red)
    pygame.draw.rect(WIN, BLUE, blue)
    pygame.draw.rect(WIN, WHITE, ball)
    pygame.display.update()


def red_movement(red, keys_pressed):
    if keys_pressed[pygame.K_w] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + red.height + VEL < HEIGHT:
        red.y += VEL


def blue_movement(blue, keys_pressed):
    if keys_pressed[pygame.K_i] and blue.y - VEL > 0:
        blue.y -= VEL
    if keys_pressed[pygame.K_k] and blue.y + blue.height + VEL < HEIGHT:
        blue.y += VEL


def reset_ball_movement(ball):
    ball.x = 445
    ball.y = 225


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(
        draw_text,
        (
            WIDTH // 2 - draw_text.get_width() // 2,
            HEIGHT // 2 - draw_text.get_height() // 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    # Defining Objects
    red = pygame.Rect(50, 225, PLAYER_WIDTH, PLAYER_HEIGHT)
    blue = pygame.Rect(850, 225, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(445, 245, BALL_WIDTH, BALL_HEIGHT)
    BALL_X, BALL_Y = 1, 1
    # Points
    red_score = 0
    blue_score = 0
    MAXSCORE = 10
    # Setting Clock
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # Setting fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            keys_pressed = pygame.key.get_pressed()
            red_movement(red, keys_pressed)
            blue_movement(blue, keys_pressed)

        ball.x += BALL_VEL * BALL_X
        ball.y += BALL_VEL * BALL_Y
        if ball.y + BALL_VEL + ball.height > 490:
            BALL_Y = -1
        if ball.y + BALL_VEL + ball.height < 0:
            BALL_Y = 1
        if red.colliderect(ball):
            BALL_X = 1
        if blue.colliderect(ball):
            BALL_X = -1
        if ball.x > blue.width + blue.x:
            red_score += 1
            reset_ball_movement(ball)
        if ball.x < red.x:
            blue_score += 1
            reset_ball_movement(ball)

        winner_text = ""
        if red_score == MAXSCORE:
            winner_text = "RED WINS!"
            draw_winner(winner_text)
            break

        if blue_score == MAXSCORE:
            winner_text = "BLUE WINS!"
            draw_winner(winner_text)
            break

        draw_window(red, blue, ball, red_score, blue_score)

    main()


if __name__ == "__main__":
    main()
