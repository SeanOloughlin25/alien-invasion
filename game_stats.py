from pathlib import Path
import json


class GameStats:
    """Track Statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize Statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # open all time high score
        self.load_all_time_high_score()
        # high score should never be reset
        self.high_score = self.high_score if self.high_score else 0
            
    
    def reset_stats(self):
        """Initialize Statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_all_time_high_score(self):
        """Load the high score from a file if it exist"""
        path = Path("high_score.json")
        if path.exists():
            contents = path.read_text()
            self.high_score = json.loads(contents)
        else:
            self.high_score = 0
            # create the file with the intial high score
            self.all_time_high_score()


    def all_time_high_score(self):
        """save high score"""
        path = Path("high_score.json")
        contents = json.dumps(self.high_score)
        path.write_text(contents)

        



    
