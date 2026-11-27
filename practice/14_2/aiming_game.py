import sys

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
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
        self.stats = GameStats(self)
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Aiming Game')
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        
        # 게임 활성화 플래그
        self.game_active = False
        # 게임 플레이 버튼
        self.play_button = Button(self, 'Play')
            
    def run_game(self):
        """메인 루프"""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
                
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button()
    
    def _check_keydown_events(self, event):
        """사용자가 키를 누를 때를 체크"""
        if event.key == pygame.K_UP:
            self.ship.up_flag = True
        elif event.key == pygame.K_DOWN:
            self.ship.down_flag = True
        elif event.key == pygame.K_SPACE:
            # 스페이스바를 누를 시 탄환객체 생성 후 그룹에 추가
            self._create_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """사용자가 키에서 손을 뗄 때를 체크"""
        if event.key == pygame.K_UP:
            self.ship.up_flag = False
        elif event.key == pygame.K_DOWN:
            self.ship.down_flag = False
    
    def _check_play_button(self):
        """플레이 버튼을 눌렀는지 체크"""
        # 플레이 버튼을 누른다면 게임 활성화
        self.mouse_pos = pygame.mouse.get_pos()
        self.clicked_button = self.play_button.rect.collidepoint(
                                                    self.mouse_pos)
        if (self.clicked_button) and (not self.game_active):
            self._start_game()
    
    def _start_game(self):
        """게임을 새로 활성화합니다."""
        # 게임 활성화하고, stats 리셋
        self.game_active = True
        self.stats.reset_stats()
        
        # 탄환 다 없애고
        self.bullets.empty()
        
        # 우주선과 타겟 위치 초기화
        self.ship.ship_midleft()
        self.target.target_midright()
    
    def _update_bullets(self):
        """탄환들의 위치를 업데이트하고,
        창밖으로 넘어간 탄환은 제거합니다.
        """
        for bullet in self.bullets.sprites():
            if bullet.rect.left <= self.screen.get_rect().right:
                self.bullets.update()
            else:
                self.bullets.remove(bullet)
                
        if (self.stats.bullets_left == 0) and (not self.bullets):
            # 남은 탄환수가 0이면서, 창 끝까지 갔다면 게임 비활성화
            self.game_active = False
        
    def _check_bullets_target_collisions(self):
        """타겟이랑, 탄환이랑 닿았나 체크"""
        self.bullets_target_collide = pygame.sprite.spritecollide(self.target,
                                                                  self.bullets,
                                                                  True)
        if self.bullets_target_collide:
            print(f"{len(self.bullets_target_collide)}")
    
    def _update_target(self):
        """타겟이 창 모서리에 닿았나 체크하고,
        방향을 바꾸고, 위치를 업데이트합니다.
        """
        if self.target.check_edges():
            self.settings.target_direction *= -1
        self.target.update()
    
    def _create_bullets(self):
        """스페이스바를 누를 시 남은 탄환 수를 확인하고,
        탄환 객체 생성 후 그룹에 추가
        """
        if self.stats.bullets_left > 0:
            bullet = Bullet(self)
            self.bullets.add(bullet)
            self.stats.bullets_left -= 1
    
    def _update_screen(self):
        """화면을 새로 그린 후 사용자에게 표시합니다."""
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blit_ship()
        self.target.draw_target()
        
        if not self.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()
        
        
if __name__ == "__main__":
    AG = AimingGame()
    AG.run_game()