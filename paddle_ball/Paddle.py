import cv2


class Paddle:
    def __init__(self, initial_x=300, width=100):
        self.x = initial_x
        self.width = width
        self.y = 450  # Fixed y position for the paddle
        self.height = 10  # Fixed height for the paddle

    def update_position(self, new_x):
        self.x = new_x

    def get_rect(self):
        """Returns the paddle's bounding rectangle coordinates"""
        return (
            self.x - self.width // 2,  # left x
            self.y,                    # top y
            self.x + self.width // 2,  # right x
            self.y + self.height       # bottom y
        )

    def draw(self, canvas):
        cv2.rectangle(
            canvas,
            (self.x - self.width // 2, self.y),
            (self.x + self.width // 2, self.y + self.height),
            (255, 0, 0), -1
        )