import cv2
import numpy as np

class Ball:
    def __init__(self):
        self.pos = [300, 150]
        self.velocity = [6, 6]
        self.radius = 10
        self.color = (0, 0, 255)  # Red
    
    def update(self, paddle):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # Wall collisions
        if self.pos[0] <= 10 or self.pos[0] >= 630:
            self.velocity[0] *= -1

        if self.pos[1] <= 10:
            self.velocity[1] *= -1

        # Paddle collision
        paddle_left, paddle_top, paddle_right, paddle_bottom = paddle.get_rect()
        if (paddle_top <= self.pos[1] <= paddle_bottom and 
            paddle_left <= self.pos[0] <= paddle_right):
            self.velocity[1] *= -1
            return True  # Return True when paddle is hit
        
        return False  # Return False when no paddle hit
    
    def check_bottom_collision(self, height):
        return self.pos[1] >= height
    
    def draw(self, canvas):
        cv2.circle(canvas, tuple(self.pos), self.radius, self.color, -1)
    
    def reset(self):
        self.pos = [300, 150]
        self.velocity = [3, 3]