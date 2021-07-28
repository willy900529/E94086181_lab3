import pygame
import math
import os
from settings import PATH1,PATH2
#來計算要走哪一條路線
check=0
calculate_variable=1

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    check = 0
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        # 創造第一個路徑
        self.path = PATH1
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]
        #創造第二個路徑
        self.path2 = PATH2
        self.path2_index = 0
        self.move2_count = 0
        self.stride2 = 1
        self.x2, self.y2 = self.path2[0]



    def draw(self, win):
        # draw enemy
        if check==0:
            win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))

        else:
            win.blit(self.image, (self.x2 - self.width // 2, self.y2 - self.height // 2))
            pygame.display.update()
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        # ...(to be done)
        #路線上的血條
        if check==0:#路線一上的血條
            pygame.draw.rect(win, (255, 0, 0), [self.x-17,self.y-30 , self.max_health*4, 5])
            pygame.draw.rect(win, (0, 255, 0), [self.x-17, self.y-30, self.health*4, 5])
        else:#路線二上的血條
            pygame.draw.rect(win, (255, 0, 0), [self.x2 - 17, self.y2 - 30, self.max_health * 4, 5])
            pygame.draw.rect(win, (0, 255, 0), [self.x2 - 17, self.y2 - 30, self.health * 4, 5])


    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        # ...(to be done)
        if check==0:#路線一
            ax, ay = self.path[self.path_index]
            bx, by = self.path[self.path_index + 1]
            self.distance_A_B = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
            max_count = int(self.distance_A_B / self.stride)  # total footsteps that needed from A to B
            if self.move_count < max_count:
                unit_vector_x = (bx - ax) / self.distance_A_B
                unit_vector_y = (by - ay) / self.distance_A_B
                delta_x = unit_vector_x * self.stride
                delta_y = unit_vector_y * self.stride
                # update the coordinate and the counter
                self.x += delta_x
                self.y += delta_y
                self.move_count += 1
                pygame.display.update()
            else:
                self.path_index += 1
                self.move_count = 0
                pygame.display.update()
        else:#路線二
            ax, ay = self.path2[self.path2_index]
            bx, by = self.path2[self.path2_index + 1]
            self.distance_A_B = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
            max_count2 = int(self.distance_A_B / self.stride2)  # total footsteps that needed from A to B
            self.check = 0
            if self.move2_count < max_count2:
                unit_vector_x = (bx - ax) / self.distance_A_B
                unit_vector_y = (by - ay) / self.distance_A_B
                delta_x = unit_vector_x * self.stride2
                delta_y = unit_vector_y * self.stride2
                # update the coordinate and the counter
                self.x2 += delta_x
                self.y2 += delta_y
                self.move2_count += 1
                pygame.display.update()
            else:
                self.path2_index += 1
                self.move2_count = 0
                pygame.display.update()



class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = []  # don't change this line until you do the EX.3 ,self.expedition = [Enemy()]
        self.period=0

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)
        #win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        self.period+=1 #self.period一直加一
        if self.gen_count<3 and self.period==self.gen_period:#self.period到120(也就是self.gen_period)的時候要多叫一個出來
            if self.is_empty()==False:
                self.gen_count += 1 #敵人加一
                self.expedition.append(self.reserved_members.pop())
                self.period = 0 #叫出怪物的間隔重新累計


    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # ...(to be done)
        global calculate_variable
        calculate_variable +=1 #每按一次,n代表要換路線
        if calculate_variable%2==0: #calculate_variable為偶數代表路線一
            global check
            check=0
        else:#calculate_variable為奇數代表路線二
            check=1
        for i in range(num): #叫出3隻怪物
            self.reserved_members.append(Enemy())
        self.period = 0
        self.gen_count=0

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





