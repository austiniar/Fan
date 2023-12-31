import pygame.sprite

from modules.animation import Animated


class Weapon(pygame.sprite.Sprite, Animated):
    def __init__(self, r, pos, animation_name, animation_period):
        pygame.sprite.Sprite.__init__(self)
        Animated.__init__(self, r, animation_name, animation_period)
        self.r = r
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.offset_not_flipped = int(), int()
        self.offset_flipped = int(), int()
        self.bullet = None
        self.bullets_group = pygame.sprite.Group()

    def release_bullet(self, mouse_position_compenstation):
        self.bullet(self.r, (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                    ((mp := pygame.mouse.get_pos())[0] + mouse_position_compenstation[0],
                     mp[1] + mouse_position_compenstation[1]), self.bullets_group)

    def apply_offset(self):
        self.rect.x += self.offset_flipped[0] if self.animation_is_flipped else self.offset_not_flipped[0]
        self.rect.y += self.offset_flipped[1] if self.animation_is_flipped else self.offset_not_flipped[1]
