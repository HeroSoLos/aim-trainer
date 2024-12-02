import pygame
import random

from playerRelated.clickSequenceTracker import ClickSequenceTracker
from playerRelated.spellCaster import SpellCaster
from playerRelated.spells.cloneSpell import CloneSpell
from playerRelated.spells.posionSpell import PoisonSpell
from playerRelated.spells.summoningSpell import SummoningSpell
from playerRelated.spells.timeSpell import TimeSpell
from playerRelated.spells.voidSpell import VoidSpell
from targetRelated.target import Target
from targetRelated.avoidTarget import AvoidTarget
from playerRelated.cursor import Cursor
# debug = True
debug = False

# game setup
moveSpeed = 5
print(f"Move speed {moveSpeed}")
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
scoreFont = pygame.font.Font(None, 36)
sequenceFont = pygame.font.Font(None, 20)

# Targets

targetList = []
for i in range(0):
    targetList.append(AvoidTarget(i, [0, 0], [0, 0], 1, 0, [0, 0, 0], targetImage, screenWidth/4))
    targetList[i].set_speed(moveSpeed)
for j in range(100):
    targetList.append(Target(j, [0, 0], [0, 0], 1, 0, [0, 0, 0], targetImage))
    targetList[j].set_speed(moveSpeed)

# Click Sequence

click_sequence_tracker = ClickSequenceTracker(0,
    [
    [3, 1, 3],
    [1, 1, 1],
    [3, 3, 3]
    ], 500)

# Spells
clone_spell = CloneSpell()
time_spell = TimeSpell()
poison_spell = PoisonSpell()
void_spell = VoidSpell()
summoning_spell = SummoningSpell()

spell_caster = SpellCaster([[poison_spell, 0], [void_spell, 0], [summoning_spell, 0], [clone_spell, 0], [time_spell, 0]])

cursor = Cursor([0, 0], 100, 100, spell_order=[poison_spell, void_spell, summoning_spell, clone_spell, time_spell], passive_buffs=[])



completed_sequence = False # TODO: Find appropriate place for this
is_fullscreen = False
running = True
while running:
    mousePos = pygame.mouse.get_pos()
    cursor.set_position(mousePos)
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
            #print(f"ADDED {event.button} CURRENT SEQUENCE {click_sequence_tracker.current_sequence}")
            totalHit+=1
            for target in targetList: # Check if hit
                if target.rect.collidepoint(mousePos): #Hit target
                    target.clicked(screenWidth, screenHeight)
                    score+=1
                    currentScore+=1
                    accurateHit+=1

            completed_sequence = click_sequence_tracker.check_completed_sequence()
            print(f"COMPLETED SEQUENCE {completed_sequence}")

            # DEMO DRAW:
            if completed_sequence == click_sequence_tracker.click_sequences[0]:
                cursor.square_repeat_draw = 720
            elif completed_sequence == click_sequence_tracker.click_sequences[1]:
                cursor.hexagon_repeat_draw = 720
            elif completed_sequence == click_sequence_tracker.click_sequences[2]:
                cursor.triangle_repeat_draw = 720

    # Background fill
    screen.fill("white")

    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if cursor.key_hold_delay < 0:
            cursor.cycle_spell_backward()
            cursor.inventory_repeat_draw = cursor.INVENTORY_REPEAT
            cursor.key_hold_delay = cursor.KEY_HOLD_REPEAT
    if keys[pygame.K_RIGHT]:
        cursor.inventory_repeat_draw = cursor.INVENTORY_REPEAT
    if keys[pygame.K_DOWN]:
        if cursor.key_hold_delay < 0:
            cursor.cycle_spell_forward()
            cursor.inventory_repeat_draw = cursor.INVENTORY_REPEAT
            cursor.key_hold_delay = cursor.KEY_HOLD_REPEAT
    if keys[pygame.K_c]:
        spell_caster.spell_list[cursor.current_spell][1] = 240

    cursor.key_hold_delay -= 1
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


    #DEMO
    cursor.draw_rect(screen)
    if cursor.hexagon_repeat_draw > 0:
        hexagon = cursor.draw_hexagon(screen)
        cursor.check_hexagon_collide(targetList, hexagon, screenWidth, screenHeight)
        cursor.hexagon_repeat_draw -= 1

    if cursor.triangle_repeat_draw > 0:
        cursor.draw_triangle(screen)
        for target in targetList:
            target.clicked(screenWidth, screenHeight)
            score+=1
        cursor.triangle_repeat_draw -= 1
    cursor.update_angle()
    #DEMO END

    click_sequence_tracker.draw(screen, sequenceFont, (0, 0, 0), mousePos)
    if cursor.inventory_repeat_draw > 0:
        cursor.draw_spell_inventory(screen)
        cursor.inventory_repeat_draw -= 1
        if cursor.inventory_repeat_draw < 20:
            cursor.draw_inventory_opacity_change(screen, cursor.fade_away_opacity1)
        elif cursor.inventory_repeat_draw < 60:
            cursor.draw_inventory_opacity_change(screen, cursor.fade_away_opacity2)

    targets_to_click = spell_caster.check_spell_list(mousePos, targetList)
    for target in targets_to_click:
        target.clicked(screenWidth, screenHeight)

    # Debug
    if debug:
        print(targetList[0].direction)

    # update
    pygame.display.flip()

    # Time and Resets

    # Score counter reset
    scoreTimeElapsed = pygame.time.get_ticks() / 1000
    scoreCurrentTimeElapsed = scoreTimeElapsed - scoreStartTime
    if scoreCurrentTimeElapsed >= scoreResetInterval:
        scoreStartTime = scoreTimeElapsed
        currentScore = 0

    click_sequence_tracker.dt(pygame.time.get_ticks())
    if click_sequence_tracker.reset_check(pygame.time.get_ticks()):
        #print("RESET")
        pass

    if completed_sequence:
        click_sequence_tracker.reset_sequence()

    clock.tick(120)  # limits FPS

pygame.quit()
print(f"Score: {score}")