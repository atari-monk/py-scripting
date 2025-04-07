import cv2
import numpy as np
from Paddle import Paddle

class PaddleBallGame:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.ball_pos = [300, 150]
        self.ball_velocity = [3, 3]
        self.score = 0
        self.game_over = False
        self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        self.paddle = Paddle()
        
        self.event_bus.subscribe("blue_ball_position", self.update_paddle)

    def update_paddle(self, blue_ball_pos):
        if blue_ball_pos:
            self.paddle.update_position(blue_ball_pos[0])

    def update_game(self):
        if self.game_over:
            return
            
        self.ball_pos[0] += self.ball_velocity[0]
        self.ball_pos[1] += self.ball_velocity[1]

        if self.ball_pos[0] <= 10 or self.ball_pos[0] >= 630:
            self.ball_velocity[0] *= -1

        if self.ball_pos[1] <= 10:
            self.ball_velocity[1] *= -1

        paddle_left, paddle_top, paddle_right, paddle_bottom = self.paddle.get_rect()
        if (paddle_top <= self.ball_pos[1] <= paddle_bottom and 
            paddle_left <= self.ball_pos[0] <= paddle_right):
            self.ball_velocity[1] *= -1
            self.score += 1

        if self.ball_pos[1] >= 480:
            self.game_over = True

    def draw(self):
        self.canvas.fill(0)
        
        cv2.circle(self.canvas, tuple(self.ball_pos), 10, (0, 0, 255), -1)
        self.paddle.draw(self.canvas)
        
        cv2.putText(
            self.canvas, f"Score: {self.score}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
        )
        
        if self.game_over:
            cv2.putText(
                self.canvas, "GAME OVER", (200, 240),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3
            )
            cv2.putText(
                self.canvas, "Press 'R' to restart", (200, 280),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2
            )
        
        cv2.imshow("Paddle Ball Game", self.canvas)

    def reset_game(self):
        self.ball_pos = [300, 150]
        self.ball_velocity = [3, 3]
        self.score = 0
        self.game_over = False
        self.paddle = Paddle()