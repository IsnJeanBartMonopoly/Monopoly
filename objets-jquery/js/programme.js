function orange(obj){
	// obj est un objet jQuery
	// la fonction renvoie un pointeur sur obj
	obj.addClass("bouton_actif_clique").removeClass("bouton_actif").val("LANCER_DE");
	return obj;
}

function bleu(obj){
	// obj est un objet jQuery
	// la fonction renvoie un pointeur sur obj
	obj.addClass("bouton_actif").removeClass("bouton_actif_clique").val("Cliquez ici");
	return obj;
}
