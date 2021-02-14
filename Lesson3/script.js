'use strict';

// 1. Переделайте makeGETRequest() так, чтобы она использовала промисы.
// ------------------ хотел бы я знать что такое makeGETRequest()......

// 2. Добавьте в соответствующие классы методы добавления товара в корзину, 
// удаления товара из корзины и получения списка товаров корзины.


// 3* Переделайте GoodsList так, чтобы fetchGoods() возвращал промис, а render() вызывался в обработчике этого промиса.
// ------------------ что за fetchGoods()??????



// домашнее задание написано так что вообще не понятно чего от меня хотят......



class Item {

    constructor(title = 'Good choise', price = 'Low price', description = 'You will never find a better offer', image = 'img/wrong.png') {
        this.title = title;
        this.price = price;
        this.description = description;
        this.image = image;
    }

    toString() {
        return this.title;
    }
}

class Cart {
    inCart = [];

    cartList() {
        return `
        In your cart is:
        ${this.inCart}
        Total price is:
        ${this.cartPrice()}`;
    };

    addToCart(item) {
        this.inCart.push(item);
    };

    removeFromCart(item) {
        const index = this.inCart.indexOf(item);
        if (index > -1) {
            this.inCart.splice(index, 1);
        }
    };

    cartPrice() {
        let price = 0;
        for (let i in this.inCart) {
            price += this.inCart[i].price;
        }
        return price;
    };
}

class GoodsList {

    constructor(...theArgs) {
        this.goods = theArgs;
        this.renderGoodsList();
    };

    renderGoodsList = () => new Promise((resolve, reject) => {
        let goodsList = this.goods.map(item => {
            return `<div class="goods-item"><h3>${item.title}</h3>
            <img src="${item.image}" alt="" class='weapon_image'></img>
            <p>${item.description}</p>
            <p>${item.price}$</p>
            <div class="buttons"><div><button class="buy-button" type="button" id="buy-${item.title}">Add to cart</button></div>
            <div><button class="remove-button" type="button" id="remove-${item.title}">Remove from cart</button></div></div></div>`;
        });
        for (let i in goodsList) {
            document.querySelector(".goods-list").innerHTML += goodsList[i];
        };
        return resolve;
    });
}

let beretta = new Item('Beretta 92FS', 850, 'Classic choise', 'img/beretta.jpg');
let p8 = new Item('H&K P8', 985, 'German quality', 'img/p8.jpg');
let scorpion = new Item('Scorpion EVO3', 1200, 'Pretty and effective', 'img/scorpion.jpg');
let leopard = new Item('Leopard 2A7', 6300000, 'If you REALLY in trouble', 'img/leo.png');

let goods = new GoodsList(beretta, p8, scorpion, leopard);

let myCart = new Cart();

document.getElementById("buy-Beretta 92FS").addEventListener("click", () => { myCart.addToCart(beretta) });
document.getElementById("remove-Beretta 92FS").addEventListener("click", () => { myCart.removeFromCart(beretta) });
document.getElementById("buy-H&K P8").addEventListener("click", () => { myCart.addToCart(p8) });
document.getElementById("remove-H&K P8").addEventListener("click", () => { myCart.removeFromCart(p8) });
document.getElementById("buy-Scorpion EVO3").addEventListener("click", () => { myCart.addToCart(scorpion) });
document.getElementById("remove-Scorpion EVO3").addEventListener("click", () => { myCart.removeFromCart(scorpion) });
document.getElementById("buy-Leopard 2A7").addEventListener("click", () => { myCart.addToCart(leopard) });
document.getElementById("remove-Leopard 2A7").addEventListener("click", () => { myCart.removeFromCart(leopard) });
document.getElementById("cart-button").addEventListener("click", () => { alert(myCart.cartList()) });