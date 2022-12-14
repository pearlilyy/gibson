// Gibson sub_history

$(document).ready(function(){
    
    $('#bar').draggable({
        axis: 'y',
        containment: 'parent'
    });
    
    var barmax = 4350;
    //바의 최대 이동값, 전체너비 - 바의 크기
    var barpos;
    //바의 이동값
    var conmax = 1000;
    //컨텐츠 최대 이동값, 크기-보여지는 영역
    var conpos;
    //컨텐츠 이동값
    
    $('#bar').on('drag',function(){
        
        barpos = $(this).offset().top;
        console.log(barpos);
        
        conpos = barpos * conmax / barmax;
        
        $('.history').css({
            top: -conpos + 'px'
        });
        
    });
    
    
}); //jQuery