'use strict';

const goods = [
    { title: 'Beretta 92FS', price: 850, description: 'Classic choise', image: 'img/beretta.jpg' },
    { title: 'H&K P8', price: 985, description: 'German quality', image: 'img/p8.jpg' },
    { title: 'Scorpion EVO3', price: 1200, description: 'Pretty and effective', image: 'img/scorpion.jpg' },
    { title: 'Leopard 2A7', price: 6300000, description: 'If you REALLY in trouble', image: 'img/leo.png' },
];

const renderGoodsItem = (title = 'Good choise', price = 'Low price', description = 'You will never find a better offer', image = 'img/wrong.png') => {
    return `<div class="goods-item"><h3>${title}</h3>
    <img src="${image}" alt="" class='weapon_image'></img>
    <p>${description}</p>
    <p>${price}$</p>
    <button class="buy-button" type="button">Add to cart</button></div>`
        ;
};

const renderGoodsList = (list) => {
    let goodsList = list.map(item => renderGoodsItem(item.title, item.price, item.description, item.image));
    for (let i in goodsList) {
        document.querySelector(".goods-list").innerHTML += goodsList[i];
    }
}

renderGoodsList(goods);

var audio_element = document.createElement("audio");
audio_element.src = "music/Resident Evil 4 - Serenity.mp3";
document.body.appendChild(audio_element)
audio_element.play();