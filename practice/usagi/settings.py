class Settings:
    """게임에 필요한 설정들을 모아놓은 클래스"""
    
    def __init__(self):
        """필요한 설정들을 초기화합니다."""
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = ((198, 220, 198))
        
        # 우사기 설정
        self.usagi_speed = 7.0
        self.usagis_left = 0 # 우사기 기본 목숨 개수
        
        # 물 총알 설정
        self.bullet_speed = 10.0
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 3
        
        # 치이카와 설정
        self.chiikawa_speed = 1.5
        self.chiikawa_x_speed = 3.0
        self.chiikawa_direction = 1 # 1이 아래쪽, -1이 위쪽 이동
        self.chiikawa_frequency = 0.015