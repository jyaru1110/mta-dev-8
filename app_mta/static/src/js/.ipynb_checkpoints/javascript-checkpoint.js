'use strict'

odoo.define('app_mta.javascript', function (require) {
    var botones = document.getElementsByClassName('condition')
    console.log("condition classes 4:")
    console.log(botones)
    console.log("Cargado");
    console.log("antes each");
    console.log($(".condition"));
    console.log(botones.length);
    
    console.log("botones_array");
    var botones_array = Array.prototype.slice.call( botones );
    console.log(botones_array);
    console.log(botones_array.length);
    console.log("botones_array_dos");
    var botones_array_dos = [...botones];
    console.log(botones_array_dos);
    console.log(botones_array_dos.length);
    document.write("XXX TEST TEST XXX");
    document.write(botones);
    /*$( ".condition" ).each( function(parametro) { console.log(parametro);} );
    console.log("tras each");*/
});