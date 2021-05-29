const generateRandomIndex = (lower, upper) => {
  let range = upper - lower + 1;
  let random = Math.floor(Math.random() * range) + lower;
  return random;
};

const generateNumbers = (start, end) => {
  let arr = [];
  for (let i = start; i <= end; i++) {
    arr.push(i);
  }
  return arr;
};

const createFinalArray = (lower, upper) => {
  if (
    upper == null ||
    lower == null ||
    upper == undefined ||
    lower == undefined
  ) {
    console.log("Cannot pass null or undefined as a parameter");
    return [];
  }
  let tempArr = [];
  let numberArray = generateNumbers(lower, upper);
  for (let i = 0; i < upper - lower; i++) {
    let randomIndex = generateRandomIndex(0, numberArray.length - 1);
    tempArr.push(...numberArray.splice(randomIndex, 1));
  }
  return tempArr;
};
let finalArray = createFinalArray(1, 20);
let secondFinalArray = createFinalArray(1, 20);
console.log(finalArray);
console.log(secondFinalArray);
