function sub(a, b){
    return a - b;
};

function somarDois(a){
    return a + 2;
};

function diaDoMes(){
    return (new Date()).getDate();
};

function superfuncao(a,b){
    let subtracao = a - b;
    subtracao -= 2;
    let diaDoMes = new Date().getDate();
    return diaDoMes - subtracao;
}

// Arrow Function

const sub2 = (a, b) => a - b;

const somarDois2 = (a) =>  a + 2;

const diaDoMes2 = () => (new Date()).getDate();

const superfuncao2 = (a,b) =>{
    let subtracao = a - b;
    subtracao -= 2;
    let diaDoMes = new Date().getDate();
    return diaDoMes - subtracao;
}

