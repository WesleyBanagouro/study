function locadora () {
    var preco = document.getElementById("valor").value;
    var tempo = document.getElementById("tempo").value;
    var calculo = preco * Math.ceil(tempo / 15  );
    var valor_pagar = document.getElementById("pagar");
    valor_pagar.textContent = 'Como você ficou ' + tempo + ' minutos, o valor é de R$ ' + calculo + '.';
}

var calcular = document.getElementById("calcular")
calcular.addEventListener("click", locadora)