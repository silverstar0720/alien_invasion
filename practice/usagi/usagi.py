import pygame

class Usagi:
    """우사기를 관리하는 클래스"""
    
    def __init__(self, game):
        """우사기의 기본 설정을 초기화합니다."""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('images/usagi.bmp')
        self.image = pygame.transform.smoothscale(self.image, (150,150))
        self.rect = self.image.get_rect()
        
        # 초기 위치를 가운데 왼쪽으로 잡습니다.
        self.rect.midleft = self.screen_rect.midleft
        self.rect.x += 20
        
        # 움직임 플래그는 정지 상태로 시작합니다.
        self.moving_up = False
        self.moving_down = False
        
        # 우사기의 y위치를 부동소수점으로 저장
        self.y = float(self.rect.y)
    
    def update(self):
        """움직임 플래그를 따라 우사기 위치를 업데이트 합니다."""
        if self.moving_up and (self.rect.top > 0):
            self.y -= self.settings.usagi_speed
        if self.moving_down and (
            self.rect.bottom < self.screen_rect.bottom):
            self.y += self.settings.usagi_speed
        self.rect.y = self.y
    
    def blitme(self):
        """화면에 그림을 그립니다."""
        self.screen.blit(self.image, self.rect)