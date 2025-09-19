var romanToInt = function (s) {
  let output = 0;

  const romanMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  for (let i = 0; i < s.length; i++) {
    const currentSymbol = s[i];
    let nextSymbol = "I";
    if (s[i + 1]) {
      nextSymbol = s[i + 1];
    }

    // for use cases, when the number is reversed eg IV or XC
    if (romanMap[nextSymbol] > romanMap[currentSymbol]) {
      output -= romanMap[currentSymbol];
      continue;
    }

    output += romanMap[currentSymbol];
  }

  return output;
};

console.log(romanToInt("III"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("MCMXCIV"));
