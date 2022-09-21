import pygame


WIDTH = 700
HEIGHT = 700
BLUE = (0,162,232)
BLACK = (0,0,0)
WHITE = (255,255,255)
BOARD_IMAGE = "C:/Users/shira/Desktop/snakes and ladder/board1.png"
PLAYER_IMAGE = "C:/Users/shira/Desktop/snakes and ladder/boy2.png"



pygame.font.init()
QUESTION1 = "The materials that a person takes for his different usages are called natural resources."
QUESTION2 = "Airplane is the most environmentally friendly means of transportation."
QUESTION3 = "The main cause of water pollution is Sewage."
QUESTION4 = "Over 60% of the dumped trash in the landfill can be recycled."
QUESTION5 = "About 30% of the world's water is drinkable"
QUESTION6 = "A plastic cup is able to survive in the garbage pile without falling apart for about 400 years."
QUESTION7 = "The most polluting country in the world is the United States."
QUESTION8 = "The land that receives the least rain is Antarctica."
QUESTION9 = "Rain that contains chemicals that harm the environment is called - chemical rain."
QUESTION10 = "The most polluted city in the world is Delhi, India"
QUESTION11 = "Specify Earth Day means raising awareness of the earth's environmental protection."
QUESTION12 = "Paper recycling means saving trees. The trees breathe carbon dioxide and emit oxygen."
QUESTION13 = "The amount of times a glass can be recycled is unlimited."
QUESTION14 = "Plastic and glass rotting naturally over time."
QUESTION15 = "If you replace a regular light bulb with a Fluorescent light bulb, you can save about 50% energy."
list_of_questions = [QUESTION1,QUESTION2,QUESTION3,QUESTION4,QUESTION5,QUESTION6,QUESTION7,
                     QUESTION8,QUESTION9,QUESTION10,QUESTION11,QUESTION12,QUESTION13,QUESTION14,QUESTION15]
dict_of_questions = {QUESTION1: True,
                     QUESTION2: False,
                     QUESTION3: True,
                     QUESTION4: True,
                     QUESTION5: False,
                     QUESTION6: True,
                     QUESTION7: False,
                     QUESTION8: True,
                     QUESTION9: False,
                     QUESTION10: False,
                     QUESTION11: True,
                     QUESTION12: True,
                     QUESTION13: True,
                     QUESTION14: False,
                     QUESTION15: False
 }
WINDOW_HIGHT = 600
WINDOW_WIDTH = 700
SIZE = (WINDOW_WIDTH, WINDOW_HIGHT)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
QUESTION_FONT = pygame.font.SysFont("comicsans", 80)
ANSWEAR_FONT = pygame.font.SysFont("comicsans", 60)

LEFT = 1
SCROLL = 2
RIGHT = 3
