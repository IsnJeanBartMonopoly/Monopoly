def LANCER_DE():
    import random
    valeur = random.randint(1,6)
    return valeur


 
def SOMME1(n):
    import random
    somme = 0
    for k in range(n):
        somme=somme +random.randint(1,6)
      
    return(somme) 

    
def SOMME2(n):
    import random
    somme = 0
    for k in range(n):
        somme=somme +random.randint(1,6)
    return(somme) 
    #~ 
a = SOMME1(1)
b = SOMME2(1)
    
for i in range (1):
	print (a , end=" ")
	print (b , end=" ")
	
def double(a,b) :
	double1 = 0
	if a == b :
		print (a+b , end=" ")
		print ("relancée")		
		double2 = double1+1
		return (double2)
	else:
		print (a+b , end="")
		return double1
c = double(a,b)
#~

if c > 2 :
	print ("allez en prison")
 


	



	

	
	
	

	

 
    

