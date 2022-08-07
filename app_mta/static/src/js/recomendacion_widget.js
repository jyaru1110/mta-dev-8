/** @odoo-module **/
import AbstractField from 'web.AbstractField';
import fieldRegistry from 'web.field_registry';
var RecomendacionWidget = AbstractField.extend({
    template: "RecomendacionWidget",
    start: function(){
        this._super.apply(this, arguments);
        if (this.recordData[this.nodeOptions.currentValue]){
            this.value = this.recordData[this.nodeOptions.currentValue]
        }
    },
    _render: function() {
        var self = this;
        var value = this.value;
        var ajax = require('web.ajax');
        this.$('.label-recomendacion').text(value);
        this.$('.button-confirmar').display("none");
        
    },
})
fieldRegistry.add('recomendacion_widget', RecomendacionWidget);