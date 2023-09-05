var inicioIn = document.getElementById('inicio');
var fimIn = document.getElementById('fim');
var passoIn = document.getElementById('passo');
var contar = document.getElementById('contar');
var contagem = document.getElementById('contagem');

contar.addEventListener('click', contarValores);

function contarValores() {
    var inicioOut = Number(inicioIn.value);
    var fimOut = Number(fimIn.value);
    var passoOut = Number(passoIn.value);
    
    contagem.innerHTML = ''; // Limpa o conteúdo anterior da contagem
    
    if (passoOut <= 0) {
        contagem.innerHTML = 'O passo deve ser maior que zero. OK?';
        return;
    }

    if (inicioOut <= fimOut) {
        for (var valorAtual = inicioOut; valorAtual <= fimOut; valorAtual += passoOut) {
            var seta = (valorAtual + passoOut <= fimOut) ? ' → ' : '';
            contagem.innerHTML += `${valorAtual}${seta}`;
        }
    } else {
        for (var valorAtual = inicioOut; valorAtual >= fimOut; valorAtual -= passoOut) {
            var seta = (valorAtual - passoOut >= fimOut) ? ' ← ' : '';
            contagem.innerHTML += `${valorAtual}${seta}`;
        }
    }
}
