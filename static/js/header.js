//Gibson header.js

$(document).ready(function(){
    
    /*서브 메뉴*/
    $('.main_menu').mouseenter(function(){
        
        $('.sub_menu').slideDown();
        $('.sub_menu').mouseover(function(){
            $(this).show();
        });
    });
    $('.main_menu, .sub_menu').mouseleave(function(){
        
        $('.sub_menu').hide();
    }); //.sub_menu hover
    
    
    /*언어 버튼 호버시 메뉴*/
    $('.global').hover(function(){
        
        $(this).children('a').children('img').stop().animate({
            rotate: '-270deg'
        },300);
        
        $(this).children('.language').slideDown();
    }, function(){
        $(this).children('a').children('img').stop().animate({
            rotate: '0deg'
        },300);
        
        $(this).children('.language').hide();
    }); //.language 메뉴 보이기
    
    
    /*언어 버튼 클릭*/
    $('.global>a').click(function(e){
        e.preventDefault();
    }); //.global click
    
    
    /*햄버거 버튼 클릭*/
    $('.hamburger').click(function(e){
        
        e.preventDefault();
        $('.sub_menu').stop().slideToggle();
    }); //.hamburger click
    
    
    /*돋보기 버튼 클릭*/
    $('.magnifying').click(function(e){
        
        e.preventDefault();
        
    }); //magnifying click
    
    
    
    $(window).scroll(function(){
        
        var scTop = $(this).scrollTop();
        
        
        
    });
    
    
    
    
    
}); //jQuery