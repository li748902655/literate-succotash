class Settings():
    # 存储飞船所有设置的类
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (230,230,20)

        # 飞船的设置

        self.ship_limit = 3

        # 子弹设置

        self.bullet_width = 300
        self.bullet_height = 5
        self.bullet_color = 60,20,65
        self.bullets_allowed = 4

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏节奏加快
        self.speedup_scale = 1.2
        # 得分倍数
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随着游戏进行，难度增加
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 1

        # fleet_direction为1 表示向右移动，-1 表示向左
        self.fleet_direction = 1

    #     计分
        self.alien_points = 1


    def increase_speed(self):
        # 提高游戏速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)