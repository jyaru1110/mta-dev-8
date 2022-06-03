'use strict'

odoo.define('app_mta.javascript', function (require) {
    require('web.dom_ready');
    var ajax = require('web.ajax');
    var boton = $('.boton_js');
    var _onButtonClick = function (e) {
        console.log(e)
    }
    boton.addEventListener('click', _onButtonClick);
});