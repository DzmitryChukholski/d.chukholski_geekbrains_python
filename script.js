// 1. Создать функцию, генерирующую шахматную доску. При этом можно использовать любые html-теги по своему желанию. 
// Доска должна быть разлинована соответствующим образом, т.е. чередовать черные и белые ячейки. 
// Строки должны нумероваться числами от 1 до 8, столбцы – латинскими буквами A, B, C, D, E, F, G, H.
// 2. Заполнить созданную таблицу буквами, отвечающими за шахматную фигуру, например К – король, Ф – ферзь и т.п., 
// причем все фигуры должны стоять на своих местах и быть соответственно черными и белыми. (optoinal with images)


// Не без костылей с нелувой оптимизацией и без картинок, но вроде эта штука работает
// Я бы навёл красоту, но пока по командировкам шастаюсь нет времени упарываться в программуху, хотя это весело


const main_table = document.createElement('div');
main_table.classList.add('main_table');
document.body.appendChild(main_table)

let marks = [8, 7, 6, 5, 4, 3, 2, 1, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' ',];
let r = 0;

for (let i = 1; i < 10; i++) {
    let hor = document.createElement('div');
    hor.classList.add('horizontal_div');
    for (let j = 1; j < 10; j++) {
        let vert = document.createElement('div');
        let test = marks[7 + j]
        if (i % 2 == j % 2 && i < 9 && j < 9) {
            vert.classList.add('white_cell');
            vert.id = (String(test) + String(9 - i));
        } else if (i < 9 && j < 9) {
            vert.classList.add('black_cell');
            vert.id = (String(test) + String(9 - i));
        }
        if (i == 9 && j !== 9) {
            vert.classList.add('not_a_cell_i');
            vert.innerHTML = marks[r];
            r++;
        }
        if (j == 9 && i !== 9) {
            vert.classList.add('not_a_cell_j');
            vert.innerHTML = marks[r];
            r++;
        }
        if (i == 9 && j == 9) {
            vert.classList.add('not_a_cell');
        }
        hor.appendChild(vert);
    }
    main_table.appendChild(hor);
}

let chess = {
    'A1': 'Ладья',
    'B1': 'Конь',
    'C1': 'Слон',
    'D1': 'Король',
    'E1': 'Ферзь',
    'F1': 'Слон',
    'G1': 'Конь',
    'H1': 'Ладья',
    'A2': 'Пешка',
    'B2': 'Пешка',
    'C2': 'Пешка',
    'D2': 'Пешка',
    'E2': 'Пешка',
    'F2': 'Пешка',
    'G2': 'Пешка',
    'H2': 'Пешка',
    'A8': 'Ладья',
    'B8': 'Конь',
    'C8': 'Слон',
    'D8': 'Король',
    'E8': 'Ферзь',
    'F8': 'Слон',
    'G8': 'Конь',
    'H8': 'Ладья',
    'A7': 'Пешка',
    'B7': 'Пешка',
    'C7': 'Пешка',
    'D7': 'Пешка',
    'E7': 'Пешка',
    'F7': 'Пешка',
    'G7': 'Пешка',
    'H7': 'Пешка',
}

for (const key in chess) {
    let place = document.getElementById(key);
    const chess_container = document.createElement('div');
    chess_container.classList.add('chess_container');
    chess_container.innerHTML = chess[key];
    place.appendChild(chess_container);
}