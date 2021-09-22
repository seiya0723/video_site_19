$(function(){
    $('#read_btn').click(function() {
        $('input[name=already_read]:checked').each(function() {
        var v = $(this).val();

        let form_elem   = "#already_read";
        let data    = new FormData();
        data.set("id", v);

        let url     = $(form_elem).prop("action");
        let method  = $(form_elem).prop("method");

        //フォーム内のデータを確認できる
        for (let v of data.entries() ){ console.log(v); }

        //Ajaxを送信する
        $.ajax({
            url: url,
            type: method,
            data: data,
            processData: false,
            contentType: false,
            dataType: 'json'
        }).done( function(data, status, xhr ) {

            if (data.error){
                console.log(data.error);
            }
            else{
                console.log("既読処理完了");
                location.reload(false);
            }
            $('#tab_system_radio_1').prop('checked', true);
            $('input[name=already_read]:checked').prop('checked', false);

        }).fail( function(xhr, status, error) {
            console.log(status + ":" + error );
        });

        });
    });
});


$(function(){
    $('#comment_delete_btn').click(function() {
        $('input[name=already_read]:checked').each(function() {
        var v = $(this).val();

        let form_elem   = "#comment_delete";
        let data    = new FormData();
        data.set("id", v);

        let url     = $(form_elem).prop("action");
        let method  = $(form_elem).prop("method");

        //フォーム内のデータを確認できる
        for (let v of data.entries() ){ console.log(v); }

        //Ajaxを送信する
        $.ajax({
            url: url,
            type: method,
            data: data,
            processData: false,
            contentType: false,
            dataType: 'json'
        }).done( function(data, status, xhr ) {

            if (data.error){
                console.log(data.error);
            }
            else{
                console.log("コメント削除処理完了");
                location.reload(false);
            }
            $('#tab_system_radio_1').prop('checked', true);
            $('input[name=already_read]:checked').prop('checked', false);

        }).fail( function(xhr, status, error) {
            console.log(status + ":" + error );
        });

        });
    });
});