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
	
	socket.on('calvert', function (info) {
		var e = 'python database.py ' + info
		console.log(e)
		exec(e);
	});
	
	socket.on('getPlayerData', function(id){
		var sql = "SELECT * FROM units WHERE id = " + id + ";"
		con.query(sql, function(err, result){
			if (err) throw err;
			console.log(result)
			
			socket.emit(
				'getPlayerData', result
			);
		})
	})
	
	socket.on('getInCombat', function(id){
		var sql = "SELECT * FROM units WHERE encounterID = " + id + ";"
		con.query(sql, function(err, result){
			if (err) throw err;
			console.log(result)
			
			socket.emit(
				'getInCombat', result
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
