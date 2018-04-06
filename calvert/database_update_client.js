var socket = io.connect('http://10.0.2.15:33339');
var r = 0
function update(which){
	var send = r + " " + which
	socket.emit(
		'execute', send
	);
	
	r += 1
}