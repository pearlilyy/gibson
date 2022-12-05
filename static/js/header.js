//Gibson header.js

$(document).ready(function () {

    /*서브 메뉴*/
    $('.main_menu').mouseenter(function () {
        $('.sub_menu').stop().slideDown();

        $('.sub_menu li').hover(function () {
            $(this).children('a').children('img').stop().fadeIn();
        }, function () {
            $(this).children('a').children('img').stop().fadeOut(200);
        });

    }).mouseleave(function () {

        $('.sub_menu').hide();

    }); //.sub_menu hover


    /*언어 버튼 호버시 메뉴*/
    $('.global').hover(function () {

        $(this).children('a').children('img').stop().animate({
            rotate: '-270deg'
        }, 300);

        $(this).children('.language').slideDown();
    }, function () {
        $(this).children('a').children('img').stop().animate({
            rotate: '0deg'
        }, 300);

        $(this).children('.language').hide();
    }); //.language 메뉴 보이기


    /*언어 버튼 클릭*/
    $('.global>a').click(function (e) {
        e.preventDefault();
    }); //.global click

    /*햄버거 버튼 호버*/
    $('.hamburger').mouseenter(function () {
        $('.hamburger span').addClass('move');

    }).mouseleave(function () {
        $('.hamburger span').removeClass('move');
    }); //.hamburger hover

    /*햄버거 버튼 클릭*/
    achg = false;
    $('.hamburger').click(function (e) {
        e.preventDefault();

        if (achg) {
            achg = false;
            $('.aside_in').animate({
                right: '-300px'
            });
            $('.hamburger span').removeClass('on');
        } else {
            achg = true;
            $('.aside_in').animate({
                right: 0
            });
            $('.hamburger span').addClass('on');
        }
    });

    /*돋보기 버튼 클릭*/
    $('.magnifying').click(function (e) {

        e.preventDefault();

    }); //magnifying click

    $(window).scroll(function () {
        var scTop = $(this).scrollTop();
    });

    var aw = $('aside').offset().left;
    var amw = $('.aside_in').offset().left;
    console.log('aside ' + amw);


}); //jQuery