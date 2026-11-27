import pygame

class Target:
    """타겟을 만드는 클래스입니다."""
    
    def __init__(self, game):
        """타겟의 요소를 초기화합니다."""
        self.settings = game.settings
        self.color = self.settings.target_color
        
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # 타겟의 Rect을 만들고 초기 위치를 설정합니다.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                self.settings.target_height)
        self.rect.midright = self.screen_rect.midright
        
        # 타겟의 y좌표를 부동소수점으로 저장합니다.
        self.y = self.rect.y
                        
    def target_midright(self):
        """타겟의 초기 위치를 midright로 설정"""
        self.rect.midright = self.screen_rect.midright
        self.y = self.rect.y
    
    def update(self):
        """타겟의 위치를 업데이트합니다."""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y
            
    def check_edges(self):
        """아래 위쪽에 닿았는지 확인 후 bool 반환"""
        return (self.rect.bottom >= self.screen_rect.bottom) or (self.rect.top 
                                                                 <= 0)
    def draw_target(self):
        """타겟을 화면에 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)