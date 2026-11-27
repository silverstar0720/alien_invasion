class GameStats:
    """게임 플레이 게임 기록"""
    
    def __init__(self, game):
        """기록를 초기화 합니다."""
        self.settings = game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """게임을 플레이하는 동안 변하는 기록 초기화"""
        self.bullets_left = self.settings.bullet_limit