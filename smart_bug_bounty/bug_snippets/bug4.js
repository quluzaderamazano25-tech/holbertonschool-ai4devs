async function getUserNames(url) {
    const response = fetch(url);
    const data = response.json();
    const names = data.map(user => user.name.toUpperCase());
    return names;
}

const result = getUserNames("https://jsonplaceholder.typicode.com/users");
console.log("Names:", result);
console.log("Fetching user names...");