# Generic Game Object to be parent class of all GameObjects
class GameObject:

    def __init__(self, type='game_object_type', name='game_object_name', hit_points=1, attack_value=1,
                 image='game_object_image', image_width=0, image_height=0,
                 xcor=0, ycor=0, lr_speed=0, ud_speed=0, x_dir=None, y_dir=None, last_lr_move=None, last_ud_move=None):
        self.type = type
        self.name = name
        self.hit_points = hit_points;
        self.attack_value = attack_value
        self.image = image
        self.image_width = image_width
        self.image_height = image_height
        self.xcor = xcor
        self.ycor = ycor
        self.lr_speed = lr_speed
        self.ud_speed = ud_speed
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.last_lr_move = last_lr_move
        self.last_ud_move = last_ud_move

    def __call__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        return self

    def move_up(self):
        self.ycor -= self.ud_speed

    def move_down(self):
        self.ycor += self.ud_speed

    def move_left(self):
        self.xcor -= self.lr_speed

    def move_right(self):
        self.xcor += self.lr_speed

    def continue_move(self):
        if self.y_dir == 'UP' or self.y_dir == 'NORTH':
            self.move_up()
        elif self.y_dir == 'DOWN' or self.y_dir == 'SOUTH':
            self.move_down()
        if self.x_dir == 'RIGHT' or self.x_dir == 'EAST':
            self.move_right()
        elif self.x_dir == 'LEFT' or self.x_dir == 'WEST':
            self.move_left()

    def collide_with(self, game_object):
        x = 0
        y = 0
        if 0 < self.xcor - game_object.xcor < abs(game_object.image_width - 10):
            x = 1
        elif 0 < game_object.xcor - self.xcor < abs(self.image_width - 10):
            x = 1
        if 0 < self.ycor - game_object.ycor < abs(game_object.image_height - 10):
            y = 1
        elif 0 < game_object.ycor - self.ycor < abs(self.image_height - 10):
            y = 1
        if x * y:
            return True

    def level_up(self, increase_atk=1, increase_hp=1):
        self.attack_value += increase_atk
        self.hit_points += increase_hp

    def destroy(self):
        del self
