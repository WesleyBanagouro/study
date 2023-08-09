var agora = new Date();
var hora = agora.getHours();
var minutos = agora.getMinutes();
var horario = window.document.getElementById('horario');
horario.innerHTML = `Agora são ${hora}h${minutos}.`;