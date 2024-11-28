// Função para abrir o menu dropdown
function hamburg() {
    const dropdownMenu = document.querySelector('.dropdown');
    dropdownMenu.classList.add('active');
}

// Função para fechar o menu dropdown
function cancel() {
    const dropdownMenu = document.querySelector('.dropdown');
    dropdownMenu.classList.remove('active');
}