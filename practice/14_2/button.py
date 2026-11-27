import pygame.font

class Button:
    """게임에 사용하는 버튼을 만듭니다."""
    
    def __init__(self, game, msg):
        """버튼 요소들을 초기화합니다."""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # 버튼 요소들을 정의
        self.width, self.height = 200, 50
        self.button_color = (34, 139, 34)
        self.font_color = (255, 255, 255)
        
        self.font = pygame.font.SysFont(None, 48)
        
        # 버튼의 rect 만들고 초기위치 설정
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.render_img(msg)
        
    def render_img(self, msg):
        """폰트를 이미지로 렌더링하고 버튼 위치와 같게 설정."""
        self.image = self.font.render(msg, True, self.font_color, self.button_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center
    
    def draw_button(self):
        """버튼을 화면에 그립니다."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image, self.image_rect)