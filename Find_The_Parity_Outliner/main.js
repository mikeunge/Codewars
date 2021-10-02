function findOutlier(integers){
	let even = [];
	let odd = [];
	integers.forEach(i => i%2 ? odd.push(i) : even.push(i));
	return even.length > 1 ? odd[0] : even[0];
}

(findOutlier([0, 1, 2]) == 1) ? console.log("ok") : console.log("wrong");