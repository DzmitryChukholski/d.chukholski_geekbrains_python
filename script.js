const defFunc = function () {
    alert('Согласно распоряжению министерства строительсва социализма с целью приближения наступления светлого социалистического будущего приобретение товара производится по схеме "Один товар в одни руки", а кто с этим несогласен тот капиталистическая свинья, враг народа и поедет в гулаг')
}

const newInCard = function () {
    console.log(inCard)
    totalPrice = 0
    inside.innerHTML = ''
    for (const el in inCard) {
        inside.innerHTML += inCard[el].name + '<br>'
        totalPrice += inCard[el].price
    }
    price.innerHTML = totalPrice + ' конфетти'
}

const ruletikFunc = function () {
    inCard.push(ruletikInfo)
    newInCard()
    ruletik.removeEventListener('click', ruletikFunc)
    ruletik.addEventListener('click', defFunc)
}

const gazonFunc = function () {
    inCard.push(gazonInfo)
    newInCard()
    gazon.removeEventListener('click', gazonFunc)
    gazon.addEventListener('click', defFunc)
}

const happyFunc = function () {
    inCard.push(happyInfo)
    newInCard()
    happy.removeEventListener('click', happyFunc)
    happy.addEventListener('click', defFunc)
}

const ruletik = document.getElementById('ruletik');
const gazon = document.getElementById('gazon');
const happy = document.getElementById('happy');
const inside = document.getElementById('inside');
const price = document.getElementById('price');

ruletik.addEventListener('click', ruletikFunc);
gazon.addEventListener('click', gazonFunc);
happy.addEventListener('click', happyFunc);

let ruletikInfo = {
    name: 'Мясной рулетик',
    price: 750
}

let gazonInfo = {
    name: 'Газонокосилка',
    price: 15000
}

let happyInfo = {
    name: 'Кигуруми',
    price: 4000
}

let inCard = [];