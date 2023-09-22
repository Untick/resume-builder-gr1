/*!
* Start Bootstrap - Shop Item v5.0.6 (https://startbootstrap.com/template/shop-item)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-item/blob/master/LICENSE)
*/

//import React from 'react';
//import 'bootstrap/dist/css/bootstrap.css';
//import ProgressBar from 'react-bootstrap/ProgressBar';
//
//
$(document).ready(function() {
  $('#inputField').on('input', function() {
    // Получаем текущее значение прогресса
    var progress = $('.progress-bar').attr('aria-valuenow');

    // Увеличиваем прогресс на 5%
    progress += 5;

    // Ограничиваем прогресс до 100%
    if (progress > 100) {
      progress = 100;
    }

    // Обновляем значение прогресса и стили progress bar
    $('.progress-bar').attr('aria-valuenow', progress).css('width', progress + '%');
  });
});

//// Получаем элементы формы и progress bar
//var form = document.getElementById('fullname');
//var progressBar = document.getElementById('progress-bar');
//
//// Чтобы отслеживать заполнение формы, можно использовать событие "input" по каждому полю
//form.addEventListener('input', function() {
//  // Вычисляем общий прогресс в процентах
//  var progress = 10;
//
//  // Обновляем стиль progress bar
//  progressBar.style.width = progress + '%';
//  progressBar.setAttribute('aria-valuenow', progress);
//  progressBar.innerHTML = progress + '%';
//});