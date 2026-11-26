import pygame

class Button:
    """버튼을 만드는 클래스"""
    
    def __init__(self, game, msg):
        """버튼 요소를 초기화"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # rect을 만들기 전에 버튼 요소 설정
        self.width, self.height = 200, 50
        self.button_color = (154, 205, 50)
        self.text_color = (255, 255, 255)
        
        self.font = pygame.Font(None, 48)
        
        # rect만들고 센터로 위치 설정
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 텍스트 이미지로 만들기
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """텍스트를 렌더링해 이미지로 나타내기"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        # 위치 설정 (센터로)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """화면에 버튼을 그립니다"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)