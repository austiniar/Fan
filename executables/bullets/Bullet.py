import time

import pygame.time


class Bullet(pygame.sprite.Sprite):
    def __init__(self, r, start_pos, end_pos, *sprite_groups):
        super().__init__(*sprite_groups)
        self.r = r
        self.lifetime = 2
        self.spawn_time = time.time()
        self.clock = pygame.time.Clock()
        self.delta_x = end_pos[0] - start_pos[0]
        self.delta_y = end_pos[1] - start_pos[1]
        self.current_pos = int(), int()
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.speed = 0.5
        self.rect = pygame.Rect(0, 0, 1, 1)

    def update(self):
        if time.time() - self.spawn_time > self.lifetime:
            self.kill()
            return
        length = self.clock.tick() * self.speed
        x_movement = (self.delta_x ** 2 * length ** 2 / (self.delta_y ** 2 + self.delta_x ** 2)) ** 0.5 \
            if self.delta_y else length
        y_movement = abs(x_movement * self.delta_y / self.delta_x) if self.delta_x else length
        self.current_pos = self.start_pos[0] + (x_movement := x_movement * (1 if self.delta_x > 0 else -1)), \
            self.start_pos[1] + (y_movement := y_movement * (1 if self.delta_y > 0 else -1))
        self.end_pos = self.end_pos[0] + x_movement, self.end_pos[1] + y_movement

