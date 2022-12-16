//Gibson main.js

$(document).ready(function(){
    
    
    /*비디오 박스 바깥에서 들어오기 효과*/
    function videoSet(){
        $('.video_txt').css({
            right: -1000
        });
    } //.video_txt 셋팅
    videoSet();
    
    
    /*마우스 스크롤*/
    $(window).scroll(function(){
        
        var scTop = $(this).scrollTop();
        console.log('스크롤 굴러가고 있다규~ '+scTop);
        
        if(scTop > 0 && scTop < 895){
            var MouseDown = $('.mouse').animate({
            bottom: '50'
        },600, 'easeInOutCirc');
            var MouseUp = $('.mouse').animate({
            bottom: '0'
        },800, 'easeInOutCirc');
        }
        
        if(scTop >=3170 && scTop <=3800){
            $('.video_txt').animate({
                right: 0
            },2000,'easeOutBounce');
        } //.video_txt 바깥에서 안으로 이동
        
    }); //window scroll
    
    
    /*메인 글씨 나타나기 효과*/
    function MainSet(){
        $('.main_txt h1').css({
            opacity: '0',
        });
    } //.main_txt 셋팅
    
    MainSet();
    $('.main_txt h1').animate({
        opacity: 1
    },5000); //.main_txt 등장
    
    
    /////.guitars slide/////////////////////////////////////////
    
    /*변수 할당*/
    var gidx = $('.guitar_img a').eq(2);
    
    //////////////////////////////////////////
    
    /*기타 슬라이드 함수*/
    function guitar_slide (){
        $('.guitar_img a:first').appendTo('.guitar_img');
        //var gidx = $('.guitar_img a').eq(2);
        $(gidx).children('img').addClass('guitar_on').parent().siblings().children('img').removeClass('guitar_on');
        
        var gnum = $('.guitar_img a:eq(2)').children('img').attr('src').split('/')[2].split('_')[1].split('.')[0];
        gnum = Number(gnum);
        var bnum = gnum -1;
        $('.btns ul li').eq(bnum).addClass('btn_on',300).siblings().removeClass('btn_on');
        
        $('.guitar_txt ul li').eq(bnum).addClass('txt_on').siblings().removeClass('txt_on');
    }
    
    var guitar_auto = setInterval(function(){
        guitar_slide();
    },2000);
    
    
    /*기타 버튼(5개) 클릭*/
    
    $('.btns ul li').click(function(){
        
        
        $(this).addClass('btn_on',300).siblings().removeClass(); //버튼 클래스 추가
        
        var idx = $(this).index();
        //console.log(idx);
        
        var cname = 'num' +(idx + 1);
        
        $('.guitar_img a img.'+cname).addClass('guitar_on').parent().siblings().children('img').removeClass('guitar_on'); //버튼에 맞는 기타 이미지 클래스 추가
        
        
        $('.guitar_txt ul li').eq(idx).addClass('txt_on').siblings().removeClass(); //텍스트 클래스 추가
        
        
        var gidx = $('.guitar_img a').eq(idx);
        /*$(gidx).children('img').addClass('guitar_on').parent().siblings().children('img').removeClass('guitar_on');*/ //기타 이미지 클래스 추가
        
        
        
    }); //.btns 버튼 클릭
    
    
    
    /*이전 버튼 클릭*/
    
    $('#prev').click(function(e){
        e.preventDefault();
        
        $('.guitar_img a:last').prependTo('.guitar_img'); //기타 마지막 이미지 맨 앞으로 이동
        
        //var gidx = $('.guitar_img a').eq(2);
        $(gidx).children('img').addClass('guitar_on').parent().siblings().children('img').removeClass('guitar_on'); //기타 중앙 이미지 클래스 추가
        
        var gnum = $('.guitar_img a:eq(2)').children('img').attr('src').split('/')[2].split('_')[1].split('.')[0];
        gnum = Number(gnum);
        //console.log('기타 중간이미지 번호? '+gnum);
        
        var bnum = gnum -1;
        $('.btns ul li').eq(bnum).addClass('btn_on',300).siblings().removeClass('btn_on'); //prev클릭>>버튼 클래스 추가
        
        $('.guitar_txt ul li').eq(bnum).addClass('txt_on').siblings().removeClass('txt_on');
        
    }); //#prev click
    
    
    /*다음 버튼 클릭*/
    
    $('#next').click(function(e){
        e.preventDefault();
        
        $('.guitar_img a:first').appendTo('.guitar_img'); //기타 첫 이미지 마지막으로 이동
        
        var gid = $('.guitar_img a').eq(2);
        $(gid).children('img').addClass('guitar_on').parent().siblings().children('img').removeClass('guitar_on'); //기타 중앙 이미지 클래스 추가
        
        
        var gnum = $('.guitar_img a:eq(2)').children('img').attr('src').split('/')[2].split('_')[1].split('.')[0];
        gnum = Number(gnum);
        //console.log('기타 중간이미지 번호? '+gnum);
        
        var bnum = gnum-1;
        $('.btns ul li').eq(bnum).addClass('btn_on',300).siblings().removeClass('btn_on'); //next클릭>>버튼 클래스 추가
        
        $('.guitar_txt ul li').eq(bnum).addClass('txt_on').siblings().removeClass('txt_on');
        
    }); //#next click
    
    
    /*영상 플레이와 모달창*/
    
    var playIn = '<iframe id="player" width="830" height="467" src="https://www.youtube.com/embed/npOOEWaTadA?autohide=1&rel=0&showinfo=0&title=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    
    /*.video 호버*/
    $('.video_inner').mouseenter(function(){
        $('.cover').stop().fadeOut(200);
    }).mouseleave(function(){
        $('.cover').stop().fadeIn(100);
    });
    
    
    /*.video 플레이 버튼 클릭*/
    $('.play_btn').click(function(e){
        e.preventDefault();
        
        $('#modal').fadeIn(600);
        
        $('#xbtn').click(function(e){
            e.preventDefault();
            $(this).children('a:first').animate({
                rotate: '-45deg',
                opacity: '0.1'
            },600);
            $(this).children('a:last').animate({
                rotate: '45deg',
                opacity: '0.1'
            },600);
            $('#modal').delay(600).fadeOut(function(){
                $('.modal_wrap').empty();
            });
            
        }); //닫기 버튼 클릭 시
        
        $('.modal_wrap').fadeIn(400,function(){
            $('.modal_wrap').html(playIn);
        });
        $('#xbtn').children('a').stop().css({
            opacity: '1',
            rotate: '0deg'
        });
    }); //.play_btn click
    
    
    
}); //jQuery