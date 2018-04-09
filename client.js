//var socket = io.connect('http://10.0.2.15:33339');
var you = {playerID: 0, STR: 5, AGI: 10, CuHP: 80, MxHP: 80, encounter: 1, lvl: 1}
var them = [
			{playerID: 1, STR: 5, AGI: 10, CuHP: 80, MxHP: 80, encounter: 1, lvl: 1, name: "Joe"}, 
			{playerID: 2, STR: 5, AGI: 10, CuHP: 80, MxHP: 80, encounter: 1, lvl: 1, name: "Shmoe"}, 
			{playerID: 1, STR: 5, AGI: 10, CuHP: 80, MxHP: 80, encounter: 1, lvl: 1, name: "Joe"}, 
			{playerID: 1, STR: 5, AGI: 10, CuHP: 80, MxHP: 80, encounter: 1, lvl: 1, name: "Joe"}, 
			]
var advantage = 0
var x = 0
var y = 6
var attackButtons = [
	"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>",
	"<p class='button attack center' onclick='fightChoose()'>Punch</p>", 
]
var attackChoiceButtons = [
	"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>"
]
var currentList = attackButtons
for(r = 0; r < them.length; r++){
	var acString = "<p class='button attack center' onclick='fight(" + r + ")'>" + them[r].name + "</p>"
	attackChoiceButtons.push(acString)
}

function update(who){
	them.push("update")
	/*socket.emit(
		'execute', who
	);*/
	them.pop()
	updateDisplay()
}
function updateDisplay(start, totalHP){
	if(totalHP > 0 && you.CuHP > 0){
		loadAttackMenu()
		document.getElementById('player').innerHTML = you.CuHP + " / " + you.MxHP
		if(start != undefined){
			for(r = 0; r < them.length; r++){
				ra = r + 1
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
		document.getElementById('menu').innerHTML = actionButtons
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
	updateDisplay()
}
function fightChoose(){
	currentList = attackChoiceButtons
	loadButtons(attackChoiceButtons, "rights")
}

function fight(choice){
	var totalHP = 0
	attack(you, them[choice])
	for(rz = 0; rz < them.length; rz++){
		if(them[rz].CuHP <= 0){
			them[rz].STR = 0
			them[rz].CuHP = 0
			attackChoiceButtons[rz + 1] = ""
		}
		AI("attack", rz)
		totalHP += them[rz].CuHP
	}
	updateDisplay(undefined, totalHP)
}
function attack(a, b){
	b.CuHP -= a.STR
	update(b)
}

/*function create(){
	r += 1
	
	document.getElementById('output').innerHTML = "You clicked the create button"
	list.push("units")
	socket.emit(
		'execute', list
	);
	list.pop()
}*/

function pull(){
	document.getElementById('output').innerHTML = "You clicked the pull button"
	socket.emit(
		'pull', 0
	)
}
/*socket.on('pull', function(data){
	console.log(data)
	//probally a better way of doing this
	you.push(data[0].playerID)
	you.push(data[0].strength)
	you.push(data[0].agility)
	you.push(data[0].currentHP)
	you.push(data[0].maxHP)
	you.push(data[0].encounterID)
	
	them.push(data[1].playerID)
    them.push(data[1].strength)
    them.push(data[1].agility)
    them.push(data[1].currentHP)
    them.push(data[1].maxHP)
    them.push(data[1].encounterID)
})*/

updateDisplay('asd', 9999)