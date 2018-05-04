var mysql = require('mysql'); 
var io = require('socket.io').listen(33333);
const {exec} = require('child_process');

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "p2950",
	database: "test_dwarven"
})

function getSizeOfObject(obj) {
    var size = 0, key;
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
}

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
			for(var e = 0; e < result.length; e++){
				var sql1 = "SELECT * FROM attack_e WHERE attackID = " + result[e].attackID + ";"
				con.query(sql1, function(err1, result1){
					if (err1) throw err1;
					result[e - 1].attackID = result1[0].attackName
				})
				var sql2 = "SELECT * FROM combat_style_e WHERE id = " + result[e].typeID + ";"
				con.query(sql2, function(err2, result2){
					if (err2) throw err2;
					result[e - 1].typeID = result2[0].styleName
				})
			}
			setTimeout(function(){
				socket.emit(
					'getAttacks', result
				)
			}, 500);
			
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

	socket.on('updateDB', function (info) {
		var sendLine = ""
		sendLine += info.playerID + " " + info.STR + " " + info.AGI + " " + info.CuHP + " " + info.MxHP + " " + info.encounter + " " + info.lvl + " '" + info.name + "'"
		
		var e = "python database.py 'updateUnits' " + sendLine
		exec(e);
	});
	
	socket.on('disconnect', function(){
		console.log("Someone From " + clientIp + " disconnected")
	})
});
