function fatorial(n) {
    let res = 1; 
    for (let i = n; i > 1; i--) {
        res *= i; 
    }
    return res;
}

console.log(fatorial(6));
