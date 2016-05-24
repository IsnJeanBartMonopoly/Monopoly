class joueur:
    def __init__(self):
        self.icon=""
        self.case=0
        self.money=20000
        
    def __str__(self):
        return "Joueur image = {} place= {} argent= {}".format(self.icon, self.case, self.money)
        
    