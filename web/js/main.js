"use strict";

async function display_weather() {
    // принимаю в переменную place значение из поля при вводе города
    let place = document.getElementById('location').value;
    // и тут понял ли я правельно, кусок этот кода я спиздил у хауди хо... кароче
    // передаю параметр (place) в и вызываю пайтон функцию уже с этим параметром а результат выполнения записывается уже в res
    let res = await eel.get_weather(place)();
    // передаю результат выполнения пайтон функции в ХТМЛ ну и он выводится
    document.getElementById('info').innerHTML = res;
}