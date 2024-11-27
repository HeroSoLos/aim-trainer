import pygame
import random

from playerRelated import clickSequenceTracker
from playerRelated.clickSequenceTracker import ClickSequenceTracker
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
scoreTimeElapsed = 0.0001
scoreResetInterval = 10
scoreStartTime = 0
scoreCurrentTimeElapsed = 0.001
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
for i in range(0):
    targetList.append(AvoidTarget(i, [0, 0], [0, 0], 1, 0, [0, 0, 0], targetImage, screenWidth/4))
    targetList[i].set_speed(moveSpeed)
for j in range(1):
    targetList.append(Target(j, [0, 0], [0, 0], 1, 0, [0, 0, 0], targetImage))
    targetList[j].set_speed(moveSpeed)

click_sequence_tracker = ClickSequenceTracker(0, [[1, 3, 1], [1, 1, 1]], 500)

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

        # Mouse Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sequence_tracker.add_click(event.button, pygame.time.get_ticks())
            print(f"ADDED {event.button} CURRENT SEQUENCE {click_sequence_tracker.current_sequence}")
            totalHit+=1
            for target in targetList: # Check if hit
                if target.rect.collidepoint(mousePos): #Hit target
                    target.clicked(screenWidth, screenHeight)
                    score+=1
                    currentScore+=1
                    accurateHit+=1

            completed_sequence = click_sequence_tracker.check_completed_sequence()
            print(f"COMPLETED SEQUENCE {completed_sequence}")

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

    # scoreText = font.render(f"Avg. Time Per Target: {round(currentScore/currentTimeElapsed, 2)} | Accuracy: {int(round(accurateHit/totalHit, 2)*100)}%", True, "black")
    # scoreTextRect = scoreText.get_rect()
    # screen.blit(scoreText, ((info.current_w-scoreTextRect.width)/2, 10))

    # Debug
    if debug:
        print(targetList[0].direction)

    # update
    pygame.display.flip()

    # Time

    # Score counter reset
    scoreTimeElapsed = pygame.time.get_ticks() / 1000
    scoreCurrentTimeElapsed = scoreTimeElapsed - scoreStartTime
    if scoreCurrentTimeElapsed >= scoreResetInterval:
        scoreStartTime = scoreTimeElapsed
        currentScore = 0

    click_sequence_tracker.dt(pygame.time.get_ticks())
    if click_sequence_tracker.reset_check(pygame.time.get_ticks()):
        print("RESET")

    clock.tick(120)  # limits FPS

pygame.quit()
print(f"Score: {score}")