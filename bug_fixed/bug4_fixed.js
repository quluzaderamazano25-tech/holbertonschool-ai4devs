[System.IO.File]::WriteAllText("$base\bug4_fixed.js", @"
async function getUserNames(url) {
    const response = await fetch(url);
    const data = await response.json();
    const names = data.map(user => user.name.toUpperCase());
    return names;
}

async function main() {
    const url = 'https://jsonplaceholder.typicode.com/users';
    const names = await getUserNames(url);
    console.log('Names:', names);
}

main();
"@, [System.Text.Encoding]::ASCII)