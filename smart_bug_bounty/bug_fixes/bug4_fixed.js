async function getUserNames(url) {
    /**
     * URL-dən istifadəçi adlarını çəkir və böyük hərflə qaytarır.
     * fetch və json() əməliyyatları await ilə gözlənilir.
     */
    try {
        const response = await fetch(url);
        const data = await response.json();
        
        const upperCaseNames = data.map(user => {
            return user.name.toUpperCase();
        });
        
        return upperCaseNames;
    } catch (error) {
        return [];
    }
}