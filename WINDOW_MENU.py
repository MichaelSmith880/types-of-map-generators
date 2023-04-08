import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Load the background image
bg_image = pygame.image.load(r'C:\Users\User\Desktop\GitHub-Python\game_space_2d\GAME_ENGINE\USER_INTERFACE\img\milky-way.jpg')
# Scale the background image to fit the display
bg_image = pygame.transform.scale(bg_image, (screen.get_width(), screen.get_height()))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define font
font = pygame.font.SysFont("Arial", 30)

# Define buttons
button_play = pygame.Rect(300, 275, 200, 50)
button_settings = pygame.Rect(300, 375, 200, 50)
button_close = pygame.Rect(300, 475, 200, 50)

# Define button text
text_play = font.render("Play", True, WHITE)
text_settings = font.render("Settings", True, WHITE)
text_close = font.render("Close", True, WHITE)

# Define function for handling events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_play.collidepoint(event.pos):
                play()
            elif button_settings.collidepoint(event.pos):
                settings()
            elif button_close.collidepoint(event.pos):
                close()

# Define functions for button actions
def play():
    while True:
        # Clear the screen
        screen.fill(WHITE)
        
        # Create text surface
        text = font.render("Playing...", True, BLACK)
        
        # Create button to go back to main menu
        button_back = pygame.Rect(300, 500, 200, 50)
        pygame.draw.rect(screen, BLACK, button_back)
        text_back = font.render("Back to Menu", True, WHITE)
        screen.blit(text_back, (350, 515))
        
        # Handle events
        handle_events()
        
        # Blit text onto screen
        screen.blit(text, (350, 250))
        
        # Update the display
        pygame.display.update()

def settings():
    while True:
        # Clear the screen
        screen.fill(WHITE)
        
        # Create text surface
        text = font.render("Settings...", True, BLACK)
        
        # Create button to go back to main menu
        button_back = pygame.Rect(300, 500, 200, 50)
        pygame.draw.rect(screen, BLACK, button_back)
        text_back = font.render("Back to Menu", True, WHITE)
        screen.blit(text_back, (350, 515))
        
        # Handle events
        handle_events()
        
        # Blit text onto screen
        screen.blit(text, (350, 250))
        
        # Update the display
        pygame.display.update()

def close():
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    # Clear the screen
    screen.blit(bg_image, (0, 0))
    
    # Draw buttons onto screen
    pygame.draw.rect(screen, BLACK, button_play)
    text_play_rect = text_play.get_rect(center=button_play.center)
    screen.blit(text_play, text_play_rect)

    pygame.draw.rect(screen, BLACK, button_settings)
    text_settings_rect = text_settings.get_rect(center=button_settings.center)
    screen.blit(text_settings, text_settings_rect)

    pygame.draw.rect(screen, BLACK, button_close)
    text_close_rect = text_close.get_rect(center=button_close.center)
    screen.blit(text_close, text_close_rect)

    
    # Handle events
    handle_events()
    
    # Update the display
    pygame.display.update()
