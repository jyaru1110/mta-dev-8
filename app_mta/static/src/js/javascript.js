'use strict'

odoo.define('app_mta.javascript', function (require) {
    require('web.dom_ready');
    var ajax = require('web.ajax');
    var boton = $('.boton_js');
    var _onButtonClick = function (e) {
        console.log(e)
        ajax.jsonRpc('get_products', 'call', {}).then(function (data) {
            console.log(data)
        });
    }
    boton.addEventListener('click', _onButtonClick);
});