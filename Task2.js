//Задание 2
if (!("a" in window)) {
    var a = 1;
}
alert(a); // всплывающее окно function a() {alert(this);}
var b = function a(x) {
    x && a(--x);
};
alert(a); // всплывающее окно function a() {alert(this);}

function a(x) {
    return x * 2;
}
var a;
alert(a); // всплывающее окно function a() {alert(this);}

function b(x, y, a) {
    arguments[2] = 10;
    alert(a); // не участвует 
}
b(1, 2, 3); // вызывает var b = function a(x) {x && a(--x);}; 

function a() {
    alert(this); // всплывающее окно [object Window]
}
a.call(null);