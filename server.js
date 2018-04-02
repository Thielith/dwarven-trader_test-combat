/*
	Code for creating tables:
	create database test_dwarven;
	create table units (playerID INT, strength INT, aglility INT, currentHP INT, maxHP INT, encounterID INT);
	create table currentStatus (playerID INT, statusID INT);
	create table combat (playerID INT, encounterID INT, currentTurn INT);
	create table statusList (statusID INT, statusName VARCHAR(16));
	create table attacks (level INT, advantage INT, advantageCost INT, attackID INT, typeID INT, effectGive INT, effectGet INT, effectClear INT);
	create table attackTypes (typeID INT, typeName INT);
	create table attackList (attackID INT, attackName VARCHAR(16));
*/
var mysql = require('mysql'); 
var io = require('socket.io').listen(33339);
const {exec} = require('child_process');

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "asdf",
	database: "test_dwarven"
})


io.sockets.on('connection', function (socket) {
	var clientIp = socket.request.connection.remoteAddress;
	console.log("Someone From " + clientIp + " Connected")
	
	socket.on('pull', function(id){
		var sendLine = []
		var sql = "SELECT * FROM units WHERE encounterID = " + id + ";"
		con.query(sql, function(err, result){
			if (err) throw err;
			console.log(result)
			
			socket.emit(
				'pull', result
			);
		})
	})

	socket.on('execute', function (info) {
		console.log(info)
		
		var sendLine = ""
		var o;
		for(i = 0; i < info.length - 1 ; i++){
			console.log(info[i])
			sendLine += info[i] + " "
			o = i
		}
		
		sendLine += "'" + info[o + 1] + "'"
		
		var e = 'python database.py ' + sendLine
		console.log(e)
		exec(e);
	});
	
	socket.on('disconnect', function(){
		console.log("Someone From " + clientIp + " disconnected")
	})
});
