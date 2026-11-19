import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """함대에 속한 외게인 하나를 나타내는 클래스"""
    
    def __init__(self, ai_game):
        """외계인을 초기화하고 시작 위치를 설정합니다."""
        super().__init__()
        self.screen = ai_game.screen
        
        # 외계인 이미지를 불러와 rect 속성을 설정합니다.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 외계인은 화면 좌측 상단 근처에 만듭니다.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 외계인의 가로 위치를 부동소수점으로 정확히 저장
        self.x = float(self.rect.x)