'use strict'

odoo.define('app_mta.javascript', function (require) {
    require('web.dom_ready');
    var botones = document.getElementsByClassName('condition')
    console.log("condition classes 2:")
    console.log(botones)
    
    $(document).ready(function(){
        $('.condition').each((boton)=>{
            console.log(boton)
        }
        )
    })
    
});