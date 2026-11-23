class GameStats:
    """싸워라! 우사기 게임 기록"""
    
    def __init__(self, game):
        """기록 초기화"""
        self.settings = game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """게임을 진행하는 동안 !!변하는 기록 초기화!!"""
        self.usagis_left = self.settings.usagis_left
        # 총알이 치이카와를 맞혔을 시 카운트
        self.bullet_collision_count = 0
        # 우사기와 치이카와가 충돌했을 시 카운트
        self.usagi_collision_count = 0
        