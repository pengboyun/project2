import randomimport pygame

# 游戏窗口SCREEN_RECT = pygame.Rect(0, 0, 480, 852) # Rect.size能返回一个元组# 刷新的帧率FRAME_PER_SEC = 60# 敌机出现事件CREATE_ENEMY_EVENT = pygame.USEREVENT# 英雄发射子弹HERO_FRIE_EVENT = pygame.USEREVENT + 1

# 定义GameSprite继承子Sprite类sprite模块class GameSprite(pygame.sprite.Sprite):"""飞机大战精灵"""

def __init__(self, image_name, speed=1):# 调用父类的初始化方法 super().__init__()

# 定义对象属性self.image = pygame.image.load(image_name) # 加载图像 self.rect = self.image.get_rect() # 获取加载图像的尺寸 self.speed = speed # 定义速度，初始值为1

def update(self):# 在屏幕的垂直方向上移动 self.rect.y += self.speed

class Background(GameSprite): # 背景精灵

def __init__(self, is_all=False):# 1.调用父类方法实现精灵的创建 super(Background, self).__init__('./images/background.png')

# 2.判断是否是交替图像，如果是，需要设置初始位置if is_all: self.rect.y = -self.rect.height

def update(self):# 1.调用父类的方法 super(Background, self).update()

# 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方if self.rect.y >= SCREEN_RECT.height: self.rect.y = -self.rect.height

class Enemy(GameSprite):def __init__(self): # 1.调用父类方法，创建敌机精灵，同时指定敌机图像 super().__init__('./images/enemy1.png')

# 2.指定敌机的初始速度self.speed = random.randint(2,4)

# 3.指定敌机的初始随机位置self.rect.bottom = 0

max_x = SCREEN_RECT.width - self.rect.width # 计算水平位置的最大值

self.rect.x = random.randint(0,max_x) # 水平初始位置def update(self): # 1.调用父类方法，保持垂直方向的飞行 super().update() # 2.判断是否飞出屏幕，如果是，需要从精灵组中移除 if self.rect.y >= SCREEN_RECT.height:

self.kill() # kill方法可以将精灵从所有精灵组中移除，精灵就会自动被销毁

# def __del__(self):# print ('敌机被炸毁啦！ %s' % self.rect)class Hero(GameSprite): """英雄精灵""" def __init__(self): # 1.调用父类方法，设置image位置 super().__init__('./images/hero1.png',0) # 2.设置英雄的初始化位置 self.rect.centerx = SCREEN_RECT.centerx self.rect.bottom = SCREEN_RECT.bottom - 50

# 创建子弹的精灵组self.bulltes = pygame.sprite.Group()

def update(self):# 英雄在水平方向移动 self.rect.x += self.speed

# 绘制移动边界if self.rect.x < 0: self.rect.x = 0 elif self.rect.right > SCREEN_RECT.right: self.rect.right = SCREEN_RECT.right

def frie(self):# 1.创建子弹精灵 bullte = Bullet()

# 2.设置子弹的位置bullte.rect.bottom = self.rect.y bullte.rect.centerx = self.rect.centerx

# 3.将精良添加到精灵组self.bulltes.add(bullte)

def __del__(self):print ('主飞机被炸毁啦！') print ('游戏结束')


class Bullet(GameSprite):def __init__(self): super().__init__('./images/bullet1.png',-4)

def update(self):# 1.调用父类方法，保持垂直方向的飞行 super().update() # 2.判断是否飞出屏幕，如果是，需要从精灵组中移除 if self.rect.bottom < 0:

self.kill() # kill方法可以将精灵从所有精灵组中移除，精灵就会自动被销毁



import pygame

from import *

class PlaneGame(object):def __init__(self): # 游戏初始化

self.screen = pygame.display.set_mode(SCREEN_RECT.size) # 创建游戏的窗口

self.clock = pygame.time.Clock() # 创建游戏的时钟

self.__create_sprite() # 调用私有方法

pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000) # 设置定时器事件，创建敌机,单位毫秒

pygame.time.set_timer(HERO_FRIE_EVENT,300) # 设置发射子弹时间def __create_sprite(self): # 创建背景精灵和精灵组 bg1 = Background() bg2 = Background(True) # 创建二张背景让其做交替切换，否则图像会有异常

self.back_ground = pygame.sprite.Group(bg1, bg2)

# 创建敌机的精灵组self.enemy_group = pygame.sprite.Group()

# 创建英雄的精灵和精灵组self.hero = Hero() self.hero_group = pygame.sprite.Group(self.hero)

def start_Game(self):

while True:# 1.设置刷新帧率 self.clock.tick(FRAME_PER_SEC) # 2.事件监听 self.__event_handler() # 3.碰撞检测 self.__check_collide() # 4.更新/绘制精灵族 self.__update_sprite() # 5.更新显示 pygame.display.update()

def __event_handler(self):

for event in pygame.event.get():# 监听用户点击退出按钮 if event.type == pygame.QUIT: PlaneGame.__game_over() # 为什么使用PlaneGame而不是self呢？

elif event.type == CREATE_ENEMY_EVENT:# 创建敌机精灵 enemy = Enemy() # 将敌机精灵添加到敌机精灵组 self.enemy_group.add(enemy) elif HERO_FRIE_EVENT: self.hero.frie()

# elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:# print ('向右移动！')

# 使用键盘提供的方法获取键盘按键，按键元组keys_pressed = pygame.key.get_pressed() # 判断元组中对应的按键索引值 1 if keys_pressed[pygame.K_SPACE]: # 涡轮增压 speed = 5 else: speed = 2 if keys_pressed[pygame.K_LEFT]:

self.hero.speed = -speed

elif keys_pressed[pygame.K_RIGHT]:

self.hero.speed = speed

else:self.hero.speed = 0

def __check_collide(self):# 子弹摧毁敌机 pygame.sprite.groupcollide(self.hero.bulltes,self.enemy_group,True,True)

enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)if len(enemies) > 0: self.hero.kill()

self.__game_over()

def __update_sprite(self):

self.back_ground.update() # 背景

self.back_ground.draw(self.screen)

self.enemy_group.update() # 敌机

self.enemy_group.draw(self.screen)

self.hero_group.update() # 英雄self.hero_group.draw(self.screen)

self.hero.bulltes.update() # 子弹self.hero.bulltes.draw(self.screen)

@staticmethod def __game_over(): # 定义静态方法 pygame.quit() exit()

if __name__ == '__main__':

while True:game = PlaneGame() # 创建实例

game.start_Game() # 游戏开始