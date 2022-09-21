import random
import pygame
import const
pygame.font.init()


def print_question(list_of_questions):
    random_index = random.randint(0, 14)
    x = 35
    y = 110
    screen = pygame.display.set_mode(const.SIZE)
    pygame.display.set_caption("QUESTION")
    img = pygame.image.load(const.BACKGROUND_QUESTION).convert()
    screen.blit(img, (0, 0))
    random_question = list_of_questions.pop(random_index)
    random_question = random_question.split("\n")
    for i in range(len(random_question)):
        text = random_question[i]
        question_text = const.QUESTION_FONT.render(text, 1, const.BLACK)
        screen.blit(question_text, (30, y))
        y += 50
    true_text = const.ANSWEAR_FONT.render("TRUE", 1, const.BLACK)
    false_text = const.ANSWEAR_FONT.render("FALSE", 1, const.BLACK)
    screen.blit(true_text, (80, 410))
    screen.blit(false_text, (400, 410))
    pygame.display.flip()
    pygame.time.wait(1000)
    return random_index


def get_answear():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == const.LEFT:
            x, y = pygame.mouse.get_pos()
            if x >= 80 and x <= 260 and y >= 410 and y <= 470:
                return True
            elif x >= 400 and x <= 600 and y >= 410 and y <= 470:
                return False


def check_answer(random_index, question_dict, list_of_questions):
    question = list_of_questions[random_index]
    answer = get_answear()
    if question_dict[question] == answer:
        return True
    else:
        return False


def open_question(list_loc):
    if list_loc[0] == 140 and list_loc[1] == 560:
        random_index = print_question(const.list_of_questions)
        return check_answer(random_index, const.dict_of_questions, const.list_of_questions)
    if list_loc[1] == 420 and (list_loc[0] == 280 or list_loc[0] == 560):
        random_index = print_question(const.list_of_questions)
        return check_answer(random_index, const.dict_of_questions, const.list_of_questions)
    if list_loc[1] == 140 and list_loc[0] == 280:
        random_index = print_question(const.list_of_questions)
        return check_answer(random_index, const.dict_of_questions, const.list_of_questions)
    if list_loc[1] == 0 and (list_loc[0] == 140 or list_loc[0] == 420):
        random_index = print_question(const.list_of_questions)
        return check_answer(random_index, const.dict_of_questions, const.list_of_questions)

