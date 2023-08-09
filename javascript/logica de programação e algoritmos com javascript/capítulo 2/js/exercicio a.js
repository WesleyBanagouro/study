function promocao () {
    var medicamento = document.getElementById("medicamento").value;
    var preco = Number(document.getElementById("preco").value);
    var quantidade = document.getElementById("quantidade").value;
    var preco_desconto = Math.floor(preco * quantidade);
    var outmedicamento = document.getElementById("nome_medicamento");
    var promocao = document.getElementById("promocao");
    outmedicamento.textContent = medicamento
    promocao.textContent = 'Leve ' + quantidade + ' por apenas R$ ' + preco_desconto.toFixed(2) + '.'
}

var calcular = document.getElementById("desconto")
calcular.addEventListener("click", promocao)