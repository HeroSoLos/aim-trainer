# Example file showing a basic pygame "game loop"
import pygame
import random
debug = False #True
# pygame setup
pygame.init()
info = pygame.display.Info()
screenLength = round(info.current_w*0.95)
screenWidth = round(info.current_h*0.90)
screen = pygame.display.set_mode((screenLength, screenWidth))
clock = pygame.time.Clock()
pygame.display.set_caption("Aim Trainer")

# game setup
targetImage = pygame.image.load(r'assets/targets.png')
targetImage = pygame.transform.scale(targetImage, (50, 50))
targetRect = targetImage.get_rect()
x = random.randint(targetRect.width, screenLength - targetRect.width)
y = random.randint(targetRect.height, screenWidth - targetRect.height)
font = pygame.font.Font(None, 36)
score = 0
currentScore=0
timeElapsed = 0.0001
resetInterval = 10
startTime = 0
currentTimeElapsed = 0.001

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            targetRect.topleft = (x, y)
            if targetRect.collidepoint(mousePos):
                x = random.randint(targetRect.width, screenLength - targetRect.width)
                y = random.randint(targetRect.height, screenWidth - targetRect.height)
                score+=1
                currentScore+=1

    # Background fill
    screen.fill("white")

    # Drawing
    screen.blit(targetImage, (x, y))
    scoreText = font.render(f"Avg. Time Per Target: {round(currentScore/currentTimeElapsed, 2)}", True, "black")
    scoreTextRect = scoreText.get_rect()
    screen.blit(scoreText, ((info.current_w-scoreTextRect.width)/2, 10))
    # Debug
    if debug:
        print(f"x {x}, y {y}")

    # update
    pygame.display.flip()

    # Time
    timeElapsed = pygame.time.get_ticks() / 1000
    currentTimeElapsed = timeElapsed - startTime
    if currentTimeElapsed >= resetInterval:
        startTime = timeElapsed
        currentScore = 0

    clock.tick(60)  # limits FPS to 60

pygame.quit()
print(f"Score: {score}")