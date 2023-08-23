var inicioIn = document.getElementById('inicio');
var fimIn = document.getElementById('fim');
var passoIn = document.getElementById('passo');
var contar = document.getElementById('contar');
var contagem = document.getElementById('contagem');

contar.addEventListener('click', guardar);

function guardar() {
    var fimOut = Number(fimIn.value);
    var passoOut = Number(passoIn.value);
    var inicioOut = Number(inicioIn.value);
    
    contagem.innerHTML = ''; // Limpa o conteúdo anterior da contagem
    
    // Loop para exibir cada valor respeitando o passo
    for (var valorAtual = inicioOut; valorAtual <= fimOut; valorAtual += passoOut) {
        var seta = (valorAtual + passoOut <= fimOut) ? ' → ' : '';
        contagem.innerHTML += `${valorAtual}${seta}`;
    }
}
