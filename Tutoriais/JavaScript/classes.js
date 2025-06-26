/* 
const corredor1 = {
    nome: 'Ayrton Senna',
    equipe: 'McLaren',
    idade: 29,
    correr: function(){
        console.log('Vrum!')
    },
}

const corredor2 = {
    nome: 'Max Verstappen',
    equipe: 'Red Bull',
    idade: 26,
    correr: function(){
        console.log('Vrum!')
    },
}
*/

// Exemplo 1 de classe:
/*
class PilotoFormula1 {
    nome = '';
    equipe = '';
    idade = 0;
    correr() {
        console.log('Vruuum!');
    };
}

const corredor1 = new PilotoFormula1();
console.log(corredor1);
corredor1.nome = 'Ayrton Senna';
corredor1.equipe = 'McLaren';
corredor1.idade = '29';
console.log(corredor1);
corredor1.correr();

*/

// Exemplo 2 de classe:

class PilotoFormula1 {
    constructor(nome, equipe, idade){
        this.nome = nome;
        this.equipe = equipe;
        this.idade = idade;
    }

    correr() {
        console.log('Vruuum!');
    };
}

const corredor1 = new PilotoFormula1('Fernando', 'Red Bull', 20);
console.log(corredor1)