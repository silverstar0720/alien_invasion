import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """우사기가 발사하는 물총의 총알을 관리하는 클래스"""
    
    def __init__(self, game):
        """총알 객체 요소를 초기화합니다."""
        super().__init__()
        
        self.screen = game.screen
        self.usagi = game.usagi
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        # 일단 이미지가 없으니 Rect객체로 만듦.
        # 초기위치는 임시로 (0,0)
        self.rect = pygame.Rect(0,0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        
        # 초기위치 진짜 설정. 우사기 기준 가운데 오른쪽
        self.rect.midright = self.usagi.rect.midright
        
        # 위치를 부동소수점으로 저장
        self.x = float(self.rect.x)
        
    def update(self):
        """총알 위치를 업데이트합니다."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self):
        """화면에 총알을 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)