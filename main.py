import pygame
screen_height = 600
screen_width = 400
screen = pygame.display.set_mode((screen_width, screen_height))
game = True
game_stage = "enter_size"
pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 30)


def draw_text(text):
    text_draw  = my_font.render("Арбуз верни деньги ", False, (33, 234, 23))
    screen.blit(text, (100, 100))

def draw_text(text):
    text_draw  = my_font.render("Арбуз верни деньги ", False, (33, 234, 23))
    screen.blit(text, (100, 100))

def button_to_text(button):
    if button == pygame.K_1:
        text = "1"
    elif button == pygame.K_2:
        text = " 2"
    elif button == pygame.K_3:
        text = " 3"
    elif button == pygame.K_4:
        text = " 4"
    elif button == pygame.K_5:
        text = " 5"
    elif button == pygame.K_6:
        text = " 6"


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key in [ pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,
                              pygame.K_0,pygame.k_x]



    screen.fill("black")
    pygame.draw.rect(screen, (21, 13, 238), (0, 0, 0, 0))
    if game_stage == "enter_size":
        draw_text( "test")


    pygame.display.update()






