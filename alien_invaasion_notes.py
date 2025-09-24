"""When Making a game, First start with a description of what the games about"""
    # In alien invasion, one player controls a rocket ship that appears at the
    # bottom center of the screen. The player can move the ship right or left
    # using the arrow keys and shoot bullets using the spacebar.
    # When the game begins, a fleet of aliens fill the sky and moves across
    # and down the screen. The player shoots and destroys the aliens.
    # If the player destroys all the aliens, a new fleet appears that moves
    # faster than the previous fleet. If any alien hits the players ship or 
    # reaches the bottom of the screen, the players loses a ship. 
    # if the player loses three ships, the game ends.

# Where to start
    # First make a ship that can move left or right by using the arrow keys
    # can shoot by pressing the space bar

# Install Pygame
    # $ python -m pip install --user pygame
    # or pip3 install pygame

# creat a new file in Alien Invasion Folder called alien_invasion
    # we'll use this to create a pygame window and a class that represents the 
    # game
# first steps
    # Creat Pygame Window and Responding to User Input
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1700, 900))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            # Watch for keyword and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()

# Second Step
# Controlling the Frame Rate

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1700, 900))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock() # ADD CLOCK IN INIT SECTION

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            # Watch for keyword and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60) # ADD TICK TO SET THE ONE ARGUMENT FOR FR

if __name__ == '__main__':
    # Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()
    
# Setting the background color

import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1700, 900))
        pygame.display.set_caption("Alien Invasion")
        # set clock for framerate
        self.clock = pygame.time.Clock()
        # set backgound color
        self.bg_color = (230, 230, 230)#*******

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            # Watch for keyword and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through loop
            self.screen.fill(self.bg_color)#********

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()

# Creating a Setting Class
    # instead of adding settings throughout the code,
    # we'll make a module called settings that will contain a class
    # called Settings
        # having this in a mod will make it easier to adjust as our project grows
        # heres both Classes

# Settings

class Settings:
    """A Class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the games settings"""
        # Screen Settings
        self.screen_width = 1700
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

# Updated Alien Invasion

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        # set clock for framerate
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            # Watch for keyword and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

# Upload image for game

# to do so we use the pygame method blit()
# pay attention to licensing
# cheapest way to start is using freely licensed graphics from a website like
    # opengameart.org
    # you can use any file type but will have to convert
    # use bitmap (.bmp) this is pygames default
    # for AI we'' use the books recomendation ship.bmp

# Creating a ship Class

import pygame

class Ship:
    """A Class to Manage the Ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

# Updated ai class

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        # set clock for framerate
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self) # call ship. one arg instance in AI

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            # Watch for keyword and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() # Draw ship to screen using blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make game instance and run game.
    ai = AlienInvasion()
    ai.run_game()

# Refactoring: the_check_events() and _update_screen() Methods
    # restructures the code youve already written
    # making it easier to build on

    # Now we'll break the run game method into two sections to avoid its
    # already length build

    # Helper method: does work inside a class but isnt meant to be used by
    # code outside.  These methods are identified by a single leading underscore

# The _check_events() Method:
    # We'll move the code that manages events to a seperate method called 
    # _check_events()
    # Isolating this will allow us to manage events seperatly from 
    # other aspects of the game

# updated methods
        def run_game(self):
        """Starts the main loop for game"""
        while True:
            self._check_events()

            # Redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyword and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# The _update_screen() Method:
    # To further simplify our code we'll move the code for updateing the screen
    # to a seperate method called _ipdate_screen()
        # SO MUCH CLEANERRRRRRR
    def run_game(self):
        """Starts the main loop for game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyword and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on screen, and flip to a new screen"""
        # Redraw the screen during each pass through loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Piloting the Ship
    # First we'll apply code to move the ship to right
    # Then use the same principles to move ship to left
    # Using right and left arrows

    # Responding to a Keypress
    # whenever a player presses a key, that keypress is registered as an event
    # each event is picked up by the pygame.event.get() method
    # We have to sepcify in our _check events() what kind of events we want
    # the game to check for 
    # Thats where the KEYDOWN function comes in
    # FOr instance, when a player presses the right arrow
    # we want our ships rect.x value to move the ship to the right

def _check_events(self):
    """Watch for keyword and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    elif event.type == pygame.KEYDOWN: # Use KEYDOWN to detect user input
        if event.key == pygame.K_RIGHT: # If he pushes right key
        # move the ship to right
            self.ship.rect.x += 1    # Ship moves to right by 1 rect

# Allowing Continuous Movement 
    # We dont want the ship to move over just once
    # we want the user to be able to hold the right key and have our ship move
    # until he stops holding the right key
    # We'll use KEYUP and KEYDOWN events to make this happen
    # All attribues of ship will be added to the Ship class

class Ship:
    """A Class to Manage the Ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement Flag: start with a ship thats not moving
        self.moving_right = False
    # update movement
    def update(self):
        """Update the ships position based on the movement Flag"""
        if self.moving_right:
            self.rect.x += 1
        

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    # Now we need to update _check_events() so that moving_right is True
    # when player presses right key and False when that key is release
    # This will be implemented in the run_game() method in AI

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            self._check_events()
            self.ship.update()# thats it!
            self._update_screen()
            self.clock.tick(60)

     def _check_events(self):
        """Watch for keyword and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Updated to recognize if key is pressed down or release
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

# Movig Both Left and Right Key 
    # Since we already moved right, moving left is straight forward
    # instead of x+=1 it will be x-=1 in ship class
     # Movement Flag: start with a ship thats not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement Flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    # And we have to make two additions to the check_events() secion in AI
            elif event.type == pygame.KEYDOWN: # only once for left and right
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: # only once for left and right 
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

# Adjusting the ships speed
    # we'll adjust how fast we can move the ship
    # and will also make it so out ship cant fly off course and out of our window

    # Speed
    # Currently our ship is moving one pixel per cycle through our while loop
    # we can take for control over this by adding ship_speed attribute to our 
    # settings class

    self.screen_width = 1700
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # we used a float for more control
        # .5 more doesnt seem like much but we can adjust the tempo of the game 
        # later
        # our ship only takes in integers as of now
        # so lets make some adjustments there

        # Store a float for the new ships exact horizontal position.
        self.x = float(self.rect.x)
    
         def update(self):
        """Update the ships position based on the movement Flag"""
        # Update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
    
# Limiting the Ships Range
    # When moving the ship left or right youll notice the ship will fly off the
    # scren
    # Wh can make the ship stop once it hits the edge of the screen by modifying 
    # the update method in Ship
    # if ship rect is less than 0 it hasnt hit the right edge of the screen
    # if ship rect is greater than 0 it hasnt hit the left edge of the screen

if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

# Refactoring _check_events()
    # this method will become bigger the deeper we get into the game development
    # Lets break up the KEYDOWN and KEYUP events

    # we two new helper method, _check_keyup and _check_keydown
    # each take in parameter self, event
    # replace old code with calls to the new methods
    # cleaner structure and gives us more room to ad to payer input 

    def _check_events(self):
        """Watch for keyword and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Responds to ey release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


# Pressing Q to Quit 
    # It can get tedious to click the x on the top of the screen
    # since we are more efficiant with our key presses we'll make another shortcut
    # wright a code so that when a player presses Q the game will exit

    # in the key_down helper method add an event.key to quit the game

def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

# Running the game in Full Screen Mode
    # Some people or systems may prefer to play a game in full screen mode
    # To make this possible we'll make some adjustments to the __init__ section

    # when creating the full screen we pass a size in (0, 0)
    # this tells python to figure out the screen size
    # we use wideth and hight attributes of the screen rect to update 
    # the settings object

     self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

# Shooting Bullets
# Now we'll add the ability to shoot bullets 
# the bullets are represented by a small rectangle 
# Fires when the player presses down on the space bar
# First add bullets to settings

# Bullets Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

# speed slightly faster than ship, width and height 3 pix by 15 pix, and a 
# dark grey for the color

# Creating Bullet Class
# new file called bullet.py
    # the bullet class inherits from Sprite
    # this groups related elements in your game and acts on all group elements
    # at once 

    # to create a bullet instance the __init__() needs the current instance of AI
    # so we call super() to inherit properly from Sprite
    # we also add attributes for screen, and settings object, and bullet color
    
    # then we set bullet rect attributes
    # we dont have an image for bullet so we build a rect from scratch pygame.RECT()
    # requires x and y coordinates of top left and width height of rect
    # we start at (0,0) but we'll move it to the correct position in the 
    # next line, bullet position depends on ship position
    # set bullet midtop attribute to ship midtop attribute
    # this will make it shoot from the top of the ship
    # we use float for y coordinate so we can make fine adjustments to its speed

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.setting.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet position as a float
        self.y = float(self.rect.y)

# Sceond part for bullet class
    # the update method manages the bullets position
    # when fired, bullet moves up the screen to a decreasing y coordinate value
    # to update to subtract settings.bullet_speed from slef.y
    # then we use the value of self.y to set value of rect.y

    # dont have to change x coordinate cuz bullet just moves up screen

    # when we want to draw bullet we call draw_bullet() the draw.rect fills the
    # part of the screen defined by bullets rect with the color sotred in self.color

   def update(self):
        """Move the bullet up the screen"""
        # update the exact positon of the bullet
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

# now implement these changes in AlienInvasion class

from ship import Ship
from bullet import Bullet # import bullet

self.ship = Ship(self)
self.bullets = pygame.sprite.Group() # creat a group that holds the bullets in __init__

# next update position of bullets for each pass through the while loop
 def run_game(self):
        """Starts the main loop for game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

# Firing Bullets
# modify keydown events to fire bullet when player presses spacebar
# you dont need to modify keydown because nothing happens when a player releases

# we also need to modify _update_screen to make sure the bullet is drawn before we call
# flip()

 def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

 def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on screen, and flip to a new screen"""
        # Redraw the screen during each pass through loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

# Deleteing Old Bullets
    # right now our bullets continue to exist
    # even though they are out of screen they continue to move up the y coordinate
    # doing so can consume memory and processing power

    # We need to get rid of old bullets, or the game will slow down
    # detect the bottom value of the bullets rect has reached 0
    # this indicates that the bullet has left the screen

    # the Group function works like a list. gathering all the bullets.  
    # we use the copy method which leaves us free to modify the orginal
    # bullets inside the loop. 
    # we check if each bullet has left the screen
    # use print to see how many bullets exist in the game and verify that they
    # are deleted
    # since we see that it works. remove print after checking

    def run_game(self):
        """Starts the main loop for game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()
            self.clock.tick(60)

# Limited number of bullets
# First store number of bullets allowed in seting.py
# use this setting to check how many bullets excist before creating a new bullet
# in _fire_bullet()

 # Bullets Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
# if len of bullets shot < 3 you can shoot another. if 3 on screen
# you cant shoot another till one disapears

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

# Creating the _update_bullets() method

# to keep our code organized we will move our bullet management to a seperate 
# method called _update_bullets(). add this just before _update screen

# Chapter 13
    # Learn more about pygame and how to manage large files
    # how to detect collisions between elements in game
    
    # when working on a large project, before starting another huge session
    # review what you intend to do, get a gameplan together
        # for example.....
        # add alien to the top left of screen with appropriate spacing 
        # around it
        # fill the upper portion of the screen with as many aliens as we can
        # fit horizontally. We then add additional rows of aliens until 
        # we have a full fleet
        # make the feet move sideways and down until the entire fleet is 
        # shot down, hits our ship, or reaches the ground.
        # if entire fleet is shot down, we then create a new fleet.
        # if the alien hits our ship or the ground, we destroy our ship 
        # and create a new fleet
        # create a number of ships a player can use, and end game when all ships
        # are destroyed


# Creating our First Alien
    # make class

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("image/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.x = float(self.rect.x)

    # edit main code for game
        # __init__
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    # make method for creating alien

    def _create_fleet(self):
        """Create fleet of aliens"""
        # make an alien
        alien = Alien(self)
        self.aliens.add(alien) 

# Building the Alien Fleet

    # to draw a fleet we need to figure out how to full the upper portion of the
    # screen with aliens without over crowding the game window
    # we'll do this by adding aliens across the top of the screen until
    # theres no space left for a new alien
    # we will repeat this process as long as we have enough vertical space
    # to add a new row

# creating a row of aliens
    # the only function we need to adjust is _creat_fleet:
    def _create_fleet(self):
        """Create fleet of aliens"""
        # create an alien and continue to do so until theres no room left
        # spacing between aliens is one alien width
        alien = Alien(self)
        alien_width = alien.rect.width
        # we get the aliens width from the first one we crated
        current_x = alien_width 
        # keep placing aliens WHILE there is still room to place one
        while current_x < (self.settings.screen_width - 2 * alien_width): 
            # crate alien in correct position, difine horizontal position of next alien, creat new alien, asign it to new_alien
            new_alien = Alien(self)
            # set percise horizontal position to the current value of x
            new_alien.x = current_x
            # we also position the aliens rect at the same value
            new_alien.rect.x = current_x
            # and then add new alien to group self.aliens
            self.aliens.add(new_alien)
            # incriment value of current_x
            current_x += 2 * alien_width 

# Refactoring _create_fleet()
    # if all we need was one row of aliens we'd be set but theres more work here
    # so lets clean up
    # make another helper method under create fleet
    # the code used is the same as the previous in create fleet BUT
    # we change the parameter name from current_x to parameter_x
    # this will make it easier to add new rows and create an entire fleet
     def _create_alien(self, x_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

# Adding Rows
# we will work with two While loops an outer and inner
# one focusing on x axis and another on y axis which will make new rows

def _create_fleet(self):
        """Create fleet of aliens"""
        # create an alien and continue to do so until theres no room left
        # spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        # we need to know aliens height to place row, so we grab height and 
        # width using size attributes of an alien rect
        alien_width, alien_height = alien.rect.size
        # set x y values for the placement of our first alien
        current_x, current_y = alien_width, alien_height
        # define while loop that controls how many rows are placed on screen
        # as long as next row is less than screen height - 3 alien heights
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # call _create_alien and pass it the y value and x position
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width 

            # Finished a row; reset x value, and increment y value.
            # this block only runs after inner loop is finished
            # runs once after each row is created
            current_x = alien_width
            current_y += 2 * alien_height   

# now we need to modify _create_alien() to set the vertical position of the 
# alien correctly
                                    # add parameter
def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        # add intention
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

# making the fleet move

# Move to right 
# to move aliens to the right we'll use a update method in the aliens file
    # first add a setting to control the speed of the aliens moving 
    self.alien_speed = 1.0

    # next use this setting to implement update speed in Alien Class
    # create a settings parameter in init to access aliens speed in update 
    # each time it updates it moves alien to right at the speed stored in settings
     def __init__(self, ai_game):
        """Initialize the alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

    # create update function
    # we track aliens exact position with self.x attributes which can hold float values
    # then use value of self.x to update position of aliens rect
    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

    # in main loop, add a call to update the position of each alien as well
    def run_game(self):
        """Starts the main loop for game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    # now we can write the code for _uodate_aliens() which will move the fleet
    # place this after _update_bullets() to match the order in while loop
    # we use update method on the alien group which calls the aliens update()
    
    def _update_aliens(self):
        """Update positions of all aliens in fleet"""
        self.aliens.update()

    # Creating Settings for fleet direction
    # now we'll create the settings that will move the fleet down the screen
    # and to the left when hit hits the right edge of the screen
    # Start in settings
    # note, we could use left or right (using if else statements)
    # BUT since we're only going left and right number 1 and -1 will be cleaner
    # Alien Setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    # Checking whether an alien has hit the edge
    # make method to check if alien has hit the edge 
    # and modify update to allow each alien to move in the appropriate direction

    # detects if alien at right edge if rect right is <= screen right
    # detects left edge if position is <= 0 
    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    # modify update 
    # allows motion to the ledt or right by multiplying the aliends speed by
    # its direction
    def update(self):
        """Move the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    # dropping the fleet and changing direction
    # loop through the fleet and call check edges()
    # if returned True we know alien is at an edge and the loop will break
    def _check_fleet_edges(self):
        """Respond appropriatly if any alien has reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    # loop through aliens and drop each one using the fleet drop speed
    # then we change the value of fllet drop speed by multiplying it by -1
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    # lastly update _update_aliens()

    def _update_aliens(self):
        """Update positions of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    # Shooting Aliens

    # In a lot of game programming, collisions happen when game elements 
    # over lap.  

    # to make the bullets shoot down the aliens we'll use
        # sprite.groupcollide()

    # Detecting Bullet Collision

    # look for collision immediatly after updating the position of all the bullets
    # the sprite.groupcollide() functions compares the rects of each element in
    # one group with the rects of each element in another group(Bullet and Alien)
    # this will return of dictionary of each alien and bullet that have been 
    # collided
    # Each key will be a bullet, and corresponding value will be the alien
    # that was hit (This is also how we'll create a scoring system)
    # add following code to the end of _uodate_bullets()

    # Check for any bullets that have hit Aliens.
        #   If so, get rid of bullet and alien
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        # compares bullets and alien position. Whenever they collide the key value
        # pair gets added to the dictionary it returns
        # The True argument tells python to delete both bullet and alien
        # after they collide

# Making larger bullets for testing
 
    # You could shoot down every fleet on the screen to see if your code
    # responds to an empty fleet correctly but that could take a while

    # To test this you can change the settings of bullet speed, amount of aliens
    # or give yourself a shit load of bullets 

    # Or making a really wide bullet that remains active even after they've hit
    # an alien

    # change bullet setting bullet_width to 300
    # or 3000 and see how quickly you can shoot them down
    # also could be a good idea for a super charges bullet ;)

    # Repopulating the Fleet
    # We dont want the game to be over when the first fleet is gone
    # We first want to check if the alien group is empty
    # is so we make a call to _create_fleet()
    # Perform this check at the end of _update_bullets()
    # this is where the individual aliens are performed
    # checks if alien group empty. an empty group evaluates to False
    if not self.aliens: 
            # Destroy existing bullets and create new fleet.
            # if alien empty use empty() method to remove all remaining sprites in a group
            self.bullets.empty()
            # call to fill screen with aliens again
            self._create_fleet()

    # Speed Up Bullets

    # When you start making a game usually you have seetings to a slower pace
    # now since the bones are put together, and weve done our tests
    # lets speed it up a smidge
    # This is another reason why refractoring is important
    # head to settings and uncrease bullet speed
    # so simple

    # Refractoring _update_bullets()
    # refractor so theres not as much going on in this method
    # we'll move bullet alien collision to a seperate mothod 
    
    # Ending the Game
    # If the aliens make contact with the ship, your ship will be destroyed
    # or if the alien reaches the bottom of the screen, destroyed
    # We will limit the number of ships a player can use
    # game ends when player has used all ships

    # Detecting Ship Collision
    # we'll check for alien ship collisions immediatly after updating
    # the position of each alien in AlienInvasion

     def _update_aliens(self):
        """Update positions of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("SHIP HIT!!!")
        # spritecollideany function takes two arguments
        # a sprite and a group
        # the function looks for any member of the group that has collided
        # with the sprite...the ship. and stops loop as soon as collision happens

# Responding to alien-ship Collision
    # We' count how many times the ship has been hit by tracking statistics from
    # the game. This will also help with scoring 
    # Start by making a new class GameStats

    class GameStats:
    """Track Statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize Statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize Statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit

        # In this class the init will set the stats when game first opens
        # and will call reset stats whenevr a ship is destroyed
        # the number of ships a player starts with will be stored in settings
        # add ship_limit and set it to 3
        # Also, need to update Alien Invasion

        # add from time import sleep so we can pause game for a moment
        # when the ship has been hit
        # Import gaestats aswell
        # create an instance for game_stats

        import sys
        from time import sleep
        import pygame

        from settings import Settings
        from game_stats import GameStats
        # creat instance to store game statistics
        self.stats = GameStats(self)
        # add new method to Alien Invasion
        def _ship_hit(self):
            """Respond to the ship being hit by an Alien"""
            # Decrement Ships Left
            self.stats.ships_left -= 1
            # Get rid of any remaining bulets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(0.5)
        # not edit _update_aliens. replace print('Ship Hit') with calling for 
        # ship_hit()
        def _update_aliens(self):
            """Update positions of all aliens in fleet"""
            self._check_fleet_edges()
            self.aliens.update()
            # look for alien-ship collision
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self._ship_hit()
        # now add new method to ship to recenter ship
        def center_ship(self):
            """Center the ship on the screen"""
            self.rect.midbottom = self.screen_rect.midbottom
            self.x = float(self.rect.x)

# Aliens that reach the bottom of the Screen
    # If an alien hits the bottom of the screen we'll have the game reset 
    # the same way it does when a ship gets hit
    # We'll add this new method to Alien Invasion
    def _check_aliens_bottom(self):
        """Check if any Aliens have reached the Bttom of Screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same way if ship got hit 
                self._ship_hit()
                break
    # update and call this method from _update_aliens()
    def _update_aliens(self):
        """Update positions of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Look for aliens hitting bottom of screen
        self._check_aliens_bottom()

    # Game Over
    # Right now the ships_left() just grows into the negative
    # We'll add a game active flag so we can end the game when a player
    # runs out of ships
    
        # Start Alien Invasion in an active state
            self.game_active = True
    
    # Now add code to _ship_hit() that sets game to false with ships are all gone
    def _ship_hit(self):
        """Respond to the ship being hit by an Alien"""
        if self.stats.ships_left > 0:
            # Decrement Ships Left
            self.stats.ships_left -= 1
            # Get rid of any remaining bulets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    # identifying when parts of the game should run
        # We need to identify the parts of the game that should always run
        # and the parts that should only run when active

        def run_game(self):
        """Starts the main loop for game"""
            while True:
                self._check_events()

                if self.game_active:
                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()
                    
                self._update_screen()
                self.clock.tick(60)


# scoring
# add play button
# ajust the game_active in the init secction to false
# now the game runs but is inactive. 
# we need to build a new class Button to make it so we are able to start the game

# restart game when it ends
# speed up game after completing levels
# implement a scoring system

