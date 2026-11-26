import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target

class AimingGame:
    """조준하여 맞추는 게임입니다."""
    
    def __init__(self):
        """조준 게임에 필요한 요소를 초기화"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Aiming Game')
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
    
    def run_game(self):
        """메인 루프"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            if self.target.check_edges():
                self.settings.target_direction *= -1
            self.target.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """사용자의 이벤트를 체크합니다."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """사용자가 키를 누를 때를 체크"""
        if event.key == pygame.K_UP:
            self.ship.up_flag = True
        elif event.key == pygame.K_DOWN:
            self.ship.down_flag = True
        elif event.key == pygame.K_SPACE:
            # 스페이스바를 누를 시 탄환객체 생성 후 그룹에 추가
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _check_keyup_events(self, event):
        """사용자가 키에서 손을 뗄 때를 체크"""
        if event.key == pygame.K_UP:
            self.ship.up_flag = False
        elif event.key == pygame.K_DOWN:
            self.ship.down_flag = False
    
    def _update_bullets(self):
        """탄환들의 위치를 업데이트하고,
        창밖으로 넘어간 탄환은 제거합니다.
        """
        for bullet in self.bullets.sprites():
            if bullet.rect.left <= self.screen.get_rect().right:
                self.bullets.update()
            else:
                self.bullets.remove(bullet)
    
    
    def _update_screen(self):
        """화면을 새로 그린 후 사용자에게 표시합니다."""
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blit_ship()
        self.target.draw_target()
        pygame.display.flip()
        
        
if __name__ == "__main__":
    AG = AimingGame()
    AG.run_game()