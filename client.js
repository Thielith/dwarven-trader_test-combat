/*
	Code for creating tables:
	create database test_dwarven;
	create table units (playerID INT, strength INT, aglility INT, currentHP INT, maxHP INT, encounterID INT);
	create table currentStatus (playerID INT, statusID INT);
	create table combat (playerID INT, encounterID INT, currentTurn INT);
*/


var socket = io.connect('http://10.0.2.15:33339');
var r = 0
//playerID INT, strength INT, aglility INT, currentHP INT, maxHP INT, encounterID INT
var you = []
var them = []

function update(){
	them.push("update")
	socket.emit(
		'execute', them
	);
	them.pop()
	document.getElementById('player').innerHTML = you[3]
	document.getElementById('enemy').innerHTML = them[3]
}

function attack(){
	document.getElementById('output').innerHTML = "You clicked the attack button"
	them[3] -= 1
	update()
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

socket.on('pull', function(data){
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
})