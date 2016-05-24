import cherrypy
import json
import os, os.path
import random
import string
import debis



J1=None
J2=None



class Root(object):
	resultat=0
	resultat2=0
	@cherrypy.expose
	def index(self):
		return """<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
        <script type="text/javascript" src="programme.js"></script>
        <script type="text/javascript" src="jquery.js"></script>
        <title>Monopoly- Le Site Web</title>
    </head>

    <body>
        <header>        
            <h1>le jeu</h1>
        </header>
        
        <div id="nav">
        
           <p>
    Voici notre plateau de jeu :<br />
    <img src="/static/monop4.jpg" alt="plateau" />
    
</p>
        </div>
        
        <section
            <article>                
                <h1>Je suis le créateur de ce jeu</h1>
                <p>Bla bla bla bla (texte de l'article)</p>
            </article>
        </section>
        <footer>
            <p>Copyright kireds- Tous droits réservés

            <a href="#">Me contacter !</a></p>
        </footer>
        
        		<div id="nav2">
        		<img src="/static/drapeaufrancais.png" alt="" />
        		</div>>
        		
        		<div id="nav3">
        		<img src="/static/drapeaufrancais.png" alt="" />
        		</div>>
        		<input type="button" class="bouton_actif" id="b1" value="lancée les dés" onclick="$.get('/LANCER_DE').done(
        		function(data){
        		  console.log(data);
        		  $('#resultat').html(data);
        		 
        		})">
        		<div id="resultat">
        		</div>   
        		<div id="resultat2">
        		</div>     			
    </body>
</html>"""
	@cherrypy.expose
	@cherrypy.tools.json_out()

	def LANCER_DE(self):
		typD = 6
		nbD = 1
		resultat = (random.randrange(1,(typD+1)))
		resultat2 = (random.randrange(1,(typD+1)))
		return (resultat,resultat2)
		



	    
	    

if __name__ == '__main__':
 J1=debis.joueur()
 J2=debis.joueur()
 cherrypy.quickstart(Root(), config ="serveur.conf")
 cherrypy.quickstart(Root(), '/')

