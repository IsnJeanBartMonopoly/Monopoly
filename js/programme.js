function roll() {
	var p = player[turn];

	$("#option").hide();
	$("#buy").show();
	$("#manage").hide();

	if (p.human) {
		document.getElementById("nextbutton").focus();
	}
	document.getElementById("nextbutton").value = "End turn";
	document.getElementById("nextbutton").title = "End turn and advance to the next player.";

	game.rollDice();
	var die1 = game.getDie(1);
	var die2 = game.getDie(2);

	doublecount++;

	if (die1 == die2) {
		addAlert(p.name + " rolled " + (die1 + die2) + " - doubles.");
	} else {
		addAlert(p.name + " rolled " + (die1 + die2) + ".");
	}

	if (die1 == die2 && !p.jail) {
		updateDice(die1, die2);

		if (doublecount < 3) {
			document.getElementById("nextbutton").value = "Roll again";
			document.getElementById("nextbutton").title = "You threw doubles. Roll again.";

		// If player rolls doubles three times in a row, send him to jail
		} else if (doublecount === 3) {
			p.jail = true;
			doublecount = 0;
			addAlert(p.name + " rolled doubles three times in a row.");
			updateMoney();


			if (p.human) {
				popup("You rolled doubles three times in a row. Go to jail.", goToJail);
			} else {
				gotojail();
			}

			return;
		}
	} else {
		document.getElementById("nextbutton").value = "End turn";
		document.getElementById("nextbutton").title = "End turn and advance to the next player.";
		doublecount = 0;
	}

	updatePosition();
	updateMoney();
	updateOwned();

	if (p.jail === true) {
		p.jailroll++;

		updateDice(die1, die2);
		if (die1 == die2) {
			document.getElementById("jail").style.border = "1px solid black";
			document.getElementById("cell11").style.border = "2px solid " + p.color;
			$("#landed").hide();

			p.jail = false;
			p.jailroll = 0;
			p.position = 10 + die1 + die2;
			doublecount = 0;

			addAlert(p.name + " rolled doubles to get out of jail.");

			land();
		} else {
			if (p.jailroll === 3) {

				if (p.human) {
					popup("<p>You must pay the $50 fine.</p>", function() {
						payFifty();
						payfifty();
						player[turn].position=10 + die1 + die2;
						land();
					});
				} else {
					payfifty();
					p.position = 10 + die1 + die2;
					land();
				}
			} else {
				$("#landed").show();
				document.getElementById("landed").innerHTML = "You are in jail.";

				if (!p.human) {
					popup(p.AI.alertList, game.next);
					p.AI.alertList = "";
				}
			}
		}


	} else {
		updateDice(die1, die2);

		// Move player
		p.position += die1 + die2;

		// Collect $200 salary as you pass GO
		if (p.position >= 40) {
			p.position -= 40;
			p.money += 200;
			addAlert(p.name + " collected a $200 salary for passing GO.");
		}

		land();
	}
}