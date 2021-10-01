let number = (busStops) => {
	let remainder = 0;
	busStops.forEach(s => {
		remainder += s[0];
		remainder -= s[1];
	});
	return remainder;
}


(number([[10,0],[3,5],[5,8]]) == 5) ? console.log("ok") : console.log("wrong");
