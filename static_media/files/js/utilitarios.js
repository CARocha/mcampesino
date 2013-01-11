$(document).ready(function(){
    $('.escondete').css('display','none');

    $("#id_nombre_mercado").bind("change", function(e){
        $('.escondete').show();
       
        var mercado = $(this).val();
        $.post('/reqdata/', {mercado:mercado}, function(data){
            data = eval('('+data+')');
            
            var datos = [
                    {text:'Excelente', value:'1'},
                    {text:'Muy buena', value:'2'},
                    {text:'Buena', value:'3'},
                    {text:'Mala', value:'4'},
            ]

            var forms = $('#forms').html('');
            for (k in data.productos){
                var select = $('<select name="product-'+k+'"></select>').appendTo(forms);
                $('<option value"'+k+'">'+data.productos[k]+'</option>').appendTo(select);
                var unidad = $('<input type="text" name="unidad-'+k+'" value="'+data.unidadf[k]+'" readonly/>').appendTo(forms);
                var volumen_venta = $('<input type="text" name="volumen-'+k+'" />').appendTo(forms);
                var precio_promedio = $('<input type="text" name="promedio-'+k+'" />').appendTo(forms);
                var precio_municipal = $('<input type="text" name="municipal-'+k+'" />').appendTo(forms);
                var selecto = $('<select name="calidad-'+k+'"></select> <br>').appendTo(forms);
                for(var i=0; i < datos.length; i++) {
                selecto.append('<option value="'+datos[i].value+'">'+datos[i].text+'</option>');
                }
            }
            
            var forms2 = $('#forms2').html('');
            for (u in data.procesado){
                var select = $('<select name="productp-'+u+'"></select>').appendTo(forms2);
                $('<option value"'+u+'">'+data.procesado[u]+'</option>').appendTo(select);
                var unidad = $('<input type="text" name="unidad-'+u+'" value="'+data.unidadp[u]+'" readonly/>').appendTo(forms2);
                var volumen_venta = $('<input type="text" name="volumenp-'+u+'" />').appendTo(forms2);
                var precio_promedio = $('<input type="text" name="promediop-'+u+'" />').appendTo(forms2);
                var precio_municipal = $('<input type="text" name="municipalp-'+u+'" />').appendTo(forms2);
                var selecto2 = $('<select name="calidadp-'+u+'"></select> <br>').appendTo(forms2);
                for(var i=0; i < datos.length; i++) { 
                selecto2.append('<option value="'+datos[i].value+'">'+datos[i].text+'</option>');
                }
            }

        });
    
    });

    $('#formulariomovimiento input[name="_addanother"]').on('click', function(e){
       e.preventDefault();
       var fd = new FormData($("#formulariomovimiento").get(0));
       $.ajax({
               url: location.href,
               type: 'POST',
               data: fd,
               success: function(){
                       top.location = location.href;
               },
               processData: false,
               contentType: false
       });
    });

    $('#formulariomovimiento input[name="_save"]').on('click', function(e){
       e.preventDefault();
       var fd = new FormData($("#formulariomovimiento").get(0));
       $.ajax({
               url: location.href,
               type: 'POST',
               data: fd,
               success: function(){
                       top.location = '/admin/movimientos/movimiento';
               },
               processData: false,
               contentType: false
       });
    });
    
});