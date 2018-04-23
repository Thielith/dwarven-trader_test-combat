var mysql = require('mysql'); 
var io = require('socket.io').listen(33333);
const {exec} = require('child_process');

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "p2950",
	database: "test_dwarven"
})


io.sockets.on('connection', function (socket) {
	var clientIp = socket.request.connection.remoteAddress;
	console.log("Someone From " + clientIp + " Connected")
	
	socket.on('calvert', function () {
		var e = 'python simple.py'
		console.log(e)
		exec(e);
	});
	
	socket.on('getPlayerData', function(id){
		console.log("player")
		var sql = "SELECT * FROM units WHERE id = " + id + ";"
		con.query(sql, function(err, result){
			if (err) throw err;
			console.log(result)
			socket.emit(
				'getPlayerData', result
			);
		})
	})
	
	socket.on('getAttacks', function(level){
		console.log("attack")
		var sql = "SELECT * FROM _attack_ WHERE level <= " + level + ";"
		con.query(sql, function(err, result){
			if (err) throw err;
			console.log(result)
			for(var e = 0; e < result.length; e++){
				var sql1 = "SELECT * FROM attack_e WHERE attackID = " + result[e].attackID + ";"
				con.query(sql1, function(err1, result1){
					if (err1) throw err1;
					console.log(result1)
					result[e].attackID = result1[0].attackName
				})
				var sql2 = "SELECT * FROM combat_style_e WHERE id = " + result[e].typeID + ";"
				con.query(sql1, function(err2, result2){
					if (err2) throw err2;
					console.log(result2)
					result[e].typeID = result2[0].styleName
				})
			}
			socket.emit(
				'getAttacks', result
			)
		})
	})
	
	socket.on('getInCombat', function(id){
		console.log("combat")
		var sql = "SELECT * FROM units WHERE encounterID = " + id[0] + ";"
		con.query(sql, function(err, result){
			if (err) throw err;
			var send = []
			for(var d = 0; d < result.length; d++) {
				if(result[d].id != id[1]){
					send.push(result[d])
				}
			}
			socket.emit(
				'getInCombat', send
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
