import os
import random
import pygame

import Game_Object


class SpaceInvaders():

    def __init__(self):
        # Begin the game
        # background = webbrowser.open(
        #     "https://ia601203.us.archive.org/13/items/13BinarySunsetAlternate/21%20Scherzo%20for%20X-Wings.mp3",
        #     autoraise=False)
        # Test to see why Github uploaded via an old account....

        # Set up display parameters
        display_width = 800
        display_height = 800
        frames_per_second = 60
        self.pause = False

        # Set up score
        score = [0]
        # Set up display in game using parameters
        game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Space Invaders Game by Ning Wang')
        clock = pygame.time.Clock()
        clock.tick(frames_per_second)  # Not sure if this needs to be in the main game loop

        # Set up my spaceship design (Should be 100 x 100 pixels)
        self.my_spaceship = Game_Object.GameObject(type='Player', name='Player Spaceship', attack_value=1,
                                                   hit_points=10,
                                                   image='Millennium_Falcon.png', image_width=50, image_height=70,
                                                   xcor=int(display_width * 0.45), ycor=int(display_height * 0.8),
                                                   lr_speed=5, ud_speed=5)
        enemy_list = []
        ally_list = []

        def launch_ship(ship_type):
            if ship_type == -2:
                ally = Game_Object.GameObject(type='Ally', name='Ally X_Wing', hit_points=5, attack_value=2,
                                              image='X_Wing.png', image_width=50, image_height=56,
                                              xcor=random.randint(0, display_width - 50), ycor=display_height - 86,
                                              lr_speed=2, ud_speed=2)
            elif ship_type == -1:
                ally = Game_Object.GameObject(type='Ally', name='Ally Y_Wing', hit_points=3, attack_value=1,
                                              image='Y_Wing.png', image_width=50, image_height=50,
                                              xcor=random.randint(0, display_width - 50), ycor=display_height - 80,
                                              lr_speed=1, ud_speed=1)
            if ship_type == 1:
                enemy = Game_Object.GameObject(type='Enemy', name='Enemy Tie_Fighter', hit_points=1, attack_value=1,
                                               image='Tie_Fighter.png', image_width=50, image_height=45,
                                               xcor=random.randint(0, display_width - 50), ycor=0,
                                               lr_speed=1, ud_speed=1)

            elif ship_type == 2:
                enemy = Game_Object.GameObject(type='Enemy', name='Enemy Tie_Better_Fighter', hit_points=2,
                                               attack_value=2,
                                               image='Tie_Better_Fighter.png', image_width=50, image_height=45,
                                               xcor=random.randint(0, display_width - 50), ycor=0,
                                               lr_speed=2, ud_speed=1)
            elif ship_type == 3:
                enemy = Game_Object.GameObject(type='Enemy', name='Enemy Tie_Advanced_Fighter', hit_points=5,
                                               attack_value=3,
                                               image='Tie_Advanced_Fighter.png', image_width=60, image_height=45,
                                               xcor=random.randint(0, display_width - 50), ycor=0,
                                               lr_speed=2, ud_speed=2)
            elif ship_type == 5:
                enemy = Game_Object.GameObject(type='Enemy', name='Enemy Star_Destroyer', hit_points=500,
                                               attack_value=50,
                                               image='Star_Destroyer.png', image_width=300, image_height=300,
                                               xcor=random.randint(0, display_width - 400), ycor=-299,
                                               lr_speed=0, ud_speed=1)
                pygame.mixer.music.load('Sounds/Vader.wav')
                pygame.mixer.music.play(loops=-1)
            if ship_type > 0:
                enemy_list.append(enemy)
            elif ship_type < 0:
                ally_list.append(ally)

        bullet_list = []

        def shoot_bullet(bullet_type, hit_points, attack_value,
                         bullet_width, bullet_height,
                         xcor, ycor, x_dir, y_dir, lr_speed, ud_speed):
            bullet = Game_Object.GameObject(type=str(bullet_type), name=str(bullet_type),
                                            hit_points=hit_points, attack_value=attack_value,
                                            image=str(bullet_type) + '.png',
                                            image_width=bullet_width, image_height=bullet_height,
                                            xcor=xcor, ycor=ycor,
                                            lr_speed=lr_speed, ud_speed=ud_speed,
                                            x_dir=x_dir, y_dir=y_dir)
            bullet_list.append(bullet)

        def draw_object(game_object):
            game_display.blit(pygame.image.load('Pictures/' + game_object.image), (game_object.xcor, game_object.ycor))

        def draw_all():
            game_display.fill((0, 0, 0))
            for enemy in enemy_list:
                draw_object(enemy)
            for ally in ally_list:
                draw_object(ally)
            for bullet in bullet_list:
                draw_object(bullet)
            draw_object(self.my_spaceship)

        def move_all(time):
            for ship in enemy_list:
                if ship.name != 'Enemy Star_Destroyer':
                    if time % 2:
                        ship.ycor += int(ship.ud_speed)
                    if time % 250 == 0:
                        left_or_right = random.randint(0, 2)
                        if left_or_right:
                            ship.x_dir = 'RIGHT'
                        else:
                            ship.x_dir = 'LEFT'
                    if ship.xcor <= 0 and (ship.x_dir == 'LEFT' or ship.x_dir == 'WEST'):
                        ship.x_dir = 'RIGHT'
                    elif ship.xcor >= display_width - ship.image_width and (
                            ship.x_dir == 'RIGHT' or ship.x_dir == 'EAST'):
                        ship.x_dir = 'LEFT'
                    if ship.x_dir == 'RIGHT' or ship.x_dir == 'EAST':
                        ship.xcor += int(ship.lr_speed)
                    elif ship.x_dir == 'LEFT' or ship.x_dir == 'WEST':
                        ship.xcor -= int(ship.lr_speed)
                else:
                    if time % 10 == 0:
                        ship.ycor += int(ship.ud_speed)
            for ship in ally_list:
                if time % 2:
                    ship.ycor -= int(ship.ud_speed)
                if time % 250 == 0:
                    left_or_right = random.randint(0, 2)
                    if left_or_right:
                        ship.x_dir = 'RIGHT'
                    else:
                        ship.x_dir = 'LEFT'
                if ship.xcor <= 0 and (ship.x_dir == 'LEFT' or ship.x_dir == 'WEST'):
                    ship.x_dir = 'RIGHT'
                elif ship.xcor >= display_width - ship.image_width and (
                        ship.x_dir == 'RIGHT' or ship.x_dir == 'EAST'):
                    ship.x_dir = 'LEFT'
                if ship.x_dir == 'RIGHT' or ship.x_dir == 'EAST':
                    ship.xcor += int(ship.lr_speed)
                elif ship.x_dir == 'LEFT' or ship.x_dir == 'WEST':
                    ship.xcor -= int(ship.lr_speed)

            for bullet in bullet_list:
                if bullet.x_dir == 'RIGHT' or bullet.x_dir == 'EAST':
                    bullet.xcor += bullet.lr_speed
                elif bullet.x_dir == 'LEFT' or bullet.x_dir == 'WEST':
                    bullet.xcor -= bullet.lr_speed
                if bullet.y_dir == 'DOWN' or bullet.y_dir == 'SOUTH':
                    bullet.ycor += bullet.ud_speed
                elif bullet.y_dir == 'UP' or bullet.y_dir == 'NORTH':
                    bullet.ycor -= bullet.ud_speed
                if bullet.ycor > display_height or bullet.ycor < -bullet.image_height:
                    bullet_list.remove(bullet)
                    bullet.destroy()

        def check_crash():
            # Enemy collisions
            for enemy in enemy_list:
                for bullet in bullet_list:
                    if enemy.collide_with(bullet) and bullet.y_dir == 'UP':
                        if not self.pause:
                            os.system("afplay Sounds/Explosion.wav&")
                        enemy.hit_points -= bullet.attack_value
                        bullet_list.remove(bullet)
                        bullet.destroy()
                    if enemy.hit_points <= 0:
                        if enemy.name == 'Enemy Star_Destroyer':
                            print('win')
                            pygame.mixer.music.load('Sounds/Falcon_vs_The_TIE_Fighters.wav')
                            pygame.mixer.music.play(loops=-1)
                        enemy_list.remove(enemy)
                        enemy.destroy()
                        score[0] += 1
                        self.my_spaceship.level_up(increase_atk=0.1, increase_hp=0.1)
                        print(score[0])
                        break
            for ally in ally_list:
                for bullet in bullet_list:
                    if ally.collide_with(bullet) and bullet.y_dir == 'DOWN':
                        if not self.pause:
                            os.system("afplay Sounds/Explosion.wav&")
                        ally.hit_points -= bullet.attack_value
                        bullet_list.remove(bullet)
                        bullet.destroy()
                    if ally.hit_points <= 0:
                        ally_list.remove(ally)
                        ally.destroy()
                        score[0] -= 1
                        break
            # My collisions
            for bullet in bullet_list:
                if bullet.y_dir == 'DOWN' and self.my_spaceship.collide_with(bullet):
                    if not self.pause:
                        os.system("afplay Sounds/Explosion.wav&")
                    self.my_spaceship.hit_points -= bullet.attack_value
                    bullet_list.remove(bullet)
                    bullet.destroy()
            for enemy in enemy_list:
                if enemy.ycor >= display_height - enemy.image_height:
                    if not self.pause:
                        os.system("afplay Sounds/Explosion.wav&")
                    self.my_spaceship.hit_points -= enemy.hit_points
                    enemy_list.remove(enemy)
                    enemy.destroy()
            for ally in ally_list:
                if ally.ycor <= 0:
                    ally.ycor = display_height - ally.image_height
            if self.my_spaceship.hit_points <= 0:
                if not self.pause:
                    os.system("afplay Sounds/You_Exploded.wav&")
                    os.system("afplay Sounds/R2D2.wav&")
                # os.system("pkill firefox")
                return True

        def game_loop():
            afk = 0
            timer = 0
            cool_down = 0
            wave_timer = 0
            collide = False
            running = True  # Keeps the game running
            print('starting hp = ', self.my_spaceship.hit_points)

            # Main game loop
            while running:
                # Verifies each update
                if afk >= 1800:
                    running = False
                    print('You were kicked for inactivity')
                if timer % 200 == 0:
                    launch_ship(1)
                if score[0] > 10 and timer % 300 == 0:
                    launch_ship(2)
                if score[0] > 20 and timer % 600 == 0:
                    launch_ship(3)
                if score[0] > 30 and timer % 5000 == 0:
                    launch_ship(5)
                if score[0] > 15 and timer % 500 == 0:
                    launch_ship(-1)
                if score[0] > 30 and timer % 1000 == 0:
                    launch_ship(-2)
                if timer % 10 == 0:
                    shoot = False
                    for enemy in enemy_list:
                        if random.randint(0, 10) == 0:
                            if enemy.name == 'Enemy Tie_Fighter':
                                shoot = True
                                shoot_bullet('Red_Laser', 1, enemy.attack_value, 15, 45,
                                             enemy.xcor + int(enemy.image_width / 2),
                                             enemy.ycor + enemy.image_height,
                                             None, 'DOWN', 0, 5)
                            if enemy.name == 'Enemy Tie_Better_Fighter':
                                shoot = True
                                shoot_bullet('Red_Laser', 1, enemy.attack_value, 15, 45,
                                             enemy.xcor + int(enemy.image_width / 2),
                                             enemy.ycor + enemy.image_height,
                                             None, 'DOWN', 0, 5)
                            if enemy.name == 'Enemy Tie_Advanced_Fighter':
                                shoot = True
                                shoot_bullet('Red_Laser', 1, enemy.attack_value, 15, 45,
                                             enemy.xcor + 10, enemy.ycor + enemy.image_height,
                                             None, 'DOWN', 0, 5)
                                shoot_bullet('Red_Laser', 1, enemy.attack_value, 15, 45,
                                             enemy.xcor + enemy.image_width - 10,
                                             enemy.ycor + enemy.image_height,
                                             None, 'DOWN', 0, 5)
                    for ally in ally_list:
                        if random.randint(0, 8) == 0:
                            if ally.name == 'Ally Y_Wing':
                                    shoot = True
                                    shoot_bullet('Red_Laser', 1, ally.attack_value, 15, 45,
                                                 ally.xcor + int(ally.image_width / 2), ally.ycor + 45,
                                                 None, 'UP', 0, 5)
                            elif ally.name == 'Ally X_Wing':
                                shoot = True
                                shoot_bullet('Red_Laser', 1, ally.attack_value, 15, 45,
                                             ally.xcor, ally.ycor + 45,
                                             None, 'UP', 0, 5)
                                shoot = True
                                shoot_bullet('Red_Laser', 1, ally.attack_value, 15, 45,
                                             ally.xcor + ally.image_width, ally.ycor + 45,
                                             None, 'UP', 0, 5)

                    if not self.pause and shoot:
                        # os.system("afplay Sounds/TIE_Fighter_Fire.wav&")
                        os.system("afplay Sounds/Star_Destroyer_Fire.wav&")
                for event in pygame.event.get():
                    afk = 0
                    # Exits the game via clicking the X in the corner
                    if event.type == pygame.QUIT:
                        running = False
                    # Pressing keys to impact game
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        if event.key == pygame.K_p:
                            self.pause = not self.pause
                        if not self.pause:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                if self.my_spaceship.last_lr_move is None:
                                    self.my_spaceship.last_lr_move = pygame.K_LEFT
                                elif self.my_spaceship.last_lr_move == pygame.K_RIGHT:
                                    self.my_spaceship.last_lr_move = None
                            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                if self.my_spaceship.last_lr_move is None:
                                    self.my_spaceship.last_lr_move = pygame.K_RIGHT
                                elif self.my_spaceship.last_lr_move == pygame.K_LEFT:
                                    self.my_spaceship.last_lr_move = None
                            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                                if self.my_spaceship.last_ud_move is None:
                                    self.my_spaceship.last_ud_move = pygame.K_UP
                                elif self.my_spaceship.last_ud_move == pygame.K_DOWN:
                                    self.my_spaceship.last_ud_move = None
                            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                if self.my_spaceship.last_ud_move is None:
                                    self.my_spaceship.last_ud_move = pygame.K_DOWN
                                elif self.my_spaceship.last_ud_move == pygame.K_UP:
                                    self.my_spaceship.last_ud_move = None
                            elif event.key == pygame.K_RSHIFT:
                                self.my_spaceship.last_ud_move = None
                                self.my_spaceship.last_lr_move = None
                            elif event.key == pygame.K_SPACE:
                                if cool_down == 0:
                                    if score[0] < 50:
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int((self.my_spaceship.image_width - 15) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                    elif score[0] < 200:
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int(
                                                         (self.my_spaceship.image_width - 30) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int(
                                                         (self.my_spaceship.image_width + 30) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                    else:
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int(
                                                         (self.my_spaceship.image_width - 30) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int(
                                                         (self.my_spaceship.image_width - 15) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int(
                                                         (self.my_spaceship.image_width + 30) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                        shoot_bullet('Green_Laser', 1, self.my_spaceship.attack_value, 15, 45,
                                                     self.my_spaceship.xcor + int(
                                                         (self.my_spaceship.image_width + 15) / 2),
                                                     self.my_spaceship.ycor - 45,
                                                     None, 'UP', 0, 10)
                                    if not self.pause:
                                        os.system("afplay Sounds/Laser_Cannon.wav&")
                                    cool_down = timer
                                elif timer > cool_down + 5:
                                    cool_down = 0
                if 0 <= self.my_spaceship.xcor <= (display_width - 100) and (
                        display_height - 100) >= self.my_spaceship.ycor >= 0:
                    if self.my_spaceship.last_lr_move == pygame.K_LEFT:
                        self.my_spaceship.xcor -= self.my_spaceship.lr_speed
                    elif self.my_spaceship.last_lr_move == pygame.K_RIGHT:
                        self.my_spaceship.xcor += self.my_spaceship.lr_speed
                    if self.my_spaceship.last_ud_move == pygame.K_UP:
                        self.my_spaceship.ycor -= self.my_spaceship.ud_speed
                    elif self.my_spaceship.last_ud_move == pygame.K_DOWN:
                        self.my_spaceship.ycor += self.my_spaceship.ud_speed
                    if self.my_spaceship.ycor < (display_height - 110):
                        collide = False
                else:
                    if not self.pause:
                        os.system("afplay Sounds/Bounce.wav&")
                    if self.my_spaceship.xcor < 0:
                        self.my_spaceship.xcor += int(self.my_spaceship.lr_speed * 0.5)
                        self.my_spaceship.last_lr_move = pygame.K_RIGHT
                    elif self.my_spaceship.xcor > (display_width - 100):
                        self.my_spaceship.xcor -= int(self.my_spaceship.lr_speed * 0.5)
                        self.my_spaceship.last_lr_move = pygame.K_LEFT
                    if self.my_spaceship.ycor < 0:
                        self.my_spaceship.ycor += int(self.my_spaceship.ud_speed * 0.5)
                        self.my_spaceship.last_ud_move = None
                    elif self.my_spaceship.ycor >= (display_height - 100):
                        self.my_spaceship.ycor -= int(self.my_spaceship.ud_speed * 0.5)
                        self.my_spaceship.last_ud_move = None
                    collide = True
                if not self.pause:
                    if not collide:
                        self.my_spaceship.ycor += 1
                    draw_all()
                    move_all(timer)

                    if check_crash():
                        running = False

                    if len(enemy_list) == 0:
                        wave_cleared = pygame.font.Font(None, 100).render('Wave Cleared!', True, (255, 255, 0))
                        game_display.blit(wave_cleared,
                                          wave_cleared.get_rect(center=(int(display_width / 2),
                                                                        int(display_height / 10))))
                    if wave_timer == 0 and len(enemy_list) == 0:
                        # self.my_spaceship.attack_value += 1
                        # self.my_spaceship.hit_points += 1
                        self.my_spaceship.level_up(increase_atk=0, increase_hp=5)
                        if random.randint(0, 5) % 5 == 0:
                            self.my_spaceship.level_up(increase_atk=1, increase_hp=3)
                        print('Attack = {}'.format(self.my_spaceship.attack_value))
                        print('Hitpoints = {}'.format(self.my_spaceship.hit_points))
                        wave_timer = timer
                    elif timer >= wave_timer + 200:
                        wave_timer = 0

                    pygame.display.update()
                    afk += 1
                    timer += 1

            del afk
            del timer
            del cool_down
            del collide
            del running

        game_loop()
        print('Final score = {}'.format(*score))
        if __name__ == '__main__':
            pygame.quit()
        else:
            del self.my_spaceship

            for bullet in bullet_list:
                bullet_list.remove(bullet)
                bullet.destroy
            del bullet_list

            for enemy in enemy_list:
                enemy_list.remove(enemy)
                enemy.destroy
            del enemy_list

            for ally in ally_list:
                ally_list.remove(ally)
                ally.destroy
            del ally_list

            del score[0]
            del score

            del clock
            del game_display


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.music.load('Sounds/Falcon_vs_The_TIE_Fighters.wav')
    pygame.mixer.music.play(loops=-1)
    SpaceInvaders()
    quit()
