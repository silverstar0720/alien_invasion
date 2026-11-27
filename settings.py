class Settings:
    """외계인 침공의 설정을 저장하는 클래스"""
    
    def __init__(self):
        """게임의 정적 설정 초기화"""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 우주선 설정
        self.ship_limit = 1
        
        # 탄환 설정
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 # 딱 세 개까지 쏠 수 있음
        
        # 외계인 설정
        self.fleet_drop_speed = 10
        
        # 게임을 빠르게 만드는 속도
        self.speedup_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """게임을 진행하는 동안 변하는 설정 초기화"""
        self.ship_speed = 4.5
        self.bullet_speed = 4.5
        self.alien_speed = 1.0
        
        # 1은 오른쪽, -1은 왼쪽입니다.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """속도 설정을 높입니다."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale