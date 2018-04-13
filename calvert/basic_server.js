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
	socket.on('execute', function (info) {
		var e = 'python database.py ' + info
		console.log(e)
		exec(e);
	});
});
