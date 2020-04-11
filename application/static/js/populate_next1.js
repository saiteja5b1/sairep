$(document).ready(function(){
    $('#opt-a').hide();
    $('#opt-b').hide();
    $('#opt-c').hide();
    $('#opt-d').hide();
    $('#Mono').hide();
})
function show_rest1(exx){
    $('#opt-a').show();
}
function show_rest2(exx){
    $('#opt-b').show();
}
function show_rest3(exx){
    $('#opt-c').show();
}
function show_rest4(exx){
    $('#opt-d').show();
}
function next_sel(){
    var ddl=document.getElementById("taste_of_crop");
    var selectedvalue=ddl.options[ddl.selectedIndex].value;
    if(selectedvalue=="mon"){
        $('#Mono').show();
    }
}
