/* Gibson sub_fix js */

$(document).ready(function(){
    
    

    

    var fileTarget = $('#fix_file');
    fileTarget.on('change',function(){
        if(window.FileReader){
            var filename = $(this)[0].files[0].name;
        }else{
            var filename = $(this).val().split('/').pop().split('\\').pop();
        }
            
        $(this).siblings('.file_name').val(filename);
    });
    
    
}); //jQuery