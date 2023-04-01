

class Death:
    def __init__(self):
        self.displayx = 600
        self.displayy = 600
        self.size = 40 

    def check_death(self,posx,posy):
         if posx >= self.displayx-self.size or posy >= self.displayy-self.size or posx < self.size or posy < self.size:
                return True
         else:
              return False
