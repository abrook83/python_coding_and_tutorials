class Settings:
    """ A class to store all the game's settings """

    def __init__(self):
        """ initialise the game's settings """
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 95, 135)     

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15        
        self.bullet_colour = (255,183,75)
        self.bullets_allowed = 3