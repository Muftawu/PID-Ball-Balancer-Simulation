import pygame 
from ball import Ball
from settings import *
from utils import * 

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()
FPS = 60

# ball coordinates
BALL_X, BALL_Y = 300, 450

font = pygame.font.SysFont('', 32)

def display_text(data, x, y, color):
    text = font.render(data, True, color)
    win.blit(text, (x,y))

def platform_center():
    pygame.draw.circle(win, 'white', PLATFORM_CENTER, 40, width=1)
    pygame.draw.circle(win, 'red', PLATFORM_CENTER, PLATFORM_CENTER_RADIUS)

def main():
    run = True
    balls = []

    for i in range(NUM_BALLS):
        # ball = Ball(win, BALL_X, BALL_Y, BALL_RADIUS)
        ball = Ball(win, random_ball_points(WIDTH, HEIGHT)[0], random_ball_points(WIDTH, HEIGHT)[1], BALL_RADIUS)
        balls.append(ball)

    while run:
        win.fill('black')
        clock.tick(FPS)

        platform_center()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for ball in balls:
            ball.draw()        
            ball.manual_mode()
            display_text(f"PID BALL BALANCER", TEXT_X, TEXT_Y, 'RED')
            ball.pid_output_control_X(*PLATFORM_CENTER)
            ball.pid_output_control_Y(*PLATFORM_CENTER)

        pygame.display.update()

if __name__ == "__main__":
    main()