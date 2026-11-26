import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """탄환을 만드는 클래스입니다."""
    
    def __init__(self, game):
        """탄환을 초기화합니다."""
        super().__init__()
        
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        self.screen = game.screen
        self.ship_rect = game.ship.rect
        
        # 탄환의 rect을 만들고 초기위치를 설정합니다.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = self.ship_rect.midright
        
        # 탄환의 x 위치를 부동소수점으로 저장합니다.
        self.x = self.rect.x
        
    def update(self):
        """탄환의 위치를 업데이트합니다."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
        
    def draw_bullet(self):
        """탄환을 화면에 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)