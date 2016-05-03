function orange(obj){
	// obj est un objet jQuery
	// la fonction renvoie un pointeur sur obj
	obj.addClass("bouton_actif_clique").removeClass("bouton_actif").val("ouille");
	return obj;
}

function bleu(obj){
	// obj est un objet jQuery
	// la fonction renvoie un pointeur sur obj
	obj.addClass("bouton_actif").removeClass("bouton_actif_clique").val("Cliquez ici");
	return obj;
}


function ouille(){
	var o = $("#b1");
	orange(o);
	setTimeout( function(){bleu(o);}, 500 );
}


function grinche(el){
	//el est un élément de la page web
	$(el).attr('src', 'smiley.jpg');
	setTimeout( 
		function(){
			$(el).attr('src', 'smiley-rire1209759738.jpg');
		}, 
		300
	);
}