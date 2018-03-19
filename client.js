/*
	Code for creating tables:
	create database test_dwarven;
	create table units (playerID INT, strength INT, aglility INT, currentHP INT, maxHP INT, encounterID INT);
	create table currentStatus (playerID INT, statusID INT);
	create table combat (playerID INT, encounterID INT, currentTurn INT);
*/

//CONSTANTS
//playerID INT, strength INT, aglility INT, currentHP INT, maxHP INT, encounterID INT
var ID = 0, STR = 1, AGI = 2, CuHP = 3, MxHP = 4, encounter = 5


//var socket = io.connect('http://10.0.2.15:33339');
var r = 0
var you = [0, 5, 10, 80, 80, 0]
var them = [1, 5, 10, 80, 80, 0]

function update(who){
	them.push("update")
	/*socket.emit(
		'execute', who
	);*/
	them.pop()
	document.getElementById('player').innerHTML = you[CuHP]
	document.getElementById('enemy').innerHTML = them[CuHP]
}

function AI(){
	var aiChoice = Math.floor((Math.random() * 3) + 1);
	if(aiChoice == 1){
		aiChoice = 1 //will be more eventually
		if(aiChoice == 1){
			attack(them, you)
		}
	}
	else if(aiChoice == 2){
		//for when items are implemented
		console.log("Items")
	}
	else if(aiChoice == 3){
		aiChoice = Math.floor((Math.random() * 1) + 1);
		
		if(aiChoice == 1){
			//run
			console.log("run")
			number = Math.floor((Math.random() * 100) + 1);
			if(number < 25){
				document.getElementById('menu').innerHTML = "<p class='center'>The enemy ran away</p> <p class='center'>You won x gold and 0 xp!</p>"
			}
			else{
				document.getElementById('output').innerHTML = "they tripped"
			}
		}
		else if(aiChoice == 2){
			//defend
			console.log("defend")
		}
		else if(aiChoice == 3){
			//counter
			console.log("counter")
		}
	}
}

function loadAttackMenu(){
	var mainButtons = [
		"<p class='button attack center' onclick='choice(1)'>Attack</p>",
		"<p class='button attack center' onclick='choice(2)'>Items</p>",
		"<p class='button attack center' onclick='choice(3)'>Actions</p>"
	]
	document.getElementById('menu').innerHTML = mainButtons
}

function choice(pick){
	var buttons = []
	if(pick == 1){
		buttons = [
		"<p class='button attack center' onclick='fight()'>Basic Attack</p>",
		"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>"
		]
		document.getElementById('output').innerHTML = "You clicked the attack button"
		document.getElementById('menu').innerHTML = buttons
	}
	else if(pick == 2){
		//when items are implemented
	}
	else if(pick == 3){
		buttons = [
		"<p class='button attack center' onclick='actions(1)'>Run</p>",
		"<p class='button attack center' onclick='actions(2)'>Defend</p>",
		"<p class='button attack center' onclick='actions(3)'>Counter</p>",
		"<p class='button attack center' onclick='loadAttackMenu()'>Back</p>"
		]
		document.getElementById('output').innerHTML = "You clicked the actions button"
		document.getElementById('menu').innerHTML = buttons
	}
	
}
function attack(a, b){
	b[CuHP] -= a[STR]
	update(b)
}
function actions(choice){
	if(choice == 1){
		number = Math.floor((Math.random() * 100) + 1);
		if(number < 75){
				document.getElementById('menu').innerHTML = "<p class='stayCenter'>You ran away and left all of your stuff behind</p>"
			}
			else{
				document.getElementById('output').innerHTML = "You tripped"
				loadAttackMenu()
			}
	}
}

function fight(){
	attack(you, them)
	AI()
	if(them[CuHP] > 0){
		loadAttackMenu()
	}
	else{
		document.getElementById('menu').innerHTML = "<p class='stayCenter'>You Win!</p>"
	}
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