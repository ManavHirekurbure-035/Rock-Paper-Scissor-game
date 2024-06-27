import pygame   
import random   # to generate random choice for computer 

pygame.init()

screenHeight = 550
screenWidth = 800
Text_color = (255, 255, 255)



player_clicked = False  # to check if player has selected an option
update_score = False

player_score = 0
computer_score = 0


choice_list = ["rock", "paper", "scissor"]  
playerChoice = "" 
computerChoice = ""
round_winner=""

# all types of fonts used
medium_font = pygame.font.SysFont('comicsansms', 20)
large_font = pygame.font.SysFont('comicsansms', 30)
extralarge_font = pygame.font.SysFont('comicsansms', 60)

# initialize game screen
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Rock Paper Scissor')

# load images
# rock image
rock_img = pygame.transform.scale(pygame.image.load('./images/rock.png').convert_alpha(),(100,100))
rock_rect = rock_img.get_rect()
rock_rect.center = (250, 385)

# paper image
paper_img = pygame.transform.scale(pygame.image.load('./images/paper.png').convert_alpha(),(100,100))
paper_rect = paper_img.get_rect()
paper_rect.center = (400, 385)

# scissor image
scissor_img = pygame.transform.scale(pygame.image.load('./images/scissor.png').convert_alpha(),(100,100))
scissor_rect = scissor_img.get_rect()
scissor_rect.center = (550, 385)

# text displayed on game screen
player_text = large_font.render('YOU', True, Text_color)
computer_text = large_font.render('COMPUTER', True, Text_color)
selection_text = medium_font.render('Select your choice', True, Text_color)

# images displayed after selection (enlarged images)
qmark_img = pygame.transform.scale(pygame.image.load('./images/questionMark.png').convert_alpha(),(150,150))
rock_img1 = pygame.transform.scale(pygame.image.load('./images/rock.png').convert_alpha(),(150,150))
paper_img1 = pygame.transform.scale(pygame.image.load('./images/paper.png').convert_alpha(),(150,150))
scissor_img1 = pygame.transform.scale(pygame.image.load('./images/scissor.png').convert_alpha(),(150,150))

# various button images
play_again_img = pygame.transform.scale(pygame.image.load('./images/play_again.png').convert_alpha(),(110,50))
play_again_rect = play_again_img.get_rect()
play_again_rect.center = (300, 500)

restart_img = pygame.transform.scale(pygame.image.load('./images/restart.png').convert_alpha(),(110,50))
restart_rect = restart_img.get_rect()
restart_rect.center = (500, 500)


# section background
choice_section_rect = pygame.Rect(150, 300, 500, 155)  # (x, y, width, height)
score_section_rect = pygame.Rect(0, 0, 800, 45)

# increment the score of winner
def score_update(winner_player, p_score, c_score) :
    if winner_player == "You":
        p_score +=1
    elif winner_player == "Computer":
        c_score +=1
    
    return p_score, c_score

# display score on screen
def score_display(player,computer) :

    player_text = medium_font.render('You : '+str(player), True, Text_color)
    computer_text = medium_font.render('Computer : '+str(computer), True, Text_color)
    screen.blit(player_text,(15,7))
    screen.blit(computer_text,(665,7))

# select random choice for computer from choice_list (rock, paper, scissor)
def compchoice() :
    return random.choice(choice_list)
    
# check for the winner and return the result
def winner() :
    # generate computer choice
    cChoice = compchoice()

    if playerChoice == "rock" and cChoice == "scissor" or  playerChoice == "scissor" and cChoice == "paper" or playerChoice == "paper" and cChoice == "rock":
        win_player = "You"        
    elif playerChoice == cChoice :
        win_player = "Draw"
    else:
        win_player = "Computer"
        
    return cChoice, win_player
    
# update game screen according to the winner   
def display_winner(player_won) :    
    pygame.draw.rect(screen, "#FD5959", choice_section_rect)
    if player_won == "You" or player_won == "Computer" :
        winner_text = extralarge_font.render(player_won +" WON", True, Text_color) 
    else:
        winner_text = extralarge_font.render("It is a Draw", True, Text_color) 
    winner_rect = winner_text.get_rect()
    winner_rect.center = (400,370)
    screen.blit(winner_text, winner_rect)



# game loop
run = True
while run:
    # screen.blit(text_surface, (50,50))    
    screen.fill('#373737')    

    pygame.draw.rect(screen, "#FD5959", choice_section_rect)
    pygame.draw.rect(screen, "#FD5959", score_section_rect)

    screen.blit(player_text,(190,60))
    screen.blit(computer_text,(495,60))
    screen.blit(selection_text,(310,300))
    screen.blit(rock_img, rock_rect)
    screen.blit(paper_img, paper_rect)
    screen.blit(scissor_img, scissor_rect)   
    screen.blit(play_again_img, play_again_rect)
    screen.blit(restart_img, restart_rect)

    

    # display question mark when no option selected
    if playerChoice == "" and computerChoice == "":
        screen.blit(qmark_img, (150, 120)) 
        screen.blit(qmark_img, (500, 120))


    # event handler
    for event in pygame.event.get():
        
        # checks the option selected by user (rock, paper, scissor, play again, restart)
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if rock_rect.collidepoint(event.pos):
                if player_clicked == False :
                    
                    playerChoice = choice_list[0]
                    player_clicked = True
                    update_score = True
                    computerChoice, round_winner = winner()
                    
                    

            if paper_rect.collidepoint(event.pos):
                if player_clicked == False :
                    
                    playerChoice = choice_list[1]
                    player_clicked = True
                    update_score = True
                    computerChoice, round_winner = winner()     
                                 
                    

            if scissor_rect.collidepoint(event.pos):
                if player_clicked == False :
                      
                    playerChoice = choice_list[2]
                    player_clicked = True
                    update_score = True
                    computerChoice, round_winner = winner()   
                      
                      
                    

            if play_again_rect.collidepoint(event.pos):
                player_clicked = False
                playerChoice = ""
                computerChoice = ""
            
            if restart_rect.collidepoint(event.pos):
                player_clicked = False
                playerChoice = ""
                computerChoice = ""
                player_score = computer_score = 0
                  


        # quit game
        if event.type == pygame.QUIT:
            run = False
    
    if update_score :
        player_score, computer_score = score_update(round_winner, player_score, computer_score)
        update_score = False
    
    score_display(player_score, computer_score)
    

    # update screen only if player has selected their option
    if player_clicked : 
        if computerChoice == "rock" :
            screen.blit(rock_img1, (500, 120))
        elif computerChoice == "paper" :
            screen.blit(paper_img1, (500, 120))
        elif computerChoice == "scissor" :
            screen.blit(scissor_img1, (500, 120))

        if playerChoice == "rock" :
            screen.blit(rock_img1, (150, 120))
        elif playerChoice == "paper" :
            screen.blit(paper_img1, (150, 120))
        elif playerChoice == "scissor" :
            screen.blit(scissor_img1, (150, 120))
        # display the round winner
        display_winner(round_winner)
        

    pygame.display.update()  
    
pygame.quit()