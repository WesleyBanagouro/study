let num = [3, 6, 9, 10, 44, 34]

for (let pos = 0; pos < num.length; pos++){
    console.log(`Na posição ${pos} temos os números ${num[pos]}.`)
}

for (let pos in num) {
    console.log(`Na posição ${pos} temos os números ${num[pos]}.`)
}