import pygame
import random
debug = False #True

# game setup
gamemode = input("What's your gamemode? (move, stationary)")
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
targetDirection = [0, 0]
accurateHit=1
totalHit=1

# pygame setup
pygame.init()
info = pygame.display.Info()
screenWidth = round(info.current_w * 0.95)
screenHeight = round(info.current_h * 0.90)
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Aim Trainer")
x = random.randint(targetRect.width, screenWidth - targetRect.width)
y = random.randint(targetRect.height, screenHeight - targetRect.height)
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            totalHit+=1
            if targetRect.collidepoint(mousePos): #Hit target
                x = random.randint(targetRect.width, screenWidth - targetRect.width)
                y = random.randint(targetRect.height, screenHeight - targetRect.height)
                score+=1
                currentScore+=1
                targetDirection = [random.randint(-1,1), random.randint(-1, 1)]
                accurateHit+=1

    # Background fill
    screen.fill("white")

    # Gamemode
    if gamemode == "move":
        x+=targetDirection[0]*moveSpeed
        y+=targetDirection[1]*moveSpeed
        if x>screenWidth or x<0:
            targetDirection[0]*=-1
        elif y>screenHeight or y<0:
            targetDirection[1]*=-1
    elif gamemode == "stationary":
        pass

    targetRect.topleft = (x, y)

    # Drawing
    screen.blit(targetImage, (x, y))
    scoreText = font.render(f"Avg. Time Per Target: {round(currentScore/currentTimeElapsed, 2)} | Accuracy: {int(round(accurateHit/totalHit, 2)*100)}%", True, "black")
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