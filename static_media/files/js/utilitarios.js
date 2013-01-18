$(document).ready(function(){
    $('.escondete').css('display','none');

    $("#id_nombre_mercado").bind("change", function(e){
        $('.escondete').fadeIn(1000);
       
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
                forms.append('<tr>');
                var select = $('<select name="product-'+k+'"></select>').appendTo(forms);
                $('<option value"'+k+'">'+data.productos[k]+'</option>').appendTo(select);
                var unidad = $('<td><input type="text" name="unidad-'+k+'" value="'+data.unidadf[k]+'" readonly/></td>').appendTo(forms);
                var volumen_venta = $('<td><input value=0 type="text" name="volumen-'+k+'" /></td>').appendTo(forms);
                var precio_promedio = $('<td><input value=0 type="text" name="promedio-'+k+'" /></td>').appendTo(forms);
                var precio_municipal = $('<td><input value=0 type="text" name="municipal-'+k+'" /></td>').appendTo(forms);
                var selecto = $('<select name="calidad-'+k+'"></select> <br>').appendTo(forms);
                for(var i=0; i < datos.length; i++) {
                selecto.append('<option value="'+datos[i].value+'">'+datos[i].text+'</option>');
                }
                forms.append('</tr>');
            }
            
            var forms2 = $('#forms2').html('');
            for (u in data.procesado){
                forms2.append('<tr id="line_p'+u+'">');
                var select = $('<select name="productp-'+u+'"></select>').appendTo(forms2);
                $('<option value"'+u+'">'+data.procesado[u]+'</option>').appendTo(select);
                var unidad = $('<td><input type="text" name="unidad-'+u+'" value="'+data.unidadp[u]+'" readonly/></td>').appendTo(forms2);
                var volumen_venta = $('<td><input value=0 type="text" name="volumenp-'+u+'" /></td>').appendTo(forms2);
                var precio_promedio = $('<td><input value=0 type="text" name="promediop-'+u+'" /></td>').appendTo(forms2);
                var precio_municipal = $('<td><input  value=0 type="text" name="municipalp-'+u+'" /></td>').appendTo(forms2);
                var selecto2 = $('<select name="calidadp-'+u+'"></select> <br>').appendTo(forms2);
                for(var i=0; i < datos.length; i++) { 
                selecto2.append('<option value="'+datos[i].value+'">'+datos[i].text+'</option>');
                }
                forms2.append('</tr>');
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