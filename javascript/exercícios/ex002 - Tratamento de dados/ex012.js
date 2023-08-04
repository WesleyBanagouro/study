var agora = new Date()
var hora = agora.getHours()

console.log(`Agora são ${hora} horas.`)
if (hora <= 12) {
    console.log(`Bom dia, Wesley!`)
} else if (hora > 12 && hora < 18) {
    console.log(`Boa tarde, Wesley!`)
} else {
    console.log(`Boa noite, Wesley!`)
}