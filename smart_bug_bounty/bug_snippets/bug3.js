function average(numbers) {
    const valid = numbers.filter(n => typeof n === "number");
    const sum = valid.reduce((acc, n) => acc + n);
    return (sum / valid.length).toFixed(2);
}

console.log(average([1, 2, 3, 4, 5]));
console.log(average([10, "hello", null, 20]));
console.log(average([]));
console.log(average([NaN, 1, 2]));