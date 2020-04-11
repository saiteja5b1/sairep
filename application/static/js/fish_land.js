// $(document).ready(function(){
//     $('#fish_lands').on('change',function(){
//         var howmuch=$(this).val();
//         var appendhtml='';
//         for(i=0;i<howmuch;i++){
//             appendhtml+="<input name="+i+" value="+">";
//         }
//         $('.appendform').append(appendhtml);
//     });
// });
$('#fish_lands').change(function(){
    var inpp=$(this).val();
    $('#inp').empty();
    for(var i=0;i<inpp;i++){
        $("#inp").append('<input type="number" name="input[]"/>');
    }
});