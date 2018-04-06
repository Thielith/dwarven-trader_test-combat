var socket = io.connect('http://localhost');
var r = 0
function update(which){
	var send = r + " " + which
	socket.emit(
		'execute', send
	);
	
	r += 1
}