<<<<<<< HEAD
var socket = io.connect('http://192.168.10.206:33339');
=======
var socket = io.connect('http://192.168.10.206:33333');
>>>>>>> 8b21a4f29b917263cbd523bbc4d5eebf70a012b9
var r = 0
function update(which){
	var send = r + " " + which
	socket.emit(
		'execute', send
	);
	
	r += 1
}