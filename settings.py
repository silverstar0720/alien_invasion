class Settings:
    """외계인 침공의 설정을 저장하는 클래스"""
    
    def __init__(self):
        """게임 설정 초기화"""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 우주선 설정
        # self.ship_speed = 1.5
        self.ship_speed = 15.0
        self.ship_limit = 3
        
        # 탄환 설정
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 # 딱 세 개까지 쏠 수 있음
        
        # 외계인 설정
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        # 은 오른쪽, -1은 왼쪽입니다.
        self.fleet_direction = 1