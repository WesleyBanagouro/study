function supermercado () {
    var produto = document.getElementById("produto").value;
    var preco = document.getElementById("preco").value;
    var terceiro_produto = preco * 0.5;
    var total = 2 * preco + terceiro_produto;
    var promocao_total = document.getElementById("preco_promocao");
    var terceiro = document.getElementById("terceiro");
    promocao_total.textContent = produto + ' - Promoção: Leve 3 por R$ ' + total + '.';
    terceiro.textContent = 'O 3º produto sai por R$' + terceiro_produto + '.';
}

var ver_promocao = document.getElementById("promocao")
ver_promocao.addEventListener("click", supermercado)