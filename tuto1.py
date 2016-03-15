import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
	return 
		<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
        <title>Monopoly- Le Site Web</title>
    </head>

    <body>
        <header>        
            <h1>le jeu</h1>
        </header>
        
        <div id="nav">
        
           <p>
    Voici notre plateau de jeu :<br />
    <img src="/home/knoppix/Downloads/monopoly-vierge.jpg" alt="plateau" />
    
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
        		<img src="drapeaufrancais.png" alt="" />
        		</div>>
        		
        		<div id="nav3">
        		<img src="drapeaufrancais.png" alt="" />
        		</div>>
        		<input type="button" class="bouton_actif" id="b1" value="lancée les dés" onclick="dé.py">
    </body>
</html>
        

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')
