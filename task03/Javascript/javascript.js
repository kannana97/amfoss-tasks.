const readline = require('readline');


const isprime = (num) => {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question('Enter a number: ',(input) => {
    const n = parseInt(input);
    console.log(`Prime numbers up to ${n} are:`);
    for (let i = 2; i <= n; i++) {
        if (isprime(i)) {
            process.stdout.write(`${i} `);
        }
    }
    console.log(); // Newline after the list
    rl.close();
});
