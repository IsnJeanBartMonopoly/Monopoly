function orange(obj){
	// obj est un objet jQuery
	// la fonction renvoie un pointeur sur obj
	obj.addClass("bouton_actif_clique").removeClass("bouton_actif").val("2");
	return obj;
}

function bleu(obj){
	// obj est un objet jQuery
	// la fonction renvoie un pointeur sur obj
	obj.addClass("bouton_actif").removeClass("bouton_actif_clique").val("Cliquez ici");
	return obj;
}


function LANCER_DE(){
	var o = $("#b1");
	orange(o);
	setTimeout( function(){bleu(o);}, 2000 );
}
