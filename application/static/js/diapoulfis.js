$(document).ready(function(){
    $('#for_pastoral_dairy').hide();
    $('#for_pastoral_poultry').hide();
    $('#for_pastoral_fish').hide();
})
$('#kind_of_pastoral').change(function(){
    if($(this).val()=="none"){
        $('#for_pastoral_dairy').hide();
        $('#for_pastoral_poultry').hide();
        $('#for_pastoral_fish').hide();
    }
    else if($(this).val()=="Dairy"){
        $('#for_pastoral_poultry').hide();
        $('#for_pastoral_fish').hide();
        $('#for_pastoral_dairy').show();
    }
    else if($(this).val()=="Poultry"){
        $('#for_pastoral_dairy').hide();
        $('#for_pastoral_fish').hide();
        $('#for_pastoral_poultry').show();
    }
    else if($(this).val()=="Fish"){
        $('#for_pastoral_dairy').hide();
        $('#for_pastoral_poultry').hide();
        $('#for_pastoral_fish').show();
    }
})