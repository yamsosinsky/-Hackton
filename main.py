import pygame
import const
import random
import sys



pygame.init()
size = (const.WIDTH, const.HEIGHT)
screen1 = pygame.display.set_mode(size)
pygame.display.set_caption("ladder and snake:")
img = pygame.image.load(const.BOARD_IMAGE)
screen1.blit(img, (0,0))
player_img = pygame.image.load(const.PLAYER_IMAGE)
player_img.set_colorkey(const.BLACK)
screen1.blit(player_img, (0,560))#התחלתי
pygame.display.flip()

def first_screen():
    pygame.init()
    size = (const.WIDTH, const.HEIGHT)
    screen1 = pygame.display.set_mode(size)
    pygame.display.set_caption("ladder and snake:")
    img = pygame.image.load(const.BOARD_IMAGE)
    screen1.blit(img, (0, 0))
    player_img = pygame.image.load(const.PLAYER_IMAGE)
    player_img.set_colorkey(const.BLACK)
    screen1.blit(player_img, (0, 560))  # התחלתי
    pygame.display.flip()
    return screen1

def set_screen(list_loc):
    pygame.init()
    size = (const.WIDTH, const.HEIGHT)
    screen1 = pygame.display.set_mode(size)
    pygame.display.set_caption("ladder and snake:")
    img = pygame.image.load(const.BOARD_IMAGE)
    screen1.blit(img, (0, 0))
    player_img = pygame.image.load(const.PLAYER_IMAGE)
    player_img.set_colorkey(const.BLACK)
    screen1.blit(player_img, (list_loc[0], list_loc[1]))  # התחלתי
    pygame.display.flip()

def random_steps():
    pygame.init()
    size = (const.WIDTH, const.HEIGHT)
    screen1 = pygame.display.set_mode(size)
    pygame.display.set_caption("steps:")
    font = pygame.font.SysFont("Loads a number...", 100)
    load = font.render("Loads a number...", True, const.WHITE)
    screen1.blit(load, (70, 300))
    pygame.display.flip()
    pygame.time.wait(2000)
    x = random.randint(1, 5)
    font = pygame.font.SysFont("your number of steps is:", 50)
    load2 = font.render("your number of steps is:", True, const.WHITE)
    screen1.blit(load2, (120, 400))
    if x == 1:
        font = pygame.font.SysFont("1", 100)
        load2 = font.render("1", True, const.WHITE)
        screen1.blit(load2, (300, 500))
    elif x == 2:
        font = pygame.font.SysFont("2", 100)
        load2 = font.render("2", True, const.WHITE)
        screen1.blit(load2, (300, 500))
    elif x == 3:
        font = pygame.font.SysFont("3", 100)
        load2 = font.render("3", True, const.WHITE)
        screen1.blit(load2, (300, 500))
    elif x == 4:
        font = pygame.font.SysFont("4", 100)
        load2 = font.render("4", True, const.WHITE)
        screen1.blit(load2, (300, 500))
    elif x == 5:
        font = pygame.font.SysFont("5", 100)
        load2 = font.render("5", True, const.WHITE)
        screen1.blit(load2, (300, 500))
    else:
        font = pygame.font.SysFont("6", 100)
        load2 = font.render("6", True, const.WHITE)
        screen1.blit(load2, (300, 500))
    pygame.display.flip()
    pygame.time.wait(2000)

    return x

def move_player(num,list_loc):
    for i in range(num):
        if list_loc[0] == 560 and list_loc[1] ==0:
            j = num -i
            for x in range(j):
                list_loc[0] -= 140
            set_screen(list_loc)
            pygame.time.wait(500)
            break
        elif (list_loc[1] == 560 or list_loc[1] == 280 or list_loc[1] == 0) and not list_loc[0] == 560:
            list_loc[0] += 140
            set_screen(list_loc)
            pygame.time.wait(500)

        elif (list_loc[1] == 560 or list_loc[1] == 280 or list_loc[1] == 0) and list_loc[0] == 560:
            list_loc[1] -= 140
            set_screen(list_loc)
            pygame.time.wait(500)

        elif (list_loc[1] == 420 or list_loc[1] == 140 ) and not list_loc[0] == 0:
            list_loc[0] -= 140
            set_screen(list_loc)
            pygame.time.wait(500)

        elif (list_loc[1] == 420 or list_loc[1] == 140 ) and list_loc[0] == 0:
            list_loc[1] -= 140
            set_screen(list_loc)
            pygame.time.wait(500)

    return list_loc

first_screen()
list_loc = [0,560]


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                num_of_steps = random_steps()
                list_loc = move_player(num_of_steps,list_loc)
                set_screen(list_loc)
                print(list_loc)
        if list_loc == [560,0]:
            print("win")
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
pygame.quit()