[System.IO.File]::WriteAllText("$base\bug3_fixed.js", @"
function average(numbers) {
    const valid = numbers.filter(n => typeof n === 'number' && !Number.isNaN(n));
    if (valid.length === 0) return 0;
    const sum = valid.reduce((acc, n) => acc + n, 0);
    return parseFloat((sum / valid.length).toFixed(2));
}

console.log(average([1, 2, 3, 4, 5]));
console.log(average([10, 'hello', null, 20]));
console.log(average([]));
console.log(average([1.5, 2.5, NaN, 3]));
"@, [System.Text.Encoding]::ASCII)