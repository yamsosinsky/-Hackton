import random
import pygame
import const
pygame.font.init()


def print_question(list_of_questions):
    random_index = random.randint(0, len(list_of_questions) - 1)
    screen = pygame.display.set_mode(const.SIZE)
    pygame.display.set_caption("QUESTION")
    screen.fill(const.WHITE)
    random_question = list_of_questions.pop(random_index)
    question_text = const.QUESTION_FONT.render(random_question, 1, const.BLACK)
    true_text = const.ANSWEAR_FONT.render("TRUE", 1, const.BLACK)
    false_text = const.ANSWEAR_FONT.render("FALSE", 1, const.BLACK)
    screen.blit(question_text, (30, 210))
    screen.blit(true_text, (80, 410))
    screen.blit(false_text, (400, 410))
    pygame.display.flip()
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


def open_question():
    pass