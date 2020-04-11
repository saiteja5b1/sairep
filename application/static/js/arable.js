$(document).ready(function(){
    $('#for_arable').hide();
    $('#Poly').hide();
    $('#Mono').hide();
})
$('#taste_of_crop').change(function(){
    $('#for_arable').show();
})
$('#taste_of_crop').change(function(){
    if($(this).val()=="none"){
        $('#Poly').hide();
        $('#Mono').hide();
    }
    else if($(this).val()=="Monoculture"){
        $('#crop_name').show();
        $('#Poly').hide();
        $('#Mono').show();
    }
    else if($(this).val()=="Polyculture"){
        $('#crop_name').hide();
        $('#Mono').hide();
        $('#Poly').show();
    }
})