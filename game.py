from config import Config
from apple import Apple
from snake import Snake
import pygame
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WIN_WIDTH, Config.WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BAISCFONT = pygame.font.Font("freesansbold.ttf", 18)
        pygame.display.set_caption("Wormy")
        self.apple = Apple()
        self.snake = Snake()

    def draw_score(self, score):
        score_surf = self.BAISCFONT.render(
            "Score: %s" % (score), True, Config.WHITE)
        score_rect = score_surf.get_rect()
        score_rect.topleft = (Config.WIN_WIDTH-120, 10)
        self.screen.blit(score_surf, score_rect)

    def draw_worm(self):
        for coord in self.snake.worm_coords:
            x = coord["x"] * Config.CELLSIZE
            y = coord["y"] * Config.CELLSIZE
            worm_segment_rect = pygame.Rect(
                x, y, Config.CELLSIZE, Config.CELLSIZE)
            pygame.draw.rect(self.screen, Config.DARKGREEN, worm_segment_rect)
            worm_inner_segment_rect = pygame.Rect(
                x+4, y+4, Config.CELLSIZE-8, Config.CELLSIZE-8)
            pygame.draw.rect(self.screen, Config.DARKGREEN,
                             worm_inner_segment_rect)

    def draw_apple(self):
        x = self.apple.x * Config.CELLSIZE
        y = self.apple.y * Config.CELLSIZE

        apple_rect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)

        pygame.draw.rect(self.screen, Config.RED, apple_rect)

    def draw_grid(self):
        for x in range(0, Config.WIN_WIDTH, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGREY,
                             (x, 0), (x, Config.WIN_HEIGHT))

        for y in range(0, Config.WIN_HEIGHT, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGREY,
                             (0, y), (Config.WIN_WIDTH, y))

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        self.draw_grid()
        self.draw_worm()
        self.draw_apple()
        self.draw_score(len(self.snake.worm_coords)-3)
        pygame.display.update()
        self.clock.tick(Config.FBS)

    def reset_game(self):
        del self.apple
        del self.snake
        self.apple = Apple()
        self.snake = Snake()

    def is_game_over(self):
        if self.snake.worm_coords[self.snake.HEAD]["x"] == -1 or self.snake.worm_coords[self.snake.HEAD]["x"] == Config.CELLWIDTH or self.snake.worm_coords[self.snake.HEAD]["y"] == -1 or self.snake.worm_coords[self.snake.HEAD]["y"] == Config.CELLHEGHT:
            return self.reset_game()

        for wormbody in self.snake.worm_coords[1:]:
            if wormbody["x"] == self.snake.worm_coords[self.snake.HEAD]["x"] and wormbody["y"] == self.snake.worm_coords[self.snake.HEAD]["y"]:
                return self.reset_game()

    def check_for_key_press(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()
        key_up_events = pygame.event.get(pygame.KEYUP)

        if len(key_up_events) == 0:
            return None
        if key_up_events[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        return key_up_events[0].key

    def handl_key_event(self, event):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.dirction != self.snake.RIGHT:
            self.snake.dirction = self.snake.LEFT

        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.dirction != self.snake.LEFT:
            self.snake.dirction = self.snake.RIGHT

        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.dirction != self.snake.DOWN:
            self.snake.dirction = self.snake.UP

        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.dirction != self.snake.UP:
            self.snake.dirction = self.snake.DOWN

        elif event.key == pygame.K_ESCAPE:
            pygame.quit()

    def draw_press_key_msg(self):
        press_key_surf = self.BAISCFONT.render(
            "press a key to play", True, Config.DARKGREEN)
        press_key_rect = press_key_surf.get_rect()
        press_key_rect.topleft = (Config.WIN_WIDTH-200, Config.WIN_HEIGHT - 30)
        self.screen.blit(press_key_surf, press_key_rect)

    def display_game_over(self):
        game_over_font = pygame.font.Font("freesansbold.ttf", 150)
        game_surf = game_over_font.render("Game", True, Config.WHITE)
        over_surf = game_over_font.render("Over", True, Config.WHITE)
        game_rect = game_surf.get_rect()
        over_rect = over_surf.get_rect()
        game_rect.midtop = (Config.WIN_WIDTH/2, 10)
        over_rect.midtop = (Config.WIN_WIDTH/2, game_rect.height+10+25)

        self.screen.blit(game_surf, game_rect)
        self.screen.blit(over_surf, over_rect)

        self.draw_press_key_msg()

        pygame.display.update()
        pygame.time.wait(500)

        self.check_for_key_press()
        while True:
            if self.check_for_key_press():
                pygame.event.get()
                return

    def show_start_screen(self):
        title_font = pygame.font.Font("freesansbold.ttf", 100)
        title_surf1 = title_font.render("Wormy!", True, Config.DARKGREEN)
        title_surf2 = title_font.render("Wormy!", True, Config.GREEN)

        dgrees1 = 0
        dgrees2 = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
            self.screen.fill(Config.BG_COLOR)
            rotated_surf1 = pygame.transform.rotate(title_surf1, dgrees1)
            rotated_rect1 = rotated_surf1.get_rect()
            rotated_rect1.center = (Config.WIN_WIDTH/2, Config.WIN_HEIGHT/2)
            self.screen.blit(rotated_surf1, rotated_rect1)

            rotated_surf2 = pygame.transform.rotate(title_surf2, dgrees2)
            rotated_rect2 = rotated_surf2.get_rect()
            rotated_rect2.center = (Config.WIN_WIDTH/2, Config.WIN_HEIGHT/2)
            self.screen.blit(rotated_surf2, rotated_rect2)

            self.draw_press_key_msg()
            pygame.display.update()
            self.clock.tick(Config.MENU_FBS)
            dgrees1 += 1
            dgrees2 += 2

    def run(self):
        self.show_start_screen()
        while True:
            self.game_loop()
            self.display_game_over()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    self.handl_key_event(event)

            self.snake.update(self.apple)
            self.draw()
            if self.is_game_over():
                break
        # self.screen.fill((255,255,255))
        # pygame.display.update()
        # self.clock.tick(60)
