import cv2
import threading
from EventBus import EventBus
from BlueBallDetector import BlueBallDetector
from PaddleBallGame import PaddleBallGame

def main():
    event_bus = EventBus()

    detector = BlueBallDetector(event_bus)
    game = PaddleBallGame(event_bus)

    detector_thread = threading.Thread(target=detector.run)
    detector_thread.daemon = True
    detector_thread.start()

    while True:
        game.update_game()
        game.draw()
        
        key = cv2.waitKey(30) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r') and game.game_over:
            game.reset_game()
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()