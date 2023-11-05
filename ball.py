import pygame 
import math 
from settings import *

pygame.init()

class Ball:
    def __init__(self, win, x, y, radius):
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.win = win 
        
        # PID Constants
        self.K_p = 0.04
        self.K_i = 0.04
        self.K_d = 0.10

    def draw(self):
        pygame.draw.circle(self.win, 'blue', (self.x, self.y), self.radius)
        pygame.draw.line(self.win, 'orange', (self.x, self.y), PLATFORM_CENTER)      

    def pid_output_control_X(self, x2, y2):
        # PID output X+
        error = math.sqrt((self.x-x2)**2 + (self.y-y2)**2)
        p_error = self.K_p*error
        i_error = self.K_i*error
        d_error = self.K_d*error

        # error correction in positive 'X' direction
        output_x1 = p_error + i_error +  d_error
        self.x += output_x1

        # PID output X-
        error = math.sqrt((self.x-x2)**2 + (self.y-y2)**2)
        p_error = self.K_p*error
        i_error = self.K_i*error
        d_error = self.K_d*error

        # error correction in negative 'X' direction
        output_x2 = p_error + i_error +  d_error
        self.x -= output_x2

        print("Error correction:", int(self.x))

    def pid_output_control_Y(self, x2, y2):
        # PID output Y-
        error = math.sqrt((self.x-x2)**2 + (self.y-y2)**2)
        p_error = self.K_p*error
        i_error = self.K_i*error
        d_error = self.K_d*error

        # error correction in negative 'Y' direction
        output_x1 = p_error + i_error +  d_error
        self.y += output_x1

        # PID output Y+
        error = math.sqrt((self.x-x2)**2 + (self.y-y2)**2)
        p_error = self.K_p*error
        i_error = self.K_i*error
        d_error = self.K_d*error

        # error correction in positive 'Y' direction
        output_x2 = p_error + i_error +  d_error
        self.y -= output_x2

        print(int(self.x))

    
    
    def manual_mode(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.x += BALL_SPEED_HORZ
        if keys_pressed[pygame.K_LEFT]:
            self.x -= BALL_SPEED_HORZ
        if keys_pressed[pygame.K_UP]:
            self.y -= BALL_SPEED_HORZ
        if keys_pressed[pygame.K_DOWN]:
            self.y += BALL_SPEED_HORZ
