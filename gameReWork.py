#Imports
import pygame
import sys
import numpy as np
import random
import time

#Initialize pygame
pygame.init()

#---------------------#Music#-----------------------#

pygame.mixer.music.load("Sanctuary Guardian.mp3")
pygame.mixer.music.play(loops = -1)

#---------------------#Display Variables#-------------------#

width, height = 800, 600  #800 pixels by 600 pixels screen

#Colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Olive = (100,100,0)
Black = (0,0,0)
Yellow = (255, 255, 0)
White = (255, 255, 255)

Background_colour = Black

#--------------------#Player/Enemy properties#---------------#

Player_size = 10

Player_pos = [width/2, height/2]
 
Enemy_size = 10
Enemy_pos = [random.randint(Enemy_size,width - Enemy_size),0]
Enemy_list = [Enemy_pos]
Num_enemy = 100   #Number of enemies

Speed = 3

#----------Msicellaneous Game Settings-------#

#Screen
screen = pygame.display.set_mode((width,height))

game_over = False

#Game frame rate
clock = pygame.time.Clock()

#Allows keys to be held down to move character
pygame.key.set_repeat(1,40)

#set mouse cursor look
pygame.mouse.set_cursor(pygame.cursors.diamond)


#--------------#Enemy Functions#-----------------#

#This function places enemies around the edges
def drop_Zombs(enemy_list):
    delay = random.random()
    #Enemy Comes from the top
    if len(enemy_list) < Num_enemy and delay < 0.10:
        x_pos = random.randint(Enemy_size,width - Enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
    #Enemy comes from the right
    elif len(enemy_list) < Num_enemy and delay > 0.9:
        x_pos = 0
        y_pos = random.randint(Enemy_size, height - Enemy_size)
        enemy_list.append([x_pos, y_pos])
    #Enemy comes from the bottom
    elif len(enemy_list) < Num_enemy and delay > 0.2 and delay < 0.3:
        x_pos = random.randint(Enemy_size, width - Enemy_size)
        y_pos = height - Enemy_size
        enemy_list.append([x_pos, y_pos])
    #Enemy comes from the right    
    elif len(enemy_list) < Num_enemy and delay > 0.4 and delay < 0.5:
        x_pos = width
        y_pos = random.randint(Enemy_size, height - Enemy_size)
        enemy_list.append([x_pos, y_pos])

#This function determines how the enmies look
def draw_Zombs(enemy_list):
    for Enemy_pos in enemy_list:
        pygame.draw.rect(screen, Blue, (Enemy_pos[0], Enemy_pos[1], Enemy_size, Enemy_size))

#This function attracts the enemies to the player    
def update_zombs_pos(enemy_list, player_pos):
    for idx, Enemy_pos in enumerate(enemy_list):
        if Enemy_pos[1] >= 0 and Enemy_pos[1] < height:
            pass
            #Making enemy move towards player
            delay = random.random()
            if player_pos[0] > Enemy_pos[0] and delay < 0.3 and player_pos[1] > Enemy_pos[1]:
                Enemy_pos[0] += Speed
                Enemy_pos[1] += Speed
            elif player_pos[0] < Enemy_pos[0] and delay < 0.3 and player_pos[1] > Enemy_pos[1]:
                Enemy_pos[0] -= Speed
                Enemy_pos[1] += Speed
            elif player_pos[0] < Enemy_pos[0] and player_pos[1] < Enemy_pos[1] and delay < 0.3:
                Enemy_pos[0] -= Speed
                Enemy_pos[1] -= Speed
            elif player_pos[0] > Enemy_pos[0] and player_pos[1] < Enemy_pos[1] and delay < 0.3:
                Enemy_pos[0] += Speed
                Enemy_pos[1] -= Speed
        #If it gets off the screen
        else:
            enemy_list.pop(idx)
            

#----------------#Player Functions#-------------------#
def collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    
    if (e_x >= p_x and e_x < (p_x + Player_size)) or (p_x >= e_x and p_x < (e_x + Enemy_size)):
        if (e_y >= p_y and e_y < (p_y + Player_size)) or (p_y >= e_y and p_y < (e_y + Enemy_size)):
            return True
    return False

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if collision(enemy_pos, player_pos):
            return True
    return False



#--------------#Weapon Properties and functions#-------------#

bullet_size = 2
bulletspeed = 5
bullets = 100
Bullet_pos = [width/2, height/2, 0]
Bullet_list = [Bullet_pos]

def load_bullet(bullet_list):
    if event.type == pygame.KEYDOWN:
        if len(bullet_list) <= bullets and event.key == pygame.K_i:
            x_pos = Player_pos[0]
            y_pos = Player_pos[1]
            direction = 1
            bullet_list.append([x_pos, y_pos, direction])
        elif len(bullet_list) <= bullets and event.key == pygame.K_k:
            x_pos = Player_pos[0]
            y_pos = Player_pos[1]
            direction = 2
            bullet_list.append([x_pos, y_pos, direction])
        elif len(bullet_list) <= bullets and event.key == pygame.K_l:
            x_pos = Player_pos[0]
            y_pos = Player_pos[1]
            direction = 3
            bullet_list.append([x_pos, y_pos, direction])
        elif len(bullet_list) <= bullets and event.key == pygame.K_j:
            x_pos = Player_pos[0]
            y_pos = Player_pos[1]
            direction = 4
            bullet_list.append([x_pos, y_pos, direction])
        
        
def draw_bullet(bullet_list):
    for Bullet_pos in bullet_list:
        pygame.draw.rect(screen, Yellow, (Bullet_pos[0], Bullet_pos[1], bullet_size, bullet_size))

def shoot_bullet(bullet_list):
    for idx, Bullet_pos in enumerate(bullet_list):
        if Bullet_pos[1] >= 0 and Bullet_pos[1] < height and Bullet_pos[2] == 1:
            Bullet_pos[1] -= bulletspeed
        elif Bullet_pos[1] >= 0 and Bullet_pos[1] < height and Bullet_pos[2] == 2:
            Bullet_pos[1] += bulletspeed
        elif Bullet_pos[0] >= 0 and Bullet_pos[0] < width and Bullet_pos[2] == 3:
            Bullet_pos[0] += bulletspeed
        elif Bullet_pos[0] >= 0 and Bullet_pos[0] < width and Bullet_pos[2] == 4:
            Bullet_pos[0] -= bulletspeed
        else:
            bullet_list.pop(idx)

#def enemy_collision(bullet_pos, enemy_pos):
#    if (bullet_pos[0] + bullet_size/2) > enemy_pos[0] and (bullet_pos[0] + bullet_size/2) < enemy_pos[0] + Enemy_size:
#        if (bullet_pos[1] + bullet_size/2) > enemy_pos[1] and (bullet_pos[1] + bullet_size/2) < enemy_pos[1] + Enemy_size:
#            return True
#    return False
#-------------Game Loop-----------#
   
while not game_over:
    
    #Quit Event
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Player_pos[0] -= Speed
    if keys[pygame.K_w]:
        Player_pos[1] -= Speed
    if keys[pygame.K_s]:
        Player_pos[1] += Speed
    if keys[pygame.K_d]:
        Player_pos[0] += Speed
      
    screen.fill(Background_colour)

    
#--------#Defining walls, Collisions, and platforms#-----------#

    if Player_pos[0] >= width:
        Player_pos[0] -= Player_size
    elif Player_pos[0] <= -2:
        Player_pos[0] += Player_size
    elif Player_pos[1] <= -2:
        Player_pos[1] += Player_size
#This part of the code makes you fall without glitching and i have no idea how
    elif Player_pos[1] >= height:
        Player_pos[1] -= Player_size
    
        
       
           
#Enemy Character  
    drop_Zombs(Enemy_list)
    update_zombs_pos(Enemy_list, Player_pos)
    draw_Zombs(Enemy_list)
    if collision_check(Enemy_list, Player_pos):
        game_over = True
        
    
#Bullets
    load_bullet(Bullet_list)
    shoot_bullet(Bullet_list)
    draw_bullet(Bullet_list)
    
        
#Main character    
    pygame.draw.rect(screen, Red, (Player_pos[0], Player_pos[1], Player_size, Player_size))

    
#60 fps    
    clock.tick(60)
    
    pygame.display.update()
        
