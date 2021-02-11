'use strict';

class Item {

    constructor(title = 'Good choise', price = 'Low price', description = 'You will never find a better offer', image = 'img/wrong.png') {
        this.title = title;
        this.price = price;
        this.description = description;
        this.image = image;
    }
}

let beretta = new Item('Beretta 92FS', 850, 'Classic choise', 'img/beretta.jpg');
let p8 = new Item('H&K P8', 985, 'German quality', 'img/p8.jpg');
let scorpion = new Item('Scorpion EVO3', 1200, 'Pretty and effective', 'img/scorpion.jpg');
let leopard = new Item('Leopard 2A7', 6300000, 'If you REALLY in trouble', 'img/leo.png');

class GoodsList {

    constructor(...theArgs) {
        this.goods = theArgs;
        this.summary = this.allPrice();
    }

    allPrice() {
        let price = 0;
        for (let i in this.goods) {
            price += this.goods[i].price;
        }
        return price;
    }
}

let goods = new GoodsList(beretta, p8, scorpion, leopard);

const renderGoodsItem = (item) => {
    return `<div class="goods-item"><h3>${item.title}</h3>
    <img src="${item.image}" alt="" class='weapon_image'></img>
    <p>${item.description}</p>
    <p>${item.price}$</p>
    <button class="buy-button" type="button">Add to cart</button></div>`
        ;
};

const renderGoodsList = (list) => {
    let goodsList = list.goods.map(item => renderGoodsItem(item));
    for (let i in goodsList) {
        document.querySelector(".goods-list").innerHTML += goodsList[i];
    }
}

renderGoodsList(goods);