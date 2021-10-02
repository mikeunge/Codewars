const assert = require('assert');

function rgb(r, g, b){
	let colorArr = [r, g, b];
	let hex = '';
	colorArr.forEach(color => {
		color < 0 ? color = 0 : color = color; // check for under 0 
		color > 255 ? color = 255 : color = color; // check for everything over 255
		let x = color.toString(16);
		x.length < 2 ? hex += x.padStart(2, "0") : hex += x;
	});
	return hex.toUpperCase();
}


assert.equal(rgb(0, 0, -20), '000000');
assert.equal(rgb(300,255,255), 'FFFFFF');
assert.equal(rgb(173,255,47), 'ADFF2F');
assert.equal(rgb(82,22,7), '521607');
