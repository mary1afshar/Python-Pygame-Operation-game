#Maryam Afshar
#ICS3U1-02
#Mr.Saleem

#summative

##################
#LEVEL 1
#################

#importing pygame
import pygame, random

#defining the size of the screen
SIZE = (WIDTH, HEIGHT) = (435, 700)

#defining colours
GREEN = (0, 240, 0)
BLUE = (64,224,208)
YELLOW = (255, 255,0)
BLACK = (0, 0, 0)
RED= (255, 0, 0)
WHITE = (255,255,255)

#Define clock so that we can change clockspeed
clock = pygame.time.Clock()

#screen
pygame.init()

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

#setting up background and screen
screen= pygame.display.set_mode(SIZE)
bg = pygame.image.load("BOBSS.png")
    
#Define a font for the text
mfont = pygame.font.SysFont("comicsansms", 22)
sfont = pygame.font.SysFont("luximono", 23)

#function for messages
def message(message, color, placement, font):
    screenText = font.render(message, True, color)
    screen.blit(screenText, placement)

#starting screen for user, to play or not, and how to play rules
def startScreen():
    intro = True
    #While loop to ensure the start screen stays until when needed
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                running = False
                pygame.quit()
                
            #If the user clicks "p", the game will start
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                    
                #If the user clicks "q", pygame will quit
                if event.key == pygame.K_q:
                    intro = False
                    running = False
                    pygame.quit()
                    
        #Fill the pygame window with the desired color
        screen.fill(BLACK)
        start = pygame.image.load("start.png")
        screen.blit(start, [0,0])
        message("GOOD LUCK AND PLEASE SAVE BOB!", BLUE, (25, 530), mfont)
        message("Press 'P' to play or 'Q' to quit", BLUE, (65, 600), mfont)
        
        #Update the display screen so that all changes are shown on the pygame window
        pygame.display.update()

        #Set the frame rate so that when the user chooses to continue or quit the wait time is adequete
        clock.tick(10)

def Level1():
    class Operation(pygame.sprite.Sprite):
    #constructor for bones
        def __init__(self):
            super().__init__() #invoke super class constructor
            self.image=pygame.image.load("bones.png").convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()

    #class for the player 
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() #invoke super class constructor
            self.image= pygame.Surface([15,15])
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()

            #speed/ start location
            self.rect.x =340
            self.rect.y =533
            self.xspeed = 3
            self.yspeed= 3

        #update screen (keyboard)
        def update(self):
            
            keys= pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -=self.xspeed
            if keys[pygame.K_RIGHT]:
                self.rect.x +=self.xspeed

            if keys[pygame.K_DOWN]:
                self.rect.y +=self.yspeed
            if keys[pygame.K_UP]:
                self.rect.y -=self.yspeed
            
            #boundrys
            if self.rect.left<20:
                self.rect.left=20
            if self.rect.right>450-50:
                self.rect.right=450-50

            if self.rect.bottom >700-10:
                self.rect.bottom=700-10
            if self.rect.top < 50:
                self.rect.top =50
   

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([5, 320])
            self.image.fill(RED)
            self.rect = self.image.get_rect()

    pygame.display.set_caption("OPERATION LEVEL 1")

    #create allSprites and a mobs group
    allsprites = pygame.sprite.Group()
    mobs= pygame.sprite.Group()
    reds= pygame.sprite.Group()

    #create 11 mobs and put them into allsprites and mobs
    mob= Operation()
    mob.rect.x= 70
    mob.rect.y= 600
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 150
    mob.rect.y= 430
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 300
    mob.rect.y= 199
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 439
    mob.rect.y= 222
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 190
    mob.rect.y= 200
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 280
    mob.rect.y= 500
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 190
    mob.rect.y= 490
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 90
    mob.rect.y= 550
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 220
    mob.rect.y= 330
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 100
    mob.rect.y= 123
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 300
    mob.rect.y= 400
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 10
    mob.rect.y= 140
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 100
    mob.rect.y= 200
    allsprites.add(mob)
    mobs.add(mob)

    mob= Operation()
    mob.rect.x= 340
    mob.rect.y= 50
    allsprites.add(mob)
    mobs.add(mob)

    #walls of the operation
    pygame.draw.rect(screen, RED, (5, 320,80,80))
    pygame.draw.rect(screen, RED, (5, 320,130,350))
    pygame.draw.rect(screen, RED, (5, 320,180,80))
    pygame.draw.rect(screen, RED, (5, 320,230,350))
    pygame.draw.rect(screen, RED, (5, 320,280,80))
    pygame.draw.rect(screen, RED, (5, 320,320,350))
    pygame.display.flip()
    

    #red enemies that user may not touch or (2 point will be removed)
    #1
    red= Enemy()
    red.rect.x= 80
    red.rect.y= 80
    allsprites.add(red)
    reds.add(red)

    #2
    red= Enemy()
    red.rect.x= 130
    red.rect.y= 350
    allsprites.add(red)
    reds.add(red)

    #3
    red= Enemy()
    red.rect.x= 180
    red.rect.y= 80
    allsprites.add(red)
    reds.add(red)

    #4
    red= Enemy()
    red.rect.x= 230
    red.rect.y= 350
    allsprites.add(red)
    reds.add(red)

    #5
    red= Enemy()
    red.rect.x= 280
    red.rect.y= 80
    allsprites.add(red)
    reds.add(red)

    #6
    red= Enemy()
    red.rect.x= 330
    red.rect.y= 350
    allsprites.add(red)
    reds.add(red)

    #SOUND
    sound= pygame.mixer.Sound("buzzz.wav")
    sound2= pygame.mixer.Sound("done.wav")
    sound3= pygame.mixer.Sound("clappp.wav")
    sound4= pygame.mixer.Sound("wave.wav")

    #create a player and add to sprite group
    player= Player()
    allsprites.add(player)
    score = 0


    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 55)
    frame_count = 0
    frame_rate = 30
    start_time = 30 #user has 30 seconds

    #speed
    x, y = 340, 533
    xspeed =5
    yspeed=5


    #main game loop
    running= True
    while running:
        #events loop
        for event in pygame.event.get(): #list of all events (mouse)
           #print(event)
            if event.type == pygame.QUIT:
                running= False

        #collision detection
        hitList= pygame.sprite.spritecollide(player,mobs,True)
        badList= pygame.sprite.spritecollide(player,reds,True)

        #logic
        allsprites.update()

        #draw
        screen.fill(WHITE)
        screen.blit(bg, [0,0])
        allsprites.draw(screen)
        pygame.display.flip()

        #walls of the operation
        pygame.draw.rect(screen, RED, (80,80,5, 320))
        pygame.draw.rect(screen, RED, (130,350,5, 320))
        pygame.draw.rect(screen, RED, (180,80,5, 320))
        pygame.draw.rect(screen, RED, (230,350,5, 320))
        pygame.draw.rect(screen, RED, (280,80,5, 320))
        pygame.draw.rect(screen, RED, (330,350,5, 320))
        
        #timer
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0 
     
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
     
        # Use python string formatting to format in leading zeros
        output_string = "Timer: {0:02}:{1:02}".format(minutes, seconds)
     
        # Time blit to the screen
        text = font.render(output_string, True, YELLOW)
        screen.blit(text, [0, 50])
        
        #score
        for deadmob in range(len(badList)):
            score= score - 2
            #sound
            sound4.play()
            
        for deadmob in range(len(hitList)):
            score= score + 1
            #SOUND
            sound.play()
        #move on to level 2  
        if score == 10:
            sound2.play()
            cont()
            level2()
        
        #stop game       
        elif score != 10 and total_seconds == 0:
            timeup()
                
        #score on screen
        text= font.render(f"Score:{score}/10", True , YELLOW)
        screen.blit(text, (10,10))
        
        
        pygame.display.flip()
     
        # Limit frames per second
        clock.tick(frame_rate)
        frame_count += 1
        
    pygame.quit()




##################
#LEVEL 2
##################


#level 2 rules 
def cont():
    intro = True
    #While loop to ensure the start screen stays until when needed
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                running = False
                pygame.quit()
                
            #If the user clicks "p", the game will start
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                #If the user clicks "q", pygame will quit
                if event.key == pygame.K_q:
                    intro = False
                    running = False
                    pygame.quit()
                    
        #Fill the pygame window with the desired color
        screen.fill(BLACK)
        #Set up and render the message that you would like in the start screen by calling the message function which we defined earlier

        screen.fill(BLACK)
        start = pygame.image.load("conttt.png")
        screen.blit(start, [0,0])
        message("GOOD LUCK!", BLUE, (150, 530), mfont)
        message("Press 'P' to play or 'Q' to quit", BLUE, (50, 600), mfont)
        
        #Update the display screen so that all changes are shown on the pygame window
        pygame.display.update()
        #Set the frame rate so that when the user chooses to continue or quit the wait time is adequete
        clock.tick(10)
    
        
#function for when the user wins
def done():
    intro = True
    #While loop to ensure the start screen stays until when needed
    while intro:
        screen.fill(BLACK)
        #Set up and render the message that you would like in the start screen by calling the message function which we defined earlier
        message("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", YELLOW, (0, 50), mfont)
        message("THANK YOU FOR SAVING BOBS LIFE", GREEN, (0, 100), mfont)
        message("IT COULDNT HAVE BEEN DONE", BLUE, (40, 350), mfont)
        message("WITHOUT YOU!", RED, (125, 400), mfont)
        message("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", YELLOW, (0, 200), mfont)
        #Update the display screen so that all changes are shown on the pygame window
        pygame.display.update()
        #Set the frame rate so that when the user chooses to continue or quit the wait time is adequete
        clock.tick(10) 

#function for losing game over
def timeup():
    intro = True
    #While loop to ensure the start screen stays until when needed
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                running = False
                pygame.quit()

        screen.fill(BLACK)
        #Set up and render the message that you would like in the start screen by calling the message function which we defined earlier
        message("TIMES UP!", WHITE, (150, 10), mfont)
        message("THANK YOU FOR PLAYING", WHITE, (50, 100), mfont)
        message("Press 'P' to play again or 'Q' to quit", BLUE, (10, 500), mfont)
        #Update the display screen so that all changes are shown on the pygame window
        pygame.display.update()
                
            #If the user clicks "p", the game will start
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    startScreen()
                    Level1()
                    
                    
                #If the user clicks "q", pygame will quit
                if event.key == pygame.K_q:
                    intro = False
                    running = False
                    pygame.quit()
                    

            #Set the frame rate so that when the user chooses to continue or quit the wait time is adequete
            clock.tick(10)


    
#function for level 2    
def level2(): 
    class Operation(pygame.sprite.Sprite):
        #constructor
        def __init__(self):
            super().__init__() #invoke super class constructor
            self.image=pygame.image.load("heart.png").convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() #invoke super class constructor
            self.image= pygame.Surface([10,10])
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()

               #speed/ start location
            self.rect.x =340
            self.rect.y =533
            self.xspeed = 3
            self.yspeed= 3

        def update(self):
            
            keys= pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -=self.xspeed
            if keys[pygame.K_RIGHT]:
                self.rect.x +=self.xspeed

            if keys[pygame.K_DOWN]:
                self.rect.y +=self.yspeed
            if keys[pygame.K_UP]:
                self.rect.y -=self.yspeed
            
            #boundrys
            if self.rect.left<20:
                self.rect.left=20
            if self.rect.right>450-50:
                self.rect.right=450-50

            if self.rect.bottom >700-10:
                self.rect.bottom=700-10
            if self.rect.top < 50:
                self.rect.top =50
            
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([5, 320])
            self.image.fill(RED)
            self.rect = self.image.get_rect()

    #SOUND
    sound= pygame.mixer.Sound("buzzz.wav")
    sound2= pygame.mixer.Sound("done.wav")
    sound3= pygame.mixer.Sound("clappp.wav")
    sound4= pygame.mixer.Sound("wave.wav")
    
    #create allSprites and a mobs group
    allsprites = pygame.sprite.Group()
    mobs= pygame.sprite.Group()
    reds= pygame.sprite.Group()

    #setting up screen for level 2
    screen= pygame.display.set_mode(SIZE)
    bg = pygame.image.load("BOBSS.png")
    pygame.display.set_caption("OPERATION LEVEL 2")

    #create 35 mobs and put them into allsprites and mobs
    for i in range(35):
        mob= Operation()
        mob.rect.x= random.randint(0+100, WIDTH-50)
        mob.rect.y= random.randint(0+100, HEIGHT-50)
        allsprites.add(mob)
        mobs.add(mob)

    #red enemies that user may not touch or (3 point will be removed)

    #1
    red= Enemy()
    red.rect.x= 80
    red.rect.y= 80
    allsprites.add(red)
    reds.add(red)

    #2
    red= Enemy()
    red.rect.x= 130
    red.rect.y= 350
    allsprites.add(red)
    reds.add(red)

    #3
    red= Enemy()
    red.rect.x= 180
    red.rect.y= 80
    allsprites.add(red)
    reds.add(red)

    #4
    red= Enemy()
    red.rect.x= 230
    red.rect.y= 350
    allsprites.add(red)
    reds.add(red)

    #5
    red= Enemy()
    red.rect.x= 280
    red.rect.y= 80
    allsprites.add(red)
    reds.add(red)

    #6
    red= Enemy()
    red.rect.x= 330
    red.rect.y= 350
    allsprites.add(red)
    reds.add(red)


    #create a player and add to sprite group
    player= Player()
    allsprites.add(player)
    score = 0

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 55)
    frame_count = 0
    frame_rate = 30
    start_time = 30 #user has 30 seconds

    #speed
    x, y = 340, 533
    xspeed =5
    yspeed=5


    #main game loop
    running= True
    while running:
        #events loop
        for event in pygame.event.get(): #list of all events (mouse)
            #print(event)
            if event.type == pygame.QUIT:
                running= False

        #collision detection
        hitList= pygame.sprite.spritecollide(player,mobs,True)
        badList= pygame.sprite.spritecollide(player,reds,True)

        #logic
        allsprites.update()

        #draw
        screen.fill(WHITE)
        screen.blit(bg, [0,0])
        allsprites.draw(screen)
        pygame.display.flip()

        #walls of the operation
        pygame.draw.rect(screen, RED, (80,80,5, 320))
        pygame.draw.rect(screen, RED, (130,350,5, 320))
        pygame.draw.rect(screen, RED, (180,80,5, 320))
        pygame.draw.rect(screen, RED, (230,350,5, 320))
        pygame.draw.rect(screen, RED, (280,80,5, 320))
        pygame.draw.rect(screen, RED, (330,350,5, 320))

        #timer
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0
     
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
     
        # Use python string formatting to format in leading zeros
        output_string = "Timer: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
        text = font.render(output_string, True, BLUE)
        screen.blit(text, [0, 50])
        
        #score
        for deadmob in range(len(badList)):
            score= score - 3
            #sound
            sound4.play()
            
        for deadmob in range(len(hitList)):
            score= score + 1
            sound.play()

        #WIN!
        if score == 30:
            sound3.play()
            done()
                
        #LOSE!       
        if score != 30 and total_seconds == 0:
            timeup()
            
        #printing score on the screen     
        text= font.render(f"Score:{score}/30", True , BLUE)
        screen.blit(text, (0,0))
        pygame.display.flip()

     
        # Limit frames per second
        frame_count += 1
        clock.tick(frame_rate)

    pygame.quit()

#calling functions
startScreen()
Level1()

