import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

from alien import Alien
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('打飞机')

    # 创建play按钮
    play_button = Button(ai_settings, screen, "play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个存储子弹和外星人的编组
    bullets = Group()
    aliens = Group()

    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf. check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)
        # 重构该循环体，加入gf
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        if stats.game_active:
            ship.update()
            gf.update_bullets( ai_settings,screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb,  ship, aliens, bullets)
        gf.update_screen(ai_settings, screen,stats, sb, ship, aliens, bullets,play_button)

            #     每次循环都重绘主屏幕
            # 重构更新屏幕部分
            # screen.fill(ai_settings.bg_color)
            # ship.blitme()
            #     #可见属性
            # pygame.display.flip()



run_game()