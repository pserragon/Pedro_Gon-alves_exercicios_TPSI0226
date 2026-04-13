// criar 

let name = "nelson";
var age = 10;
const country = "portugal ";

// estroturas de control 
// estruturas de desição     if   else
// esturas de repeticaao      for/while/ for each....

// funções

// vantagem: evitar repetição de codigo; particionar o nosso codigo

//as funcoes podem ou nao retornar

function somar() {
    return 
}

//podemos dados da função - chamam se argumentos 
function soma2(numero1, numero2){
    let soma = numero1 +  numero2
    return soma;

}


function cumprimentar (){
console.log ("Olá programador")

}



soma();
console.log(soma2(5, 5))
cumprimentar();


// funcao com valor default

function saudaçao(nome = "visitante"){
    console.log("ola" + nome);
}
saudaçao();

saudaçao("Pedro");

// outras formas de declarar funções

// funçao atribuida a uma variavel 

const multi = function(a, b){
return a * b;
};

console.log(multi(a, b));


//ES6 arrow function 

const soma3 = (a, b) => a + b;
return a + b;

const soma4 = (a, b) => a + b;
return a * b;

// funcao par ou impar (resto da divisão) %)

function parOuImpar(numero) {

    let resultado;

    if (numero % 2 == 0) {
        resultado = "Par";
    } else {
        resultado = "Ímpar";
    }

    return resultado;
}


// funcao se par ou impar 

function parOuImpar(numero) {
    let resultado = numero % 2;
if (resultado = 0){
console.log("o numero inserido e par " + "(" + numero +")");
else {
    console.log(`O número inserido é impar (${numero})`);

}

}

    console.log(resultado);
}
    parOuImpar(10);
    parOuImpar(5);

    // calculadora 

    function calculadora(num1, num2, operacao) {

    let resultado;

    if (operacao == "+") {
        resultado = num1 + num2;
    }
    else if (operacao == "-") {
        resultado = num1 - num2;
    }
    else if (operacao == "*") {
        resultado = num1 * num2;
    }
    else if (operacao == "/") {
        resultado = num1 / num2;
    }
    else {
        resultado = "Operação inválida";
    }

    return resultado;
}









