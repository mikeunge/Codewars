function declareWinner(fighter1, fighter2, firstAttacker) {
  let next = firstAttacker;
  let winner = "";
  while (true) {
    if (fighter1.name == next) {
      fighter2.health -= fighter1.damagePerAttack;
      (fighter2.health <= 0) ? winner = fighter1.name : next = fighter2.name;
    } else {
      fighter1.health -= fighter2.damagePerAttack;
      (fighter1.health <= 0) ? winner = fighter2.name : next = fighter1.name;
    }
    if (winner != "") {
      return winner;
    }
  }
}
