class joueur:      
	def __init__(self):
		#self.icon=""
		#self.cash=1500     # argent
		#self.properties = {}  Liste des propriete
		self.position=0    # position
		
	def __str__(self):
		return "Joueur image = {} position = {} cash = {}".format(self.icon, self.cash, self.position)
        
        # permet de faire bouger le joueur sur le plateau
        #def move(self, lancer, verbose=False):
         #   self.position += lancer
      #      if self.position >= 40:
        #        self.position -= 40
       #         self.cash += 200
       #     if verbose:
     #           print 'joueur {} to position: {}'.format(self.id, self.position)

	
	
	

	

 
    

