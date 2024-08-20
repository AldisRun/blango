const theNumber = 2; // Change theNumber to something other than 1
let yourName = 'Ben'; // Initial assignment in the outer scope

if (theNumber === 1) {
  yourName = 'Leo'; // Just assign 'Leo' without redeclaring yourName
  alert(yourName);
}

alert(yourName); // This will alert 'Ben' since the if block won't execute