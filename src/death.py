
class Death:
    def __init__(self):
        pass

    def check_death(self,posx,posy):
        if posx >= 560 or posy >= 560 or posx < 40 or posy < 40:
            return True
        return False
