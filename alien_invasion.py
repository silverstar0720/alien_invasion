import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""
    
    def __init__(self):
        """게임을 초기화하고, 게임 자원을 만듭니다."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        
    def run_game(self):
        """게임의 메인 루프를 시작합니다."""
        while True: 
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """키 입력과 마우스 이벤트에 응답합니다."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """키를 누를 때 응답합니다."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """키에서 손을 뗄 때 응답합니다."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """새 탄환을 만들어 탄환 그룹에 추가합니다."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """탄환 위치를 업데이트하고, 창 밖으로 사라진 탄환을 제거합니다."""
        # 탄환 위치를 업데이트합니다.
        self.bullets.update()
            
        # 창 밖으로 사라진 탄환 제거
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _create_fleet(self):
        """외계인 함대를 만듭니다."""
        # 외계인 하나를 만들고, 공간이 없을 때까지 계속 추가합니다.
        # 외계인 사이의 공간은 외계인 너비와 같습니다.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # 한 줄이 끝났으니 x값은 초기화하고 y값은 늘립니다.
            current_x = alien_width
            current_y += 2 * alien_height
            
                
    def _create_alien(self, x_position, y_position):
        """외계인 하나를 만들어 배치합니다."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        
        self.aliens.add(new_alien)
        
    def _update_screen(self):
        """화면의 이미지를 업데이트하고, 화면을 새로 그립니다."""
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()
        
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()