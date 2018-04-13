var socket = io.connect('http://192.168.10.206:33333');
var r = 0
function update(which){
	var send = r + " " + which
	socket.emit(
		'execute', send
	);
	
	r += 1
}