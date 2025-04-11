import cv2
import numpy as np
from Paddle import Paddle
from Ball import Ball  # Assuming you saved the Ball class in Ball.py

class PaddleBallGame:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.ball = Ball()
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
            
        # Update ball and check for paddle hit
        paddle_hit = self.ball.update(self.paddle)
        if paddle_hit:
            self.score += 1

        # Check for game over condition
        if self.ball.check_bottom_collision(480):
            self.game_over = True

    def draw(self):
        self.canvas.fill(0)
        
        # Draw game elements
        self.ball.draw(self.canvas)
        self.paddle.draw(self.canvas)
        
        # Draw score
        cv2.putText(
            self.canvas, f"Score: {self.score}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
        )
        
        # Draw game over message if needed
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
        self.ball.reset()
        self.score = 0
        self.game_over = False
        self.paddle = Paddle()