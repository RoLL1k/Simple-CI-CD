$(document).ready(function () {
    $('.menu-burger__header').click(function () {
        $('.menu-burger__header').toggleClass('open-menu').toggleClass('close-menu');
        $('.header__nav').toggleClass('open-menu');
    });
});
