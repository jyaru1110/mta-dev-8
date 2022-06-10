'use strict'

odoo.define('app_mta.javascript', function (require) {
    require('web.dom_ready');
    var ajax = require('web.ajax');
    var botones = document.getElementsByClassName('condition')
    //var _onButtonClick = function (e) {
    //    console.log(e)
    //    ajax.jsonRpc('get_products', 'call', {}).then(function (data) {
    //        console.log(data)
    //    });
    //}
    //botones[0].addEventListener('click', _onButtonClick);
    console.log("condition classes:")
    console.log(botones)
});