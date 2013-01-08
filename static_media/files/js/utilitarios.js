$(document).ready(function(){
    $("#id_mercado").bind("change", function(e){
        var mercado = $(this).val();
        $.post('/reqdata/', {mercado:mercado}, function(data){
            data = eval('('+data+')');

            var forms = $('#forms').html('');
            for (k in data.productos){
                var select = $('<select name="product-'+k+'"></select>').appendTo(forms);
                $('<option value"'+k+'">'+data.productos[k]+'</option>').appendTo(select);
                var cantidad = $('<input type="text" name="cant-'+k+'" /> <br>').appendTo(forms);
            }
        });
    });
});