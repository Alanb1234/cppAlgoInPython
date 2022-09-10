$(document).ready(function(){
    $('form').on('submit', function(event){
        $.ajax({
            data: {
                algorithms : $('#algorithms').val() ,
                size : $('#size').val()
            },
            type: "POST",
            url: '/'
        })

        .done(function(data){

            if(data.error){
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();

            }
            else{
                $('#successAlert').text(data.algorithms).show();
                $('#errorAlert').hide();

            }



        });

        event.preverntDefault();





    })


});