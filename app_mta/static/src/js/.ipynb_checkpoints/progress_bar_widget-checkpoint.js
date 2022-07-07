/** @odoo-module **/
var fieldRegistry = require('web.field_registry');
var FieldChar = require('web.basic_fields').FieldChar;

var ProgressBarWidget = FieldChar.extend({
    
    _renderReadonly: function () {
        /*var self = this;
        var value = this.value;
        var max_value = 100;
        value = value || 0;
        var widthComplete;
        if (value <= max_value){
            widthComplete = parseInt(value/max_value * 100);
        }
        else{
            widthComplete = 100;
        }*/
        this.$('.progress_number').text('HOLA');
        //this.$('.progress-bar-inner').css('width', widthComplete + '%');
    },
})
fieldRegistry.add('progress_bar_widget', ProgressBarWidget);