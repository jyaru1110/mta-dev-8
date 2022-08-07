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
        var buffer_size = localStorage.buffer_size
        var id = localStorage.product_id
        if(value=="nr"){
            this.$('.label-recomendacion').text("Buffer no requiere ser ajustado");
            this.$('.button-confirmar').css("display","none");
        }else if(value=="ibs"){
            var new_buffer_size = Math.round(buffer_size*1.33);
            this.$('.label-recomendacion').text("Incrementar buffer size a "+new_buffer_size);
        }else if(value="dbs"){
            var new_buffer_size = Math.round(buffer_size*0.66);
            this.$('.label-recomendacion').text("Reducir buffer size a "+new_buffer_size);
        }
        this.$('.button-confirmar').click(()=>{
            var enlace = "/set_buffer_size/"+new_buffer_size+"/"+id;
            console.log(enlace)
            ajax.jsonRpc(enlace, 'call', {}, {
                'async': false
            }).then((data)=>{
                location.reload();
            })
        })
    },
})
fieldRegistry.add('recomendacion_widget', RecomendacionWidget);