import sys

import pygame

from settings import Settings
from usagi import Usagi
from bullet import Bullet
from chiikawa import Chiikawa

class FightUsagi:
    """싸워라! 우사기 게임의 메인 클래스입니다."""
    
    def __init__(self):
        """게임에 필요한 기본 요소들을 초기화 합니다."""
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("싸워라! 우사기")
        
        self.usagi = Usagi(self)
        self.bullets = pygame.sprite.Group()
        
        self.chiikawas = pygame.sprite.Group()
        self._create_chiikawas()
    
    def run_game(self):
        """게임의 메인 루프"""
        while True:
            self._check_events()
            self.usagi.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """사용자 입력에 응답합니다."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """사용자의 키 입력에 응답합니다."""
        if event.key == pygame.K_UP:
            self.usagi.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.usagi.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """사용자가 키를 손에서 뗄 때 응답합니다."""
        if event.key == pygame.K_UP:
            self.usagi.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.usagi.moving_down = False
            
    def _fire_bullet(self):
        """새 총알을 만들어 총알그룹에 저장합니다."""
        if len(self.bullets) < self.settings.bullet_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)
    
    def _update_bullets(self):
        """총알 위치를 업데이트하고 화면 밖으로 나간 총알은 제거합니다."""
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
    
    def _create_chiikawas(self):
        """치이카와들을 만듭니다."""
        chiikawa = Chiikawa(self)
        width, height = chiikawa.rect.size
        screen_width, screen_height = self.screen.get_rect().size
        
        current_x = screen_width - (width/2 + width)
        current_y = height

        while current_x > 2 * width:
            while current_y < screen_height - 3/2 * height:
                new_chiikawa = Chiikawa(self)
                new_chiikawa.rect.y = current_y
                new_chiikawa.x = current_x
                new_chiikawa.rect.x = new_chiikawa.x
                self.chiikawas.add(new_chiikawa)
                
                current_y += height/4 + height
            current_x -= width/4 + width
            current_y = height
        
        
        
    
    def _update_screen(self):
        """화면의 ^이미지를^ 업데이트하고 화면을 새로 그립니다."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.usagi.blitme()
        
        self.chiikawas.draw(self.screen)
                    
        pygame.display.flip()
    
            
if __name__ == "__main__":
    fight_usagi = FightUsagi()
    fight_usagi.run_game()