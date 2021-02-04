const equals3 = (a, b, c) => {
  return (a == b && b == c && a != '');
}

function checkWinner(model) {
  let winner = null;

  //EDRO
  function edro() {
    let surrender = 0;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (model[i][j] == '') {
          surrender = 1
        }
      }
    }

    if (surrender == 0) {
      return 'Единая Россия'
    }
  }

  // horizontal
  function horizontal() {
    for (let i = 0; i < 3; i++) {
      if (equals3(model[i][0], model[i][1], model[i][2])) {
        return model[i][0];
      }
    }
  }

  // vertical
  function vertical() {
    for (let i = 0; i < 3; i++) {
      if (equals3(model[0][i], model[1][i], model[2][i])) {
        return model[0][i];
      }
    }
  }

  // diagonal
  function diagonal() {
    if (equals3(model[0][0], model[1][1], model[2][2])) {
      return model[0][0];
    }
    if (equals3(model[0][2], model[1][1], model[2][0])) {
      return model[0][2];
    }
  }

  if (edro() != null) { winner = edro() }
  if (vertical() != null) { winner = vertical() }
  if (horizontal() != null) { winner = horizontal() }
  if (diagonal() != null) { winner = diagonal() }
  return winner;
}

const game = () => {
  const model = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
  ];
  const playerX = 'X';
  const playerO = 'O';
  let currentPlayer = playerX;

  const $game = document.querySelector('#game');
  const $table = document.createElement('table');
  $table.classList.add('$table');

  for (let i = 0; i < 3; i++) {
    const $tr = document.createElement('tr');
    $tr.dataset.index = i;

    for (let j = 0; j < 3; j++) {
      const $td = document.createElement('td');
      $td.dataset.index = j;
      $tr.appendChild($td);
    }

    $table.appendChild($tr);
  }

  $game.appendChild($table);

  $table.addEventListener('click', (e) => {
    const row = e.target.parentNode.dataset.index;
    const column = e.target.dataset.index;


    if (e.target.innerHTML == '') {
      model[row][column] = currentPlayer;
      e.target.innerHTML = currentPlayer;

      const winner = checkWinner(model);
      if (winner) {
        $game.removeChild($table);
        const $winner = document.createElement('h1');
        $game.appendChild($winner)
        $winner.innerHTML = `Победил/а: ${winner}`
        if (winner == 'Единая Россия') {
          $winner.innerHTML = `Победила`
          $game.classList.add('edinayaRossiya');
        }
      }
      // 1. tie

      currentPlayer = currentPlayer === playerX ? playerO : playerX;
    }
  });
}

window.onload = () => {
  game();
};
