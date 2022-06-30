'use strict'

odoo.define('app_mta.javascript', function (require) {
    var botones = document.getElementsByClassName('condition')
    console.log("condition classes 2:")
    console.log(botones)
    console.log("Cargado");
    console.log("antes each");
    console.log($(".condition"))
    console.log(botones.length)
    /*$( ".condition" ).each( function(parametro) { console.log(parametro);} );
    console.log("tras each");*/
});