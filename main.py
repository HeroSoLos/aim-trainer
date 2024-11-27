import pygame
import random
from targetRelated.target import Target
from targetRelated.avoidTarget import AvoidTarget

# debug = True
debug = False

# game setup
moveSpeed = int(input("Move speed?"))
targetImage = pygame.image.load(r'assets/targets.png')
targetImage = pygame.transform.scale(targetImage, (50, 50))
targetRect = targetImage.get_rect()
score = 0
currentScore=0
timeElapsed = 0.0001
resetInterval = 10
startTime = 0
currentTimeElapsed = 0.001
accurateHit=1
totalHit=1

# pygame setup
pygame.init()
info = pygame.display.Info()
screenWidth = round(info.current_w * 0.95)
screenHeight = round(info.current_h * 0.85)
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Aim Trainer")
font = pygame.font.Font(None, 36)

targetList = []
for i in range(500):
    targetList.append(AvoidTarget(i, [0, 0], [0, 0], 1, 0, [0, 0, 0], targetImage, screenWidth/4))
    targetList[i].set_speed(moveSpeed)

is_fullscreen = False
running = True
while running:
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle F11 key for toggling fullscreen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                screenWidth = round(info.current_w)
                screenHeight = round(info.current_h)
                screen = pygame.display.set_mode((screenWidth*1.2, screenHeight*1.2), pygame.FULLSCREEN) # VERY UNSURE FOR THE FULLSCREEN MULTIPLIER
            else:
                screenWidth = round(info.current_w * 0.95)
                screenHeight = round(info.current_h * 0.85)
                screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

        # Handle maximize/restore button
        if event.type == pygame.VIDEORESIZE and not is_fullscreen:
            screenWidth, screenHeight = event.size
            screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            totalHit+=1
            for target in targetList:
                if target.rect.collidepoint(mousePos): #Hit target
                    target.clicked(screenWidth, screenHeight)
                    score+=1
                    currentScore+=1
                    accurateHit+=1

    # Background fill
    screen.fill("white")

    # Gamemode
    
    for target in targetList:
        target.rect.topleft = target.position

        if type(target) == Target:
            pass
        elif type(target) == AvoidTarget:
            target.calculate_direction(mousePos, screenWidth, screenHeight)

        target.check_wall_collision(screenWidth, screenHeight)
        target.move()

    # Drawing
    for target in targetList:
        screen.blit(target.image, target.position)

    scoreText = font.render(f"Avg. Time Per Target: {round(currentScore/currentTimeElapsed, 2)} | Accuracy: {int(round(accurateHit/totalHit, 2)*100)}%", True, "black")
    scoreTextRect = scoreText.get_rect()
    screen.blit(scoreText, ((info.current_w-scoreTextRect.width)/2, 10))

    # Debug
    if debug:
        print(targetList[0].direction)

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