function calcular() {
    var titulo = document.getElementById("titulo").value;
    var duracao = Number(document.getElementById("duracao").value);
    var convertido_horas = Math.floor(duracao / 60);
    var convertido_minutos = duracao % 60;
    var outTitulo = document.getElementById("filme");
    var outDuracao = document.getElementById("tempo");
    outTitulo.textContent = 'O filme escolhido foi o ' + titulo + '.';
    outDuracao.textContent = convertido_horas + ' hora(s) e ' + convertido_minutos + ' minuto(s).';
}

var converter = document.getElementById("converter")
converter.addEventListener("click", calcular)