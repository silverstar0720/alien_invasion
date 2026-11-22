import pygame
from pygame.sprite import Sprite

class Chiikawa(Sprite):
    """치이카와 뭉탱이 중 하나를 나타내는 클래스"""
    def __init__(self, game):
        """치이카와 기본 설정을 초기화합니다."""
        super().__init__()
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        
        self.image = pygame.image.load('images/chiikawa.bmp')
        self.image = pygame.transform.smoothscale(self.image, (100,100))
        self.rect = self.image.get_rect()
        
        # 초기 위치 설정
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 위치를 부동소수점으로 저장
        self.x = float(self.rect.x)
        
    def update(self):
        """치이카와의 위치를 업데이트합니다."""
        self.x -= self.settings.chiikawa_speed
        self.rect.x = self.x