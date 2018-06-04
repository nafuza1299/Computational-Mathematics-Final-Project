from pygame import *
from BirdClass import *
from BirdFunction import *

pygame.init()

def transition_screen2():

    '''Opens the transition screen for the second Room'''

    while True:
        menuscreen = MainScreen("level1.jpg")
        transition_text = textsprite("AngryBirds", 'Level 2', 100, 440, 170, 0, 0, 0)
        text_call = Group(transition_text)
        text_call.draw(menuscreen.display)
        transition_wait = event.wait()
        if transition_wait.type == MOUSEBUTTONDOWN:
            run_game2()
        display.update()

#runs the second level of the game
def run_game2():
    #draws the characters and background to the screen
    screen = pygame.display.set_mode((1120, 560))
    display.set_caption("Happy Birds")
    bg_image = background("level1.jpg")
    sling = imagesprite("Slingshot1.png", 80, 340)
    pygame.init()
    bird = happy(screen, 100, 340, 10)
    bird_group = Group(bird)
    sling_group = Group(sling)
    bool = True
    while True:
        bg_image.draw(screen,0,0)
        bird_group.draw(screen)
        sling_group.draw(screen)
        level2_wait = pygame.event.wait()
        if level2_wait.type == QUIT:
            quit()
        if level2_wait.type == KEYDOWN:
            if level2_wait.key == K_ESCAPE:
                import BirdHub; BirdHub.menu()
        enemy = level2(screen)
        #if bird is clicked, the sprite can be moved

        if bird.rect.collidepoint(mouse.get_pos()):
            if level2_wait.type == MOUSEBUTTONDOWN:
                while True:
                    bool = False
                    for event1 in pygame.event.get():
                        if event1.type == pygame.QUIT:
                            pygame.quit()
                    mx,my = pygame.mouse.get_pos()
                    bg_image.draw(screen,0,0)
                    enemy.show()
                    x = mx - 10
                    y = my - 10
                    #gets the difference betweeen the initial spawn point and point after mouse click
                    x2 = 100 - mx
                    y2 = (400 - my) * -1
                    #sets the above values to the class

                    bird.setleft(x)
                    bird.settop(y)
                    sling_group.draw(screen)

                    #bird can only be moved at this specific area
                    if x <= 100 and y >= 340:
                        pygame.draw.line(screen, (45, 27, 16,), [mx+10, my+10], [120, 370], 5)
                        pygame.draw.line(screen, (45, 27, 16,), [mx+10, my+10], [150, 370], 5)
                        arrow = pygame.image.load("arrow1.png")
                        if mx >= 90:
                            img = pygame.transform.rotate(arrow, mx - 130) #arrow rotation
                            screen.blit(img, (130, 280))
                        else:
                            img = pygame.transform.rotate(arrow, mx - 90) #arrow rotation
                            screen.blit(img, (130, 280))
                        screen.blit(bird.image, (x,y))


                        pygame.display.flip()

                    move_wait = pygame.event.wait()
                    if move_wait.type == QUIT:
                        quit()
                    if move_wait.type == KEYDOWN:
                        if move_wait.key == K_ESCAPE:
                            import BirdHub; BirdHub.menu()
                    bird.setscalex(0) #gives temporary value for xcoor in birdclass in case x2 and y2 is zero
                    if x<= 100 and y >= 340:
                        if x2 != 0 or y2 != 0:
                            if move_wait.type == MOUSEBUTTONDOWN:
                                Hit = pygame.mixer.Sound('Throw.wav').play()
                                y = sqrt(x2**2 + y2**2) #calculations to get the hypotenuse
                                #cosine and sine is used to manipulate the interpolation
                                cosine = math.cos(y2/y)
                                sine = math.sin(x2/y)
                                xscale =  x2/(sine*5)
                                #yscale must be positive, otherwise the bird will fly up the screen
                                if y2 < 0:
                                    yscale = y2/(cosine*5) * -1
                                else:
                                    yscale = y2/(cosine*5)
                                bird.setscaley(yscale)
                                bird.setscalex(xscale)

                                theClock = pygame.time.Clock()
                                Fps = 60
                                timer = pygame.time.get_ticks()

                                #loops the animation 300 times
                                for i in range (300):
                                    theClock.tick(Fps)
                                    Fps += 0.001
                                    bg_image.draw(screen,0,0) #redraws the background to be constantly blitting
                                    bird_group.draw(screen)
                                    enemy.show()
                                    sling_group.draw(screen)
                                    event.get()

                                    #line (117 -137)animates the interpolation and the curve
                                    #for each interval the bird increases at a set value; intervals are used to create the projectile
                                    if i < 10:
                                        bird.posi1()
                                    elif i < 20:
                                        bird.posi2()
                                    elif i < 30:
                                        bird.posi3()
                                    elif i < 40:
                                        bird.posi4()
                                    elif i < 50:
                                        bird.posi5()
                                    elif i < 60:
                                        bird.nega1()
                                    elif i < 70:
                                        bird.nega2()
                                    elif i < 80:
                                        bird.nega3()
                                    elif i >= 90:
                                        bird.nega4()

                                    display.update()
                                    #if collide with woodblock, the bird will spawn back at initial spawn point
                                    if enemy.woodblock1.rect.colliderect(bird):
                                        if enemy.woodblock_call1:
                                            Hit = pygame.mixer.Sound('Woodhit.wav').play()
                                            enemy.remove("woodblock1")
                                            bird.rect.left = 100
                                            bird.rect.top = 340
                                            break

                                    #collision between the bird and the pig
                                    if enemy.pig1.rect.colliderect(bird):
                                        if enemy.pig1 in enemy.bird_call:
                                            Hit = pygame.mixer.Sound('Hit.wav').play()
                                        enemy.remove("pig1")
                                    if enemy.pig2.rect.colliderect(bird):
                                        if enemy.pig2 in enemy.bird_call:
                                            Hit = pygame.mixer.Sound('Hit.wav').play()
                                        enemy.remove("pig2")
                                    if enemy.pig3.rect.colliderect(bird):
                                        if enemy.pig3 in enemy.bird_call:
                                            Hit = pygame.mixer.Sound('Hit.wav').play()
                                        enemy.remove("pig3")
                                    if bird.rect.left >= 1120 or bird.rect.top >= 560:
                                        bird.rect.left = 100
                                        bird.rect.top = 340
                                        break

                                    if not enemy.bird_call:
                                        import Level3; Level3.transition_screen3()



        display.update()
