function average(numbers) {
    /**
     * Massivdəki rəqəmlərin ortalamasını hesablayır.
     * NaN dəyərləri süzülür və reduce üçün 0 başlanğıcı təyin edilir.
     */
    const validNumbers = numbers.filter(n => {
        return typeof n === "number" && !Number.isNaN(n);
    });

    if (validNumbers.length === 0) {
        return 0;
    }

    const sum = validNumbers.reduce((acc, current) => {
        return acc + current;
    }, 0);

    return parseFloat((sum / validNumbers.length).toFixed(2));
}