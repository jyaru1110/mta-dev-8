'use strict'

odoo.define('app_mta.javascript', function (require) {
    require('web.dom_ready');
    var botones = document.getElementsByClassName('condition')
    console.log("condition classes:")
    console.log(botones)
});