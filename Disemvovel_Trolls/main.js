function disemvowel(str) {
  let words = [];
  for (const w of str.split(" ")) {
    let n = "";
    [...w].forEach(c => {
      if (!(c.toLowerCase() == "a" || c.toLowerCase() == "e" || c.toLowerCase() == "i" || c.toLowerCase() == "o" || c.toLowerCase() == "u")) { n += c; }
    });
    words.push(n);
  }
  return words.join(" ");
}
