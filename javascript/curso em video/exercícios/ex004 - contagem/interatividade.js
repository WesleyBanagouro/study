var agora = new Date();
var hora = agora.getHours();
var minutos = agora.getMinutes();
var horario = window.document.getElementById('horario');
var saudacao = document.getElementById('saudacao')
var nome = window.prompt('Qual é o seu nome?');
var imagem = document.getElementById('imagem');
var fundo = document.body;

if (hora < 12 && hora >= 6) {
    saudacao.innerHTML = `Bom dia, ${nome}!`;
    horario.innerHTML = `Agora são ${hora}h${minutos}.`;
    imagem.src = "manha.png";
    imagem.alt = "manha";
    fundo.style.background = "#5CF2F2";
} else if (hora >= 12 && hora < 18) {
    saudacao.innerHTML = `Boa tarde, ${nome}!`;
    horario.innerHTML = `Agora são ${hora}h${minutos}.`;
    imagem.src = "tarde.png";
    imagem.alt = "tarde";
    fundo.style.background = "#F29F05";
} else {
    saudacao.innerHTML = `Boa noite, ${nome}!`;
    horario.innerHTML = `Agora são ${hora}h${minutos}.`;
    imagem.src = "noite.png";
    imagem.alt = "noite";
    fundo.style.background = "#0B215E";
}
