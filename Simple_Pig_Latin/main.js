function pigIt(str) {
    let newArr = [];
    str.split(" ").forEach(s => {
        let arr = [];
        // check for any special characters, if any occur, push directly to stack.
        if (s.match(/[a-zA-Z]/i)) {
            s.split("").forEach(e => {
                arr.push(e);
            });
            arr.push(arr.shift(), "ay");
        } else {
            arr.push(s);
        }
        newArr.push(arr.join(""));
    });
    return newArr.join(" ");
}

(pigIt('Pig latin is cool') == 'igPay atinlay siay oolcay') ? console.log("ok") : console.log("wrong");