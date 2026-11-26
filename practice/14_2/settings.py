class Settings:
    """게임에 필요한 설정들을 모아놓는 클래스"""
    
    def __init__(self):
        """설정을 초기화 합니다."""
        # 화면 설정
        self.bg_color = (230, 230, 230)
        self.screen_width = 1200
        self.screen_height = 800
        
        # 우주선 설정
        self.ship_speed = 7.0
        
        # 탄환 설정
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullet_speed = 5.0
        self.bullet_color = (0, 0, 0)
        
        # 타겟 설정
        self.target_width = 50
        self.target_height = 50
        self.target_speed = 5.0
        self.target_color = (255, 0, 0)
        # 1은 아래쪽, -1은 위쪽으로 감
        self.target_direction = 1