import pygame

class Ship:
    """우주선을 만드는 클래스"""
    
    def __init__(self, game):
        """우주선 요소를 초기화합니다."""
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # 우주선 이미지를 불러와 rect를 만듭니다.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90.0)
        self.rect = self.image.get_rect()
        
        # 우주선 위치를 좌측 가운데로 설정
        self.rect.midleft = self.screen_rect.midleft
        
        # 우주선의 y위치를 부동소수점으로 저장
        self.y = self.rect.y
        
        self.up_flag = False
        self.down_flag = False
        
    def update(self):
        """우주선의 위치를 업데이트 합니다."""
        if self.up_flag and (self.rect.top > 0):
            self.y -= self.settings.ship_speed
            self.rect.y = self.y
        if self.down_flag and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.settings.ship_speed
            self.rect.y = self.y
        
    def blit_ship(self):
        """우주선을 화면에 그립니다."""
        self.screen.blit(self.image, self.rect)