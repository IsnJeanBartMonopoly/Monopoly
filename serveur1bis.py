import cherrypy
import json
import os, os.path
import random
import string


class Root(object):
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
    <img src="/static/monopoly-vierge.jpg" alt="plateau" />
    
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
        		    <table>
			<tr>
				<td style="text-align: left; vertical-align: top; border: none;">
					<div id="menu">
						<table id="menutable" cellspacing="0">
							<tr>
								<td class="menu-item" id="buy-menu-item">

									<a href="javascript:void(0);" title="View alerts and buy the property you landed on.">Buy</a>
								</td>
								<td class="menu-item" id="manage-menu-item">

									<a href="javascript:void(0);" title="View, mortgage, and improve your property. ">Manage</a>
								</td>
								<td class="menu-item" id="trade-menu-item">

									<a href="javascript:void(0);" title="Exchange property with other players.">Trade</a>
								</td>
							</tr>
						</table>
					</div>

					<div id="buy">
						<div id="alert"></div>
						<div id="landed"></div>
					</div>

					<div id="manage">
						<div id="option">
							<div id="buildings" title="Available buildings"></div>
							<input type="button" value="Buy house" id="buyhousebutton"/>
							<input type="button" value="Mortgage" id="mortgagebutton" />
							<input type="button" value="Sell house" id="sellhousebutton"/>
						</div>
						<div id="owned"></div>
					</div>
				</td>
				<td style="vertical-align: top; border: none;">
					<div id="quickstats" style="">
							<div><span id="pname" >Player 1</span>:</div>
							<div><span id="pmoney">$1500</span></div>
					</div>
					<div>
						<div id="die0" title="Die" class="die die-no-img"></div>
						<div id="die1" title="Die" class="die die-no-img"></div>
					</div>

				</td>
			</tr><tr>
				<td colspan="2" style="border: none">
					<div style="padding-top: 8px;">
						<input type="button" id="nextbutton" title="Roll the dice and move your token accordingly." value="Roll Dice"/>
						<input type="button" id="resignbutton" title="If you cannot pay your debt then you must resign from the game." value="Resign" onclick="game.resign();" />
					</div>
				</td>
			</tr>
		</table>
		</table>
    </body>
</html>"""
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def LANCER_DE(self):
	    import random
	    valeur = random.randint(1,12)
	    return valeur
	
	def SOMME1(n):
	    import random
	    somme = 0
	    for k in range(n):
	        somme=somme +random.randint(1,12)
	      
	    return(somme) 
	    return{"somme" : SOMME1}

if __name__ == '__main__':
 cherrypy.quickstart(Root(), config ="serveur.conf")
 cherrypy.quickstart(Root(), '/')

