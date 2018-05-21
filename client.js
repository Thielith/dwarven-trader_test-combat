var socket = io.connect('http://192.168.10.206:33333');
var you = {playerID: 0, STR: undefined, AGI: undefined, CuHP: undefined, MxHP: undefined, encounter: undefined, lvl: undefined, name: undefined, advantage: undefined}
var them = []
var advantage = 0
var x = 0
var y = 6
var damage = 1, adCost = 0
var statusGive, statusGet, statusClear, statuses = [], statusNames = []
var attackButtons = [
	"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>",
	"<p class='button attack center' onclick='fightChoose(1, 0, -1, -1, -1)'>Punch</p>", 
]
var attackChoiceButtons = [
	"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>"
]
var currentList = attackButtons
var attackList;
//Things are VERY much broken. Enemys attack too many times, went from 3 advantage to -97. Loads enemies in twice for display. Status lsit has duplicates, maybe because statusID is = undefined
//Enemys only attack too amny times when kicking. Loading enemys twice in display fixed. updateStatus python script is always undefined and theres alot of them.
//Enemys nerver attacked too many times, bug with advantage. Duplicates dont exist now
//Player gets status but enemy doesn't. Check process of adding statuses.
socket.emit('getPlayerData', you.playerID);
socket.on('getPlayerData', function(data){
	you.STR = data[0].strength
	you.AGI = data[0].agility
	you.CuHP = data[0].currentHP
	you.MxHP = data[0].maxHP
	you.encounter = data[0].encounterID
	you.lvl = data[0].level
	you.name = data[0].name
	you.advantage = data[0].advantage
	advantage = you.advantage
	var send = [you.encounter, you.playerID]
	socket.emit('getInCombat', send);
})
socket.on('getInCombat', function(data){
	for(d = 0; d < data.length; d++){
		var something = {playerID: undefined, STR: undefined, AGI: undefined, CuHP: undefined, MxHP: undefined, encounter: undefined, lvl: undefined, name: undefined, advantage: undefined}
		something.playerID = data[d].id
		something.STR = data[d].strength
		something.AGI = data[d].agility
		something.CuHP = data[d].currentHP
		something.MxHP = data[d].maxHP
		something.encounter = data[d].encounterID
		something.lvl = data[d].level
		something.name = data[d].name
		something.advantage = data[d].advantage
		them.push(something)
	}
	
	for(r = 0; r < them.length; r++){
		var acString = "<p class='button attack center' onclick='fight(" + r + ")'>" + them[r].name + "</p>"
		attackChoiceButtons.push(acString)
	}
	socket.emit('getAttacks', you.lvl)
})
socket.on('getAttacks', function(data){
	attackList = data
	socket.emit('getPlayerStatus', you.playerID)

})
socket.on('getPlayerStatus', function(data){
	if(data.length != 0){
		statuses.push(data)
	}
	
	var m = 0, loopa;
	function loop(){
		if(m < them.length - 1){
			loopa = setTimeout(function(){
				socket.emit('getStatuses', them[m].playerID)
				clearTimeout(loopa);
				loop();
				m += 1
			}, 200)
		}
		else{
			m = 0
		}
	}
	loop()
	socket.emit('getStatusNames')
})
socket.on('getStatuses', function(data){
	if(data.length != 0){
		statuses.push(data)
	}
})
socket.on('getStatusNames', function(data){
	if(data.length != 0){
		statusNames.push(data)
	}
	setTimeout(function(){
		updateDisplay("start", 9999)
	}, 250);
})

function updateDatabase(who){
	socket.emit('updateDB', who)
	statuses.unshift(who.playerID)
	socket.emit('updateStatus', statuses)
	console.log(statuses)
	statuses.shift()
	
}
function updateDisplay(start, totalHP){
	if(totalHP > 0 && you.CuHP > 0){
		loadAttackMenu()
		document.getElementById('player').innerHTML = you.name + ": " + you.CuHP + " / " + you.MxHP
		
		if(start != undefined){
			for(r = 0; r < them.length; r++){
				var t = document.getElementById('enemy').innerHTML =
					document.getElementById('enemy').innerHTML
					+ "<p id='enemy" + r + "'>" + them[r].name + ": " + them[r].CuHP + " / " + them[r].MxHP + "</p>";
			}
		}
		else{
			for(r = 0; r < them.length; r++){
				document.getElementById('enemy' + r).innerHTML = them[r].name + ": " + them[r].CuHP + " / " + them[r].MxHP
			}
		}
		document.getElementById('playerStatus').innerHTML = "null"
		document.getElementById('enemyStatus').innerHTML = "null"
		if(statuses.length != 0){
			for(st = 0; st < statuses.length; st++){
				if(statuses[st].unitID == you.playerID){
					document.getElementById('playerStatus').innerHTML =
						document.getElementById('playerStatus').innerHTML
						+ "<p id='playerStatus" + st + "'>" + statusNames[statuses[st].statusID].statusName + "</p>";
				}
				for(ste = 0; ste < them.length; ste++){
					if(statuses[st].unitID == them[ste].playerID){
						document.getElementById('enemyStatus').innerHTML =
							document.getElementById('enemyStatus').innerHTML
							+ "<p id='enemyStatus" + ste + "'>" + statusNames[statuses[st].statusID].statusName + "</p>";
					}
				}
			}
		}
		
		document.getElementById('advantage').innerHTML = advantage
	}
	else if(you.CuHP <= 0){
		document.getElementById('menu').innerHTML = "<p class='stayCenter'>You Lose!</p>"
		document.getElementById('player').innerHTML = "0 / " + you.MxHP
	}
	else{
		document.getElementById('menu').innerHTML = "<p class='stayCenter'>You Win!</p>"
		for(r = 0; r < them.length; r++){
			document.getElementById('enemy' + r).innerHTML = them[r].CuHP + " / " + them[r].MxHP
		}
	}
	
	
}
function loadAttackMenu(){
	var mainButtons = [
		"<p class='button attack center' onclick='choice(1)'>Attack</p>", 
		"<p class='button attack center' onclick='choice(2)'>Items</p>", 
		"<p class='button attack center' onclick='choice(3)'>Actions</p>"
	]
	document.getElementById('menu').innerHTML = mainButtons[0]
	for(rz = 1; rz < mainButtons.length; rz++){
		var t = document.getElementById('menu').innerHTML =
			document.getElementById('menu').innerHTML
			+ mainButtons[rz]
	}
	document.getElementById('rightButton').style.display = "none"
	document.getElementById('leftButton').style.display = "none"
}

function AI(state, which){
	var aiChoice = Math.floor((Math.random() * 3) + 1);
	if(aiChoice == 1){
		aiChoice = 1 //will be more eventually
		if(aiChoice == 1){
			if(state == "attack" || state == "tripped"){
				attack(them[which], you)
			}
			else if(state == "defend"){
				advantage += 2
			}
			else if(state == "counter"){
				attack(you, them[which])
			}
			
		}
	}
	else if(aiChoice == 2){
		//for when items are implemented
		console.log("Items")
		document.getElementById('output').innerHTML = "they chose items"
	}
	else if(aiChoice == 3){
		aiChoice = Math.floor((Math.random() * 3) + 1);
		
		if(aiChoice == 1){
			//run
			console.log("run")
			number = Math.floor((Math.random() * 100) + 1);
			if(number < 25){
				document.getElementById('menu').innerHTML = "<p class='center'>The enemy ran away</p> <p class='center'>You won x gold and 0 xp!</p>"
			}
			else{
				document.getElementById('output').innerHTML = "they tripped"
				advantage += 2
			}
		}
		else if(aiChoice == 2){
			//defend
			console.log("defend")
			document.getElementById('output').innerHTML = "they defend"
			if(state == "attack"){
				advantage -= 2
			}
			else if(state == "defend"){
				document.getElementById('output').innerHTML = "you both defend"
			}
			else if(state == "counter"){
				advantage -= 1
			}
		}
		else if(aiChoice == 3){
			//counter
			console.log("counter")
			document.getElementById('output').innerHTML = "they counter"
			if(state == "attack"){
				attack(them[which], you)
			}
			else if(state == "defend"){
				advantage += 1
			}
			else if(state == "counter"){
				document.getElementById('output').innerHTML = "you both counter"
			}
		}
	}

}

function loadButtons(list, direction){
	if(list.length > 6){
		document.getElementById('rightButton').style.display = "inline"
	}
	if(direction == "left"){
		x -= 6
		y -= 6
		document.getElementById('rightButton').style.display = "inline"
	}
	else if(direction == "right"){
		x += 6
		y += 6
		document.getElementById('leftButton').style.display = "inline"
	}
	currentButtons = list.slice(x, y)
	document.getElementById('menu').innerHTML = currentButtons[0]
	for(rz = 1; rz < currentButtons.length; rz++){
		var t = document.getElementById('menu').innerHTML =
			document.getElementById('menu').innerHTML
			+ currentButtons[rz]
	}
	
	if(x <= 0){
		document.getElementById('leftButton').style.display = "none"
	}
	else if(y >= list.length){
		document.getElementById('rightButton').style.display = "none"
	}	
	
}
function choice(pick){
	if(pick == 1){
		document.getElementById('output').innerHTML = "You clicked the attack button"
		
		for(a = 0; a < attackList.length; a++){
			if(attackList[a].advantage <= advantage){
				var newButton = "<p class='button attack center' onclick='fightChoose(" + 
				attackList[a].damage + ", " + attackList[a].advantageCost + ", " + 
				attackList[a].effectGive + ", " + attackList[a].effectGet + ", " + attackList[a].effectClear +
				")'>" + attackList[a].attackID + "</p>"
				if(attackButtons.includes(newButton) == false){
					attackButtons.push(newButton)
				}
			}
		}
		
		if(attackButtons.length > 6){
			document.getElementById('rightButton').style.display = "inline"
			loadButtons(attackButtons, "rights")
		}
		else{
			document.getElementById('menu').innerHTML = attackButtons[0]
			for(rz = 1; rz < attackButtons.length; rz++){
				var t = document.getElementById('menu').innerHTML =
					document.getElementById('menu').innerHTML
					+ attackButtons[rz]
			}
		}
	}
	else if(pick == 2){
		//when items are implemented
	}
	else if(pick == 3){
		actionButtons = [
		"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>",
		"<p class='button attack center' onclick='actions(1)'>Run</p>",
		"<p class='button attack center' onclick='actions(2)'>Defend</p>",
		"<p class='button attack center' onclick='actions(3)'>Counter</p>"
		]
		document.getElementById('output').innerHTML = "You clicked the actions button"
		loadButtons(actionButtons, "righty")
	}
	
}
function actions(choice){
	if(choice == 1){
		number = Math.floor((Math.random() * 100) + 1);
		if(number < 75){
				document.getElementById('menu').innerHTML = "<p class='stayCenter'>You ran away and left all of your stuff behind</p>"
				exit()
			}
			else{
				document.getElementById('output').innerHTML = "You tripped"
				loadAttackMenu()
				for(r = 0; r < them.length; r++){
					AI("tripped", r)
				}
			}
	}
	else if(choice == 2){
		document.getElementById('output').innerHTML = "You defend"
		for(r = 0; r < them.length; r++){
			AI("defend", r)
		}
	}
	else if(choice == 3){
		document.getElementById('output').innerHTML = "You counter"
		for(r = 0; r < them.length; r++){
			AI("counter", r)
		}
	}
	updateDisplay(undefined, 9999)
}
function fightChoose(k, ad, give, get, clear){
	currentList = attackChoiceButtons
	damage = k, adCost = ad
	statusGive = give, statusGet = get, statusClear = clear
	loadButtons(attackChoiceButtons, "rights")
}

function fight(choice){
	var totalHP = 0
	you.STR += damage
	attack(you, them[choice])
	if(statusClear != -1 && statusClear != undefined){
		console.log("clear status " + statusClear)
		for(s = 0; s < statuses.length; s++){
			if(statuses[s].unitID == you.playerID && statusClear == statuses[s].statusID){
				statuses.splice(s, 1)
			}
		}
	}
	if(statusGet != -1 && statusGet != undefined){
		console.log("get status " + statusGet)
		statuses.push({unitID: you.playerID, statusID: statusGet, magnitude: 1})
	}
	if(statusGive != -1 && them[choice].CuHP > 0 && statusGive != undefined){
		console.log("gave status " + statusGive)
		var a = statuses.push({unitID: them[choice].playerID, statusID: statusGive, magnitude: 1})
		console.log(a)
	}
	
	if(them.length > 1){
		for(rz = 0; rz < them.length; rz++){
			if(them[rz].CuHP <= 0){
				them[rz].STR = 0
				them[rz].CuHP = 0
				attackChoiceButtons[rz + 1] = ""
			}
			
			AI("attack", rz)
			totalHP += them[rz].CuHP
		}
	}
	else{
		if(them[0].CuHP <= 0){
			them[0].STR = 0
			them[0].CuHP = 0
			attackChoiceButtons[rz + 1] = ""
		}
		AI("attack", 0)
		totalHP = them[0].CuHP
	}
	resolve(totalHP)
}
function attack(a, b){
	b.CuHP -= a.STR
}

function resolve(totalHP){
	you.STR -= damage
	advantage -= adCost
	damage = 1
	adCost = 0
	console.log(statuses)
	
	for(i = 0; i < statuses.length; i++){
		for(j = 0; j < statuses.length; j++){
			if(i != j){
				if(statuses[i].unitID == statuses[j].unitID && statuses[i].statusID == statuses[j].statusID){
					statuses.splice(j, 1)
				} 
			}
		}
	}
	statuses.splice(statuses.length - 1, 1)
	
	you.advantage = advantage
	updateDatabase(you)
	for(u = 0; u < them.length; u++){
		them[u].advantage = -advantage
		updateDatabase(them[u])
	}
	
	attackButtons = [
	"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>",
	"<p class='button attack center' onclick='fightChoose(1, 0, -1, -1, -1)'>Punch</p>", 
	]
	updateDisplay(undefined, totalHP)
}
