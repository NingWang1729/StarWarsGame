import pygame


class Button:
    def __init__(self, display, x, y, width, height, text, font_type, font_size,
                 rr1, rg1, rb1, rr2, rg2, rb2, tr1, tg1, tb1, tr2, tg2, tb2, clicked=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mouse = pygame.mouse.get_pos()

        if self.over_button():
            pygame.draw.rect(display, (int(rr2), int(rg2), int(rb2)), (x, y, width, height))
            play_game_text = pygame.font.Font(font_type, font_size).render(str(text), True,
                                                                           (int(tr2), int(tg2), int(tb2)))
            display.blit(play_game_text,
                         play_game_text.get_rect(center=(int(x + width / 2), int(y + height / 2))))
        else:
            pygame.draw.rect(display, (int(rr1), int(rg1), int(rb1)), (x, y, width, height))
            play_game_text = pygame.font.Font(font_type, font_size).render(str(text), True,
                                                                           (int(tr1), int(tg1), int(tb1)))
            display.blit(play_game_text,
                         play_game_text.get_rect(center=(int(x + width / 2), int(y + height / 2))))

    def over_button(self):
        if self.x <= self.mouse[0] <= self.x + self.width and self.y <= self.mouse[1] <= self.y + self.height:
            return True
    # mouse = pygame.mouse.get_pos()
    # pygame.draw.rect(menu_display, (0, 0, 240), (int(display_width / 4), int(display_height / 2),
    #                                              int(display_width / 2), int(display_height / 4)))
    # play_game_text = pygame.font.Font(None, 100).render('Play Game', True, (240, 240, 0))
    # menu_display.blit(play_game_text,
    #                   play_game_text.get_rect(center=(int(display_width / 2), int(5 * display_height / 8))))
    #
    # if display_width / 4 <= mouse[0] <= display_width / 4 + display_width / 2:
    #   if display_height / 2 <= mouse[1] <= display_height / 2 + display_height / 4:
    #         pygame.draw.rect(menu_display, (0, 0, 255), (int(display_width / 4), int(display_height / 2),
    #                                                      int(display_width / 2), int(display_height / 4)))
    #         play_game_text = pygame.font.Font(None, 100).render('Play Game', True, (255, 255, 0))
    #         menu_display.blit(play_game_text,
    #                           play_game_text.get_rect(center=(int(display_width / 2), int(5 * display_height / 8))))

